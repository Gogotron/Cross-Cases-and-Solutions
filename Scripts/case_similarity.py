from cube_scrambling import y as rotated_cases

mirrored_cases = {
    'a': 'a',
    'b': 'd',
    'c': 'c',
    'd': 'b',
    'e': 'e',
    'f': 'h',
    'g': 'g',
    'h': 'f',
    'i': 'q',
    'j': 't',
    'k': 's',
    'l': 'r',
    'm': 'm',
    'n': 'p',
    'o': 'o',
    'p': 'n',
    'q': 'i',
    'r': 'l',
    's': 'k',
    't': 'j',
    'u': 'u',
    'v': 'x',
    'w': 'w',
    'x': 'v'
}
flipped_cases = {
    'a': 'm',
    'b': 'i',
    'c': 'e',
    'd': 'q',
    'e': 'c',
    'f': 'l',
    'g': 'u',
    'h': 'r',
    'i': 'b',
    'j': 'p',
    'k': 'v',
    'l': 'f',
    'm': 'a',
    'n': 't',
    'o': 'w',
    'p': 'j',
    'q': 'd',
    'r': 'h',
    's': 'x',
    't': 'n',
    'u': 'g',
    'v': 'k',
    'w': 'o',
    'x': 's'
}


def rotate_case(case):
    rotated_case = ""
    for pos in case:
        rotated_case += rotated_cases[pos]
    rotated_case = rotated_case[-1] + rotated_case[:-1]
    return rotated_case


def mirror_case(case):
    mirrored_case = ""
    for pos in case:
        mirrored_case += mirrored_cases[pos]
    mirrored_case = list(mirrored_case)
    mirrored_case[1], mirrored_case[3] = mirrored_case[3], mirrored_case[1]
    mirrored_case = "".join(mirrored_case)
    return mirrored_case


#


def are_similar_cases(case_a, case_b):
    temp_case = case_b
    if case_a == temp_case:
        return True  # These are exactly the same, what are you doing?!?!?
    temp_case = rotate_case(temp_case)
    if case_a == temp_case:
        return True
    temp_case = rotate_case(temp_case)
    if case_a == temp_case:
        return True
    temp_case = rotate_case(temp_case)
    if case_a == temp_case:
        return True

    temp_case = mirror_case(case_b)
    if case_a == temp_case:
        return True
    temp_case = rotate_case(temp_case)
    if case_a == temp_case:
        return True
    temp_case = rotate_case(temp_case)
    if case_a == temp_case:
        return True
    temp_case = rotate_case(temp_case)
    if case_a == temp_case:
        return True

    return False


def similar_cases(case):
    list_of_similar_cases = []

    temp_case = case
    list_of_similar_cases.append(temp_case)
    temp_case = rotate_case(temp_case)
    list_of_similar_cases.append(temp_case)
    temp_case = rotate_case(temp_case)
    list_of_similar_cases.append(temp_case)
    temp_case = rotate_case(temp_case)
    list_of_similar_cases.append(temp_case)

    temp_case = mirror_case(case)
    list_of_similar_cases.append(temp_case)
    temp_case = rotate_case(temp_case)
    list_of_similar_cases.append(temp_case)
    temp_case = rotate_case(temp_case)
    list_of_similar_cases.append(temp_case)
    temp_case = rotate_case(temp_case)
    list_of_similar_cases.append(temp_case)

    return list(set(list_of_similar_cases))


def similar_case_is_already_in_list(case, list_of_used_cases):
    for similar_case in similar_cases(case):
        if similar_case in list_of_used_cases:
            return True
    return False


def case_difference(case_a, case_b):  # This is to find how to go from one case to another.
    temp_case = case_b
    if case_a == temp_case:
        return 0
    temp_case = rotate_case(temp_case)
    if case_a == temp_case:
        return 1
    temp_case = rotate_case(temp_case)
    if case_a == temp_case:
        return 2
    temp_case = rotate_case(temp_case)
    if case_a == temp_case:
        return 3

    temp_case = mirror_case(case_b)
    if case_a == temp_case:
        return 4
    temp_case = rotate_case(temp_case)
    if case_a == temp_case:
        return 5
    temp_case = rotate_case(temp_case)
    if case_a == temp_case:
        return 6
    temp_case = rotate_case(temp_case)
    if case_a == temp_case:
        return 7

    return -1  # This should never have to be used.
