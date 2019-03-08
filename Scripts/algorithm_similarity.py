def generate_moves_dict(affected_moves, offset):
    moves_dict = {
        i: i for i in
        ["F", "F'", "F2", "B", "B'", "B2", "R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2", "D", "D'", "D2"]
    }
    for cycle in affected_moves:
        for i in cycle:
            moves_dict[i] = cycle[(cycle.index(i) + offset) % len(cycle)]
    return moves_dict


rotatedMovesByX, rotatedMovesByXp, rotatedMovesByX2 = [
    generate_moves_dict([["F", "D", "B", "U"], ["F'", "D'", "B'", "U'"], ["F2", "D2", "B2", "U2"]], i)
    for i in [1, -1, 2]
]
rotatedMovesByY, rotatedMovesByYp, rotatedMovesByY2 = [
    generate_moves_dict([["F", "R", "B", "L"], ["F'", "R'", "B'", "L'"], ["F2", "R2", "B2", "L2"]], i)
    for i in [1, -1, 2]
]
rotatedMovesByZ, rotatedMovesByZp, rotatedMovesByZ2 = [
    generate_moves_dict([["U", "L", "B", "R"], ["U'", "L'", "B'", "R'"], ["U2", "L2", "B2", "R2"]], i)
    for i in [1, -1, 2]
]

mirroredMoves = generate_moves_dict(
    [["F", "F'"], ["U", "U'"], ["B", "B'"], ["D", "D'"], ["R", "L'"], ["R'", "L"], ["R2", "L2"]], 1)
reversedMoves = generate_moves_dict([["F", "F'"], ["U", "U'"], ["B", "B'"], ["D", "D'"], ["R", "R'"], ["L", "L'"]], 1)


#


def transform_algorithm(algorithm, transformation):
    transformed_algorithm = []
    for move in algorithm:
        transformed_algorithm.append(transformation[move])
    return transformed_algorithm


def x_rotate_algorithm(alg): return transform_algorithm(alg, rotatedMovesByX)


def xp_rotate_algorithm(alg): return transform_algorithm(alg, rotatedMovesByXp)


def x2_rotate_algorithm(alg): return transform_algorithm(alg, rotatedMovesByX2)


def y_rotate_algorithm(alg): return transform_algorithm(alg, rotatedMovesByY)


def yp_rotate_algorithm(alg): return transform_algorithm(alg, rotatedMovesByYp)


def y2_rotate_algorithm(alg): return transform_algorithm(alg, rotatedMovesByY2)


def z_rotate_algorithm(alg): return transform_algorithm(alg, rotatedMovesByZ)


def zp_rotate_algorithm(alg): return transform_algorithm(alg, rotatedMovesByZp)


def z2_rotate_algorithm(alg): return transform_algorithm(alg, rotatedMovesByZ2)


def mirror_algorithm(alg): return transform_algorithm(alg, mirroredMoves)


def reverse_algorithm(alg): return list(reversed(transform_algorithm(alg, reversedMoves)))


#


def are_similar_algorithms(alg1, alg2):
    if len(alg1) != len(alg2):
        return False

    temp_alg = alg2
    if alg1 == temp_alg:
        return True  # These ae exactly the same, what are you doing?!?!?
    temp_alg = y_rotate_algorithm(temp_alg)
    if alg1 == temp_alg:
        return True
    temp_alg = y_rotate_algorithm(temp_alg)
    if alg1 == temp_alg:
        return True
    temp_alg = y_rotate_algorithm(temp_alg)
    if alg1 == temp_alg:
        return True

    temp_alg = mirror_algorithm(alg2)
    if alg1 == temp_alg:
        return True
    temp_alg = y_rotate_algorithm(temp_alg)
    if alg1 == temp_alg:
        return True
    temp_alg = y_rotate_algorithm(temp_alg)
    if alg1 == temp_alg:
        return True
    temp_alg = y_rotate_algorithm(temp_alg)
    if alg1 == temp_alg:
        return True

    return False


def similar_algorithms(alg):
    list_of_similar_algs = []

    temp_alg = alg
    list_of_similar_algs.append(temp_alg)
    temp_alg = y_rotate_algorithm(temp_alg)
    list_of_similar_algs.append(temp_alg)
    temp_alg = y_rotate_algorithm(temp_alg)
    list_of_similar_algs.append(temp_alg)
    temp_alg = y_rotate_algorithm(temp_alg)
    list_of_similar_algs.append(temp_alg)

    temp_alg = y_rotate_algorithm(alg)
    list_of_similar_algs.append(temp_alg)
    temp_alg = y_rotate_algorithm(temp_alg)
    list_of_similar_algs.append(temp_alg)
    temp_alg = y_rotate_algorithm(temp_alg)
    list_of_similar_algs.append(temp_alg)
    temp_alg = y_rotate_algorithm(temp_alg)
    list_of_similar_algs.append(temp_alg)

    return list_of_similar_algs


def similar_algorithm_is_already_in_list(alg, list_of_used_algs):
    for similarAlg in similar_algorithms(alg):
        if similarAlg in list_of_used_algs:
            return True
    return False
