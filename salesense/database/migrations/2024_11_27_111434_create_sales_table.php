<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration {
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('sales', function (Blueprint $table) {
            $table->id('id');
            $table->string('stock_code');
            $table->string('name');
            $table->integer('quantity');
            $table->timestamp('invoice_date');
            $table->float('unit_price');
            $table->float('customer_id');
            $table->string('country');
            $table->integer('year');
            $table->integer('month');
            $table->integer('day');
            $table->integer('hour');
            $table->float('total_price');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('sales');
    }
};
