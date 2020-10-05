def molemass(sequence):
    symbols = ["H", "C", "N", "O", "P", "S", "K", "F"]
    masses = [1.00784, 12.0107, 14.0067, 15.999, 30.973762, 32.065 , 39.0983, 18.998403]
    atoms_dict = dict(zip(symbols, masses))
    total_mass = 0
    for i in range(len(sequence)):
        total_mass += atoms_dict[sequence[i]]
    return total_mass