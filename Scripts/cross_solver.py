import os
from ast import literal_eval as lit_eval

from case_similarity import similar_cases, case_difference, mirror_case, rotate_case
from cube_scrambling import apply_moves as apply_scramble, apply_move_dict as apply_move, x, xp, x2, y, yp, y2, z, zp, z2
from algorithm_similarity import (
    mirror_algorithm as mirror_alg, reverse_algorithm as reverse_alg,

    x_rotate_algorithm as x_rot_alg, xp_rotate_algorithm as xp_rot_alg, x2_rotate_algorithm as x2_rot_alg,
    y_rotate_algorithm as y_rot_alg, yp_rotate_algorithm as yp_rot_alg, y2_rotate_algorithm as y2_rot_alg,
    z_rotate_algorithm as z_rot_alg, zp_rotate_algorithm as zp_rot_alg, z2_rotate_algorithm as z2_rot_alg
)


solutions_save_location = r"..\Files\Solution Files" + "\\"
cross_cases_location = r"..\Files" + "\\"


with open(cross_cases_location + "cross_cases.txt", 'r') as casesFile:
    cross_cases_used = [line.strip("\n") for line in casesFile]


def find_similar_cross_case_used(case):
    cross_cases_used_as_files_names = list(filter(lambda i: i in cross_cases_used, similar_cases(case)))
    if len(cross_cases_used_as_files_names) == 1:
        return cross_cases_used_as_files_names[0]
    else:
        # This shouldn't be possible.
        print("Multiple or no possible files found.")


def solution_retriever(case):
    cross_case_used = find_similar_cross_case_used(case)
    solutions_file_name = "case_" + cross_case_used
    solutions_file = open(solutions_save_location + solutions_file_name + ".txt", 'r')

    lines = solutions_file.readlines()
    scrambles = list(map(lambda line: lit_eval(line.strip("\n")), lines[:-1]))  # The last line isn't a solution.
    if len(scrambles) > 0:
        raw_solutions = list(map(reverse_alg, scrambles))
        transformation = case_difference(cross_case_used, case)  # How to convert the solutions for the general case to the requested case.
        for i in range(transformation % 4):
            raw_solutions = list(map(y_rot_alg, raw_solutions))
        if transformation >= 4:
            raw_solutions = list(map(mirror_alg, raw_solutions))
        solutions = raw_solutions
        return solutions
    else:
        print("No solutions found.")
        return []


def get_cross_solutions(scramble, mode="wyborg"):
    scrambled_cube = apply_scramble(scramble, "abcdefghijklmnopqrstuvwx")  # Call it a cube but it's just edge stickers.
    solutions = []
    if 'w' in mode:
        white_case = scrambled_cube[:4]
        relative_solutions = solution_retriever(white_case)
        white_solutions = relative_solutions
        solutions = reduce_solutions(solutions, white_solutions)
    if 'g' in mode:
        green_case = apply_move(x, scrambled_cube[4:8])
        relative_solutions = solution_retriever(green_case)
        green_solutions = list(map(x_rot_alg, relative_solutions))
        solutions = reduce_solutions(solutions, green_solutions)
    if 'r' in mode:
        red_case = apply_move(x, apply_move(y, scrambled_cube[8:12]))
        relative_solutions = solution_retriever(red_case)
        red_solutions = list(map(y_rot_alg, list(map(x_rot_alg, relative_solutions))))
        solutions = reduce_solutions(solutions, red_solutions)
    if 'b' in mode:
        blue_case = apply_move(x, apply_move(y2, scrambled_cube[12:16]))
        relative_solutions = solution_retriever(blue_case)
        blue_solutions = list(map(y2_rot_alg, list(map(x_rot_alg, relative_solutions))))
        solutions = reduce_solutions(solutions, blue_solutions)
    if 'o' in mode:
        orange_case = apply_move(x, apply_move(yp, scrambled_cube[16:20]))
        relative_solutions = solution_retriever(orange_case)
        orange_solutions = list(map(yp_rot_alg, list(map(x_rot_alg, relative_solutions))))
        solutions = reduce_solutions(solutions, orange_solutions)
    if 'y' in mode:
        yellow_case = apply_move(x2, scrambled_cube[20:24])
        relative_solutions = solution_retriever(yellow_case)
        yellow_solutions = list(map(x2_rot_alg, relative_solutions))
        solutions = reduce_solutions(solutions, yellow_solutions)
    return solutions


def reduce_solutions(solutions_a, solutions_b):
    if len(solutions_a) == 0 or len(solutions_b) == 0:
        return solutions_a + solutions_b
    if len(solutions_a[0]) == len(solutions_b[0]):
        return remove_dupes_in_list_of_lists(solutions_a + solutions_b)
    if len(solutions_a[0]) < len(solutions_b[0]):
        return solutions_a
    if len(solutions_b[0]) < len(solutions_a[0]):
        return solutions_b


def remove_dupes_in_list_of_lists(list_of_lists):
    return [list(tupl) for tupl in {tuple(i) for i in list_of_lists}]


if __name__ == "__main__":
    while True:
        scramble = input("Scramble: ").split(" ")
        solutions = get_cross_solutions(scramble)
        solution_strings = list(map(lambda solution: " ".join(solution), solutions))
        print("\n".join(solution_strings))
        print()
