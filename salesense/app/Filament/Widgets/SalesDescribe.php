<?php

namespace App\Filament\Widgets;

use Filament\Tables;
use Filament\Tables\Table;
use Filament\Widgets\TableWidget as BaseWidget;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Collection;

class SalesDescribe extends BaseWidget
{
    protected array $data = [];

    public function mount(): void
    {
        $this->fetchSalesData();
    }

    protected function fetchSalesData(): void
    {
        $response = Http::post(
            'http://127.0.0.1:5001/sales-overview',
            [
                'type' => 'describe'
            ]
        );

        if ($response->successful()) {
            $this->data = $response->json();
        } else {
            $this->data = []; // Hata durumunda boş bir dizi
        }
    }

    public function table(Table $table): Table
    {
        return $table
            ->query(
                $this->getDataQuery()
            )
            ->columns([
                Tables\Columns\TextColumn::make('customer_id')->label('Customer ID'),
                Tables\Columns\TextColumn::make('day')->label('Day'),
                Tables\Columns\TextColumn::make('hour')->label('Hour'),
                Tables\Columns\TextColumn::make('id')->label('Transaction ID'),
                Tables\Columns\TextColumn::make('month')->label('Month'),
                Tables\Columns\TextColumn::make('quantity')->label('Quantity'),
                Tables\Columns\TextColumn::make('total_price')->label('Total Price'),
                Tables\Columns\TextColumn::make('unit_price')->label('Unit Price'),
                Tables\Columns\TextColumn::make('year')->label('Year'),
            ]);
    }

    protected function getDataQuery(): Collection
    {
        return collect($this->data);
    }
}
