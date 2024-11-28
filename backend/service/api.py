from flask import Flask, request, jsonify
import sqlite3
import pandas as pd

app = Flask(__name__)


DATABASE = "/Users/zafer/Documents/GitHub/salesense/salesense/database/database.sqlite" 

def query_db(query):
    conn = sqlite3.connect(DATABASE)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

@app.route("/analytics", methods=["POST"])
def analytics():
    try:
        analysis_type = request.json.get("type")
        result = {}

        if analysis_type == "top_products":
            query = """
                SELECT name, SUM(quantity) as total_quantity 
                FROM sales 
                GROUP BY name 
                ORDER BY total_quantity DESC 
                LIMIT 5
            """
            df = query_db(query)
            result = df.to_dict(orient="records")

        elif analysis_type == "top_countries":
            query = """
                SELECT country, SUM(quantity) as total_quantity 
                FROM sales 
                GROUP BY country 
                ORDER BY total_quantity DESC 
                LIMIT 5
            """
            df = query_db(query)
            result = df.to_dict(orient="records")

        elif analysis_type == "sales_by_date":
            query = """
                SELECT invoice_date, SUM(total_price) as total_sales 
                FROM sales 
                GROUP BY invoice_date 
                ORDER BY invoice_date DESC 
                LIMIT 7
            """
            df = query_db(query)
            result = df.to_dict(orient="records")

        # More analyses can be added here similarly

        return jsonify({"data": result})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/sales-overview", methods=["POST"])
def sales_overview():
    try:
        analysis_type = request.json.get("type")
        result = {}

        if analysis_type == "describe":
            query = """
                SELECT quantity, total_price, unit_price FROM sales 
            """
            df = query_db(query)
            describe = df.describe()
            result = describe.to_dict(orient="records")

        return jsonify({"data": result})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
