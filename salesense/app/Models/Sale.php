<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Sale extends Model
{
    protected $table = 'sales';

    protected $fillable = [
        'stock_code',
        'name',
        'quantity',
        'invoice_date',
        'unit_price',
        'customer_id',
        'country',
        'year',
        'month',
        'day',
        'hour',
        'total_price',
    ];

    protected $casts = [
        'invoice_date' => 'datetime',
    ];


}
