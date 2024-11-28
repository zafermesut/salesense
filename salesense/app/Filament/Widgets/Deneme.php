<?php

namespace App\Filament\Widgets;

use Filament\Widgets\Widget;
use Illuminate\Support\Facades\Http;

class Deneme extends Widget
{
    protected static string $view = 'filament.widgets.deneme';

    protected int|string|array $columnSpan = 'full';


    public array $data = [];

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
            // dd($this->data);
        } else {
            $this->data = []; // Hata durumunda boş bir dizi
        }
    }
}
