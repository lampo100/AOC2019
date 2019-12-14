from math import trunc

def count_fuel(mass: int) -> int:
    fuel = trunc(mass / 3) - 2
    return 0 if fuel < 0 else fuel

def count_absolute_fuel(mass: int) -> int:
    if mass <= 0:
        return 0
    else:
        return count_fuel(mass) + count_absolute_fuel(count_fuel(mass))

if __name__ == '__main__':
    sum = 0
    with open("./input") as file:
        for line in file:
            sum += count_absolute_fuel(int(line))
    print(sum)
