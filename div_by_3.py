def max_sum_div_by_3(arr):
    some_mass = [0, 0, 0]

    for number in arr:
        for i in list(some_mass):
            new_sum = i + number
            remainder = new_sum % 3
            some_mass[remainder] = max(some_mass[remainder], new_sum)

    return some_mass[0]

def solution():
    arr = list(map(int, input().split()))
    result = max_sum_div_by_3(arr)
    print(result)

solution()