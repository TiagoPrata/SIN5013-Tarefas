def char_parser(char):
    if char == ">":
        return [0,1]
    elif char == "<":
        return [0,-1]
    elif char == "^":
        return [-1,0]
    elif char == "v":
        return [1,0]
    elif char == "x":
        return [0,0]
    else:
        return [9,9]

def invert_char(char):
    if char == ">":
        return "<"
    elif char == "<":
        return ">"
    elif char == "^":
        return "v"
    elif char == "v":
        return "^"
    elif char == "x":
        return "x"
    else:
        return "o"

def test_path_begging_in_the_borders(path,M,N):
    path_found = False
    for j in range(0,M):
        for i in range(0,N):
            if (i==0) or (j==0) or (i==N-1) or (j==M-1):            # If player starts in a border
                path_found = init_test_path(path, i, j)
                if path_found:
                    break
        if path_found:
            # print("Sim")
            break
    return path_found

def apply_path_inversion(path, inversion_sequence):
    new_path = [row[:] for row in path]
    for i in range(0, len(inversion_sequence)):
        if inversion_sequence[i] == 1:
            lin = int(i / len(path[0][:]))
            col = int(i % len(path[0][:]))
            new_path[lin][col] = invert_char(path[lin][col])
    
    return new_path

def path_inversions(path,seq,qty_of_ones,i, M, N, lim_of_inversions):
    number_of_possible_values = 2           # True or False

    if i==len(seq):
        # print(seq)
        new_path = apply_path_inversion(path, seq)
        path_found = test_path_begging_in_the_borders(new_path,M,N)
        return path_found
    for a in range (0,number_of_possible_values):
        if a==1:
            qty_of_ones += 1

        if qty_of_ones > lim_of_inversions:
            return False

        seq[i] = a
        path_found = path_inversions(path,seq,qty_of_ones,i+1,M,N,lim_of_inversions)
        if path_found:
            return True

def test_path(path, player_pos, visited_cells):
    if (player_pos[0] >= len(path[:])) or (player_pos[1] >= len(path[0][:]) or (player_pos[0] < 0) or (player_pos[1] < 0)):          # If player is out-of-bound
        return False
    elif path[player_pos[0]][player_pos[1]] == "x":                                 # If target found
        return True
    else:
        visited_cells[player_pos[0]][player_pos[1]] += 1;

        if visited_cells[player_pos[0]][player_pos[1]] > 1:                         # If returned to a visited spot (looping)
            return False
        else:
            next_move = char_parser( path[player_pos[0]][player_pos[1]] )
            player_pos[0] = player_pos[0] + next_move[0]
            player_pos[1] = player_pos[1] + next_move[1]
            return test_path(path, player_pos, visited_cells)


def init_test_path(path, start_line, start_col):
    visited_cells = [[0 for x in range(len(path[0][:]))] for y in range(len(path[:]))]
    player_pos = [start_line, start_col]

    return test_path(path, player_pos, visited_cells)


if __name__=="__main__":
    while(True):
        user_entry = input()
        if user_entry == "0":
            break

        N, M, K = list(map(int, user_entry.split()))

        path = [[0 for x in range(M)] for y in range(N)]

        for i in range(0,N):
            path_row = input()
            for j in range(0, len(path_row)):
                path[i][j] = path_row[j]


        seq = [0 for x in range(M*N)]
        path_found = path_inversions(path,seq, 0, 0, M, N, K)

        if path_found:
            print("Sim")
        else:
            print('Nao')