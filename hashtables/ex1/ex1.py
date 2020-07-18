def get_indices_of_item_weights(weights, length, limit):
    items = {}

    for item in range(0, length):
        weight = weights[item]
        needed = limit - weight
        if needed in items:
            item_pair = (item, items[needed])
            return sorted(item_pair, reverse=True)
        else:
            items[weight] = item

    return None