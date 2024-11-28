<?php

namespace App\Filament\Clusters\SaleReport\Pages;

use App\Filament\Clusters\SaleReport;
use Filament\Pages\Page;
use Filament\Pages\SubNavigationPosition;


class Customers extends Page
{
    protected static SubNavigationPosition $subNavigationPosition = SubNavigationPosition::Top;
    protected static ?int $navigationSort = 4;
    protected static ?string $title = 'Customer Insights';
    protected static ?string $navigationIcon = 'heroicon-o-users';
    protected static string $view = 'filament.clusters.sale-report.pages.customers';
    protected static ?string $cluster = SaleReport::class;
}
