def merge_sort_orders(orders):
    """
    Sorts a list of online orders by estimated delivery time using Merge Sort.

    Args:
        orders (list): A list of dictionaries, where each dictionary represents
                       an order and has a key 'delivery_time' (int).

    Returns:
        list: The sorted list of orders.
    """
    if len(orders) <= 1:
        return orders

    mid = len(orders) // 2
    left_half = orders[:mid]
    right_half = orders[mid:]

    left_half = merge_sort_orders(left_half)
    right_half = merge_sort_orders(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    """
    Merges two sorted lists of orders into a single sorted list.

    Args:
        left (list): The left sorted list of orders.
        right (list): The right sorted list of orders.

    Returns:
        list: The merged and sorted list of orders.
    """
    merged_orders = []
    i = 0  # Pointer for the left list
    j = 0  # Pointer for the right list

    while i < len(left) and j < len(right):
        if left[i]['delivery_time'] < right[j]['delivery_time']:
            merged_orders.append(left[i])
            i += 1
        else:
            merged_orders.append(right[j])
            j += 1

    # Append any remaining elements from either list
    while i < len(left):
        merged_orders.append(left[i])
        i += 1
    while j < len(right):
        merged_orders.append(right[j])
        j += 1

    return merged_orders

if __name__ == "__main__":
    # Example usage:
    online_orders = [
        {'order_id': 'A101', 'item': 'Pizza', 'delivery_time': 30},
        {'order_id': 'B202', 'item': 'Burger', 'delivery_time': 15},
        {'order_id': 'C303', 'item': 'Salad', 'delivery_time': 45},
        {'order_id': 'D404', 'item': 'Pasta', 'delivery_time': 20},
        {'order_id': 'E505', 'item': 'Sushi', 'delivery_time': 60},
        {'order_id': 'F606', 'item': 'Tacos', 'delivery_time': 25},
    ]

    print("Original Orders:")
    for order in online_orders:
        print(order)

    sorted_orders = merge_sort_orders(online_orders)

    print("\nSorted Orders by Delivery Time:")
    for order in sorted_orders:
        print(order)
