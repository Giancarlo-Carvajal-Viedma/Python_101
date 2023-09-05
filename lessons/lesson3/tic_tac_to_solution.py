
# Jag rekommenderar att skapa en variabel som heter board som innehåller en lista.
from typing import List, Tuple


global board
board = [['#', '#', '#'],
         ['#', '#', '#'],
         ['#', '#', '#']]

# rekommenderar följande funktioner men ni får göra som ni vill, lägg till fler eller ta bort.
# Pass ordet kan ni bara ta bort när ni implementerat eran version av funktionen.
# Det är bara en placeholder tills det finns något annat.


# Att skriva ut brädan kommer behöva göras många gånger så bra att ha en dedikerad funktion
def print_board():
    print("")
    for row in board:
        print(row)
    print("")
    pass


# vi behöver på något sätt få input från användaren vilken ruta de vill sätta sin markering på.
# Tips är kanske koordinater x, y? eller om ni har en roligare idé.
def get_input() -> Tuple[int, int]:
    valid = False
    while not valid:
        coordinates_string = input("Rad och kolumn för markering separera med mellanrum: ")
        valid, res = validate_input(coordinates_string)
    return res

# vi kommer kontrollera att inputen dels följer vårat valda system för inputm vi får lite på användaren till en gräns,
# men vi måste se till att det inte går att sätta in ett nytt märke där det redan finns ett.
def validate_input(string: str) -> Tuple[bool, Tuple[int, int]]:
    string = string.strip()
    split_string: List[str] = string.split(" ")
    if len(split_string) <2:
        print("Fel input")
        return (False, None)
    if not str.isdigit(split_string[0]) or not str.isdigit(split_string[1]):
        print("Fel input")
        return (False, None)
    
    row: int = int(split_string[0])
    col : int = int(split_string[1])
    if not 1 <= row <= 3 or not 1 <= col <= 3:
#    if row >3 or col>3 or row <1 or col <1:
        print("Fel input")
        return (False, None)

    if board[row-1][col-1] != "#":
        print("Fel input")
        return (False, None)
    
    return (True, (row-1, col-1))


# Efter input så måste vi lägga in så markeringen synns på brädan.
def update_board(row: int, col: int, marker: str):
    board[row][col] = marker


# Vi måste efter varje runda kolla om det faktiskt finns en vinnare. så att vi kan avsluta spelet.
def check_winner():
    # Kolla rader
    for row in board:
        row_set = set(row)
        if len(row_set) ==1 and row_set.pop() != "#":
            return True

    # Kolla kolumner
    for i in range(2):
        col_set = {board[0][i], board[1][i], board[2][i]}
        if len(col_set) ==1 and col_set.pop() != "#":
            return True
    
    # Kolla diagonaler
    across_set1 = {board[0][0],board[1][1],board[2][2]}
    if len(across_set1) ==1 and across_set1.pop() != "#":
        return True
    across_set2 = {board[0][2],board[1][1],board[2][0]}
    if len(across_set2) ==1 and across_set2.pop() != "#":
        return True
    return False    

    # Markering 0, x

def main():
    marker = "X"
    winner = False
    while not winner:
        marker = "O" if marker == "X" else "X"
        print_board()
        row, col = get_input()
        update_board(row,col, marker)
        winner = check_winner()

    print_board()
    print(f"Winner is {marker}")
main()
