#!/usr/bin/python3

def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Checks if there is a winner."""
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """Main game logic."""
    board = [[" "]*3 for _ in range(3)] 
    player = "X" 
    while not check_winner(board):
        print_board(board)

        
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

                
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid row or column! Please enter values between 0 and 2.")
                elif board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                else:
                    break 
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

        
        board[row][col] = player

        player = "O" if player == "X" else "X"

    print_board(board)
    print(f"Player {player} wins!")

tic_tac_toe()
