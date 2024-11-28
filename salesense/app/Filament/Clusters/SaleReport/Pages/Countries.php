<?php

namespace App\Filament\Clusters\SaleReport\Pages;

use App\Filament\Clusters\SaleReport;
use Filament\Pages\Page;
use Filament\Pages\SubNavigationPosition;


class Countries extends Page
{
    protected static SubNavigationPosition $subNavigationPosition = SubNavigationPosition::Top;
    protected static ?int $navigationSort = 3;
    protected static ?string $title = 'Geographical Sales';
    protected static ?string $navigationIcon = 'heroicon-o-globe-alt';
    protected static string $view = 'filament.clusters.sale-report.pages.countries';
    protected static ?string $cluster = SaleReport::class;
}
