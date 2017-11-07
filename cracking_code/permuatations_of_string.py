def insert(letter, string, index):
    return string[:index] + letter + string[index:]

def make_combos(letter, combos):
    next_combos = []
    for combo in combos:
        print combo
        for i in range(len(combo) + 1):
            next_combos.append(insert(letter, combo, i))
    return next_combos

def permuatations_of_string(string):
    combinations = [string[0]]
    for i in range(1, len(string)):
        combinations = make_combos(string[i], combinations)
    print len(combinations)
    print combinations

permuatations_of_string('abcd')