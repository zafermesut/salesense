<x-filament::page>
    <div class="space-y-4">
        <x-filament::tabs>
            <!-- Products Tab -->
            <x-filament::tabs.item :href="route('sales-reports.products')" :active="$activeTab === 'products'" wire:click="$set('activeTab', 'products')">
                Products
            </x-filament::tabs.item>

            <!-- Countries Tab -->
            <x-filament::tabs.item :href="route('sales-reports.countries')" :active="$activeTab === 'countries'" wire:click="$set('activeTab', 'countries')">
                Countries
            </x-filament::tabs.item>

            <!-- Sales Tab -->
            <x-filament::tabs.item :href="route('sales-reports.sales')" :active="$activeTab === 'sales'" wire:click="$set('activeTab', 'sales')">
                Sales
            </x-filament::tabs.item>
        </x-filament::tabs>

        <div class="mt-6">
            <!-- Top Products Chart -->
            @if ($activeTab === 'products')
                <div id="top-products-chart">
                    <h2 class="text-xl font-semibold">Products</h2>
                </div>
            @endif

            <!-- Top Countries Chart -->
            @if ($activeTab === 'countries')
                <div id="top-countries-chart">
                    <h2 class="text-xl font-semibold">Countries</h2>
                </div>
            @endif

            <!-- Sales by Date Chart -->
            @if ($activeTab === 'sales')
                <div id="sales-by-date-chart">
                    <h2 class="text-xl font-semibold">Sales</h2>
                </div>
            @endif
        </div>
    </div>
</x-filament::page>
