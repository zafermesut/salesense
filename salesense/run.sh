#!/bin/bash

# Python servisini başlat
echo "Starting Python API server..."
python3 /Users/zafer/Documents/GitHub/salesense/backend/service/api.py &
PYTHON_PID=$!

# Laravel server'ını başlat
echo "Starting Laravel server..."
php artisan serve --host=0.0.0.0 --port=8000

# Laravel servisi kapandığında Python servisini sonlandır
echo "Stopping Python API server..."
kill $PYTHON_PID
