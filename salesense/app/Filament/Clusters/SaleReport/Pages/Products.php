<?php

namespace App\Filament\Clusters\SaleReport\Pages;

use App\Filament\Clusters\SaleReport;
use Filament\Pages\Page;
use Filament\Pages\SubNavigationPosition;


class Products extends Page
{
    protected static SubNavigationPosition $subNavigationPosition = SubNavigationPosition::Top;
    protected static ?int $navigationSort = 2;
    protected static ?string $title = 'Product Sales';
    protected static ?string $navigationIcon = 'heroicon-o-shopping-bag';
    protected static string $view = 'filament.clusters.sale-report.pages.products';
    protected static ?string $cluster = SaleReport::class;
}
