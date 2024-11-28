<?php

namespace App\Filament\Clusters\SaleReport\Pages;

use App\Filament\Clusters\SaleReport;
use Filament\Pages\Page;
use Filament\Pages\SubNavigationPosition;


class TimeSeries extends Page
{
    protected static SubNavigationPosition $subNavigationPosition = SubNavigationPosition::Top;
    protected static ?int $navigationSort = 4;
    protected static ?string $title = 'Sales Trends';
    protected static ?string $navigationIcon = 'heroicon-o-clock';
    protected static string $view = 'filament.clusters.sale-report.pages.time-series';
    protected static ?string $cluster = SaleReport::class;
}
