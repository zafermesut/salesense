<?php

namespace App\Filament\Clusters\SaleReport\Pages;

use App\Filament\Clusters\SaleReport;
use App\Filament\Widgets\Deneme;
use App\Filament\Widgets\SalesDescribe;
use Filament\Pages\Page;
use Filament\Pages\SubNavigationPosition;
use Http;


class Sales extends Page
{
    protected static SubNavigationPosition $subNavigationPosition = SubNavigationPosition::Top;
    protected static ?int $navigationSort = 1;
    protected static ?string $title = 'Sales Overview';
    protected static ?string $navigationIcon = 'heroicon-o-chart-pie';
    protected static string $view = 'filament.clusters.sale-report.pages.sales';
    protected static ?string $cluster = SaleReport::class;


    public array $data = []; // Dynamic data for the active tab

    protected function getHeaderWidgets(): array
    {
        return [
            Deneme::class
        ];
    }

}
