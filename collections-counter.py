from collections import Counter

def calulate_order_total(num_shoes, shoe_sizes, orders):
    total = 0
    items = Counter(shoe_sizes).items()
    inventory = {}
    for item in items:
        inventory[item[0]] = item[1]

    for order in orders:
        size = order[0]
        price = order[1]

        if size in inventory.keys():
            if price and inventory[size] != 0:
                total += price
                inventory[size] -= 1

    return total


if __name__ == "__main__":

    num_shoes = int(input())
    shoe_sizes = list(map(int, input().split()))
    num_customers = int(input())
    orders = []
    for n in range(num_customers):
        order = list(map(int, input().split()))
        orders.append(order)

    total = calulate_order_total(num_shoes, shoe_sizes, orders)
    print(total)
