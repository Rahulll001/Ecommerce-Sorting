
def merge_sort(products):
    if len(products) <= 1:
        return products

    mid = len(products) // 2
    left = merge_sort(products[:mid])
    right = merge_sort(products[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


prices = [500, 200, 800, 100, 400]

print("Original Prices:", prices)
print("Sorted Prices:", merge_sort(prices))
