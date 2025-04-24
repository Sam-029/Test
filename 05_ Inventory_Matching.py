'''
Sorts products by price (cheapest first) to maximize affordable quantity.
Tries to fulfill the order quantity using available items within the budget.
Tracks how many items are taken from each product and at what cost.
Check order requirements:

'''
def check_order_fulfillment(inventory, order_quantity, budget):
    # Sort inventory by price (lowest first)
    sorted_inventory = sorted(inventory, key=lambda x: x['price'])

    total_cost = 0
    total_items_taken = 0
    items_fulfilled = []

    for item in sorted_inventory:
        if total_items_taken >= order_quantity:
            break

        available = item['quantity']
        needed = order_quantity - total_items_taken
        can_take = min(available, needed)

        cost = can_take * item['price']

        # If we can take all from this item within budget
        if total_cost + cost <= budget:
            total_cost += cost
            total_items_taken += can_take
            items_fulfilled.append({
                'product': item['name'],
                'quantity': can_take,
                'cost': cost
            })
        else:
            # Take only what's affordable
            remaining_budget = budget - total_cost
            max_possible = int(remaining_budget // item['price'])

            if max_possible > 0:
                cost = max_possible * item['price']
                total_cost += cost
                total_items_taken += max_possible
                items_fulfilled.append({
                    'product': item['name'],
                    'quantity': max_possible,
                    'cost': cost
                })
            break  # budget exhausted

    # Determine fulfillment status
    if total_items_taken == order_quantity:
        status = "Fulfillable"
    elif total_items_taken > 0:
        status = "Partially Fulfillable"
    else:
        status = "Not Fulfillable (Impossible)"

    return {
        'status': status,
        'items': items_fulfilled,
        'total_cost': total_cost
    }

inventory = [
    {'name': 'Product A', 'quantity': 5, 'price': 10},
    {'name': 'Product B', 'quantity': 3, 'price': 5},
    {'name': 'Product C', 'quantity': 10, 'price': 2}
]

order_quantity = 4
budget = 1 

result = check_order_fulfillment(inventory, order_quantity, budget)

print("Order Status:", result['status'])
if result['status'] != "Not Fulfillable (Impossible)":
    print("Items Fulfilled:")
    for item in result['items']:
        print(f"  {item['product']}: {item['quantity']} pcs for ${item['cost']}")
    print("Total Cost:", result['total_cost'])
