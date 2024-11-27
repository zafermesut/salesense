<?php

use App\Filament\Pages\SalesReports;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/sales-reports/products', [SalesReports::class, 'getTopProducts'])->name('sales-reports.products');
Route::get('/sales-reports/countries', [SalesReports::class, 'getTopCountries'])->name('sales-reports.countries');
Route::get('/sales-reports/sales', [SalesReports::class, 'getSalesByDate'])->name('sales-reports.sales');
