<x-filament-widgets::widget>
    <x-filament::section>
        <div>
            <table class="table-auto w-full rounded-lg border-collapse border border-gray-300 ">
                <thead>
                    <tr>
                        <th></th>
                        <th class="border px-4 py-2">Count</th>
                        <th class="border px-4 py-2">Mean</th>
                        <th class="border px-4 py-2">Minimum</th>
                        <th class="border px-4 py-2">%25</th>
                        <th class="border px-4 py-2">%50</th>
                        <th class="border px-4 py-2">%75</th>
                        <th class="border px-4 py-2">Maximum</th>
                        <th class="border px-4 py-2">Std.</th>
                    </tr>
                </thead>
                <tbody>
                    @foreach ($data as $item)
                        <tr>
                            <td class="border px-4 py-2">Quantity</td>
                            @foreach ($item as $value)
                                <td class="border px-4 py-2">{{ $value['quantity'] }}</td>
                            @endforeach
                        </tr>
                        <tr>
                            <td class="border px-4 py-2">Unit Price</td>
                            @foreach ($item as $value)
                                <td class="border px-4 py-2">{{ $value['unit_price'] }}</td>
                            @endforeach
                        </tr>
                        <tr>
                            <td class="border px-4 py-2">Total Price</td>
                            @foreach ($item as $value)
                                <td class="border px-4 py-2">{{ $value['total_price'] }}</td>
                            @endforeach
                        </tr>
                    @endforeach
                </tbody>
            </table>
        </div>
    </x-filament::section>
</x-filament-widgets::widget>
