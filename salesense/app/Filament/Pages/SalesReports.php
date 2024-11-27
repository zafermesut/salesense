<?php

namespace App\Filament\Pages;

use Filament\Pages\Page;
use Illuminate\Support\Facades\Http;

class SalesReports extends Page
{
    protected static ?string $navigationIcon = 'heroicon-o-chart-bar';
    protected static string $view = 'filament.pages.sales-reports';

    public string $activeTab = 'products';

    // Method to fetch analytics data from Python API based on the report type
    public function getAnalyticsData(string $type)
    {
        $response = Http::post('http://127.0.0.1:5001/analytics', [
            'type' => $type,
        ]);

        if ($response->successful()) {
            return $response->json('data');
        }

        return [];
    }

    // Method to get the top products report
    public function getTopProducts()
    {
        return $this->getAnalyticsData('top_products');
    }

    // Method to get the top countries report
    public function getTopCountries()
    {
        return $this->getAnalyticsData('top_countries');
    }


    public function getSalesByDate()
    {
        return $this->getAnalyticsData('sales_by_date');
    }
}
