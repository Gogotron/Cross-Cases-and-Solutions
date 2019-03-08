def generate_moves_dict(affected_positions, offset):
    moves_dict = {i: i for i in "abcdefghijklmnopqrtsuvwx"}
    for cycle in affected_positions:
        for i in cycle:
            moves_dict[i] = cycle[(cycle.index(i) + offset) % len(cycle)]
    return moves_dict


F, Fp, F2 = [generate_moves_dict(['efgh', 'clur'], i) for i in [1, -1, 2]]
U, Up, U2 = [generate_moves_dict(['abcd', 'eqmi'], i) for i in [1, -1, 2]]
R, Rp, R2 = [generate_moves_dict(['ijkl', 'bpvf'], i) for i in [1, -1, 2]]
L, Lp, L2 = [generate_moves_dict(['qrst', 'dhxn'], i) for i in [1, -1, 2]]
D, Dp, D2 = [generate_moves_dict(['uvwx', 'gkos'], i) for i in [1, -1, 2]]
B, Bp, B2 = [generate_moves_dict(['mnop', 'atwj'], i) for i in [1, -1, 2]]

x, xp, x2 = [generate_moves_dict(['ijkl', 'qtsr', 'bpvf', 'nxhd', 'aoue', 'cmwg'], i) for i in (1, -1, 2)]
y, yp, y2 = [generate_moves_dict(['abcd', 'uxwv', 'eqmi', 'gsok', 'frnj', 'htpl'], i) for i in (1, -1, 2)]
z, zp, z2 = [generate_moves_dict(['efgh', 'mpon', 'clur', 'ajwt', 'bkxq', 'divs'], i) for i in (1, -1, 2)]

moveDicts = {"F": F, "F'": Fp, "F2": F2, "B": B, "B'": Bp, "B2": B2, "U": U, "U'": Up, "U2": U2, "D": D, "D'": Dp,
             "D2": D2, "R": R, "R'": Rp, "R2": R2, "L": L, "L'": Lp, "L2": L2}


def apply_move_dict(move_transformation_dict, piece_positions):
    new_piece_positions = ""
    for piece_position in piece_positions:
        new_piece_positions += move_transformation_dict[piece_position]
    return new_piece_positions


def apply_moves(moves, piece_positions="abcd"):
    new_piece_positions = piece_positions
    for move in moves:
        new_piece_positions = apply_move_dict(moveDicts[move], new_piece_positions)
    return new_piece_positions
