def fractional_knapsack(capacity, parcels):
    """
    Calculates the maximum profit using the Fractional Knapsack strategy.

    Args:
        capacity (int): The maximum weight capacity of the truck.
        parcels (list of tuples): A list where each tuple represents a parcel
                                   in the format (weight, profit).

    Returns:
        float: The maximum profit achievable.
    """

    # Calculate profit-to-weight ratio for each parcel and store as (ratio, weight, profit)
    # Sort parcels in descending order of profit-to-weight ratio
    sorted_parcels = sorted(
        [(p[1] / p[0], p[0], p[1]) for p in parcels],
        key=lambda x: x[0],
        reverse=True
    )

    total_profit = 0.0
    remaining_capacity = capacity

    for ratio, weight, profit in sorted_parcels:
        if remaining_capacity <= 0:
            break

        if weight <= remaining_capacity:
            # Take the whole parcel
            total_profit += profit
            remaining_capacity -= weight
        else:
            # Take a fraction of the parcel
            fraction = remaining_capacity / weight
            total_profit += profit * fraction
            remaining_capacity = 0  # Knapsack is now full

    return total_profit

# Example Usage:
if __name__ == "__main__":
    truck_capacity = 50
    # Parcels: (weight, profit)
    available_parcels = [(10, 60), (20, 100), (30, 120)]

    max_profit = fractional_knapsack(truck_capacity, available_parcels)
    print(f"Maximum profit achievable: {max_profit:.2f}")

    truck_capacity_2 = 15
    available_parcels_2 = [(5, 10), (10, 20), (15, 30)]
    max_profit_2 = fractional_knapsack(truck_capacity_2, available_parcels_2)
    print(f"Maximum profit achievable (example 2): {max_profit_2:.2f}")

