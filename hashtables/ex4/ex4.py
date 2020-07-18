def has_negatives(a):
    integers = {}
    result = []

    for num in a:
        if num > 0:
            negative = num * -1
            if integers.get(negative) is True:
                result.append(num)
        else:
            positive = num * -1
            if integers.get(positive) is True:
                result.append(positive)

        integers[num] = True

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
