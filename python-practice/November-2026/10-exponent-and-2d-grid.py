# Topic: Exponential Function Using range() and 2D Lists

# 1. Exponential Function
def raise_to_power(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result = result * base_num
    return result  # Kept outside the loop so all iterations complete

print(raise_to_power(2, 3))


# 2. 2D List (Grid)
number_grid = [
    [10, 15, 25],
    [35, 45, 55],
    [65, 75, 85],
    [95, 100]
]

for row in number_grid:
    for col in row:
        print(col)

print(f"{number_grid[2][0]} is the 0th column from the 2nd row")