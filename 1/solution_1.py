from math import trunc

def count_fuel(module_mass: str) -> int:
    return trunc(int(module_mass) / 3) - 2

if __name__ == '__main__':
    sum = 0
    with open("./input") as file:
        for line in file:
            sum += count_fuel(line)
    print(sum)
