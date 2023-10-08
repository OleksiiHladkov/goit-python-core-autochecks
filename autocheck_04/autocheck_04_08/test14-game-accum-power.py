def game(terra: list, power: int) -> int:
    accum_energy = power

    for energy_list in terra:
        for energy in energy_list:
            if energy <= accum_energy:
                accum_energy += energy
            else:
                break

    return accum_energy


if __name__ == '__main__':
    terra = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
    power = 1
    print(game(terra, power))
