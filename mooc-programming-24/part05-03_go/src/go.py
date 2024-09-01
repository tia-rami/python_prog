# Write your solution here
def who_won(game_board: list):
    count_player_one = 0
    count_player_two = 0

    for row in game_board:
        for element in row:
            if element == 1:
                count_player_one += 1
            elif element == 2:
                count_player_two += 1
     
    if count_player_one == count_player_two:
        return 0
    return 1 if count_player_one > count_player_two else 2

if __name__ == "__main__":
    go = [[1, 2, 2, 2], [2, 1, 1, 1], [0, 2, 1, 0]]
    print(who_won(go))