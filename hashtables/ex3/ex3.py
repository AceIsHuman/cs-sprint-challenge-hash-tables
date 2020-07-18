def intersection(arrays):
    initial_list = {}
    intersections = {}

    for i in range(len(arrays)):
        for num in arrays[i]:
            if i == 0:
                initial_list[num] = True
            elif initial_list.get(num) is True:
                intersections[num] = True

        if i != 0:
            initial_list = intersections.copy()

    result = list(intersections)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
