#this program is for creating a game called tic tac toe. 
#author: Manuel Guevara

def main():
    print("Wellcome to the tic tac toe game")
    print()
    print(f"There are two players and two symbols, one will use (x) and the other will use (o) ")
    print(f"in order for a player to win. he must complete a row, a column or a diagonal within the grid ")
    print()

    value=[1 , 2, 3, 4, 5, 6, 7, 8, 9]
#this line calls the function get grid
    get_grid(value)
  
#sample of the grid
def get_grid(value):

    print(f" {value[0]} | {value[1]}| {value[2]}")
    print(f" --+--+--         ")
    print(f" {value[3]} | {value[4]}| {value[5]}")
    print(f" --+--+--         ")
    print(f" {value[6]} | {value[7]}| {value[8]}")
    print()
# chooses the position of x or o
def x_o_position(value):
    first_move= input("choose a vacant position from the grid: ")
    turn= "x"
    if turn == "x":
        value[first_move-1]= "x"
    
    elif turn == "o":
        value[first_move-1]= "o"
        

    
main()
   