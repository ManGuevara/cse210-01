#this program is for creating a game called tic tac toe. 
#author: Manuel Guevara

def main():
    print("Wellcome to the tic tac toe game")
    print()
    print(f"There are two players and two symbols, one will use (x) and the other will use (o) ")
    print(f"in order for a player to win. he must complete a row, a column or a diagonal within the grid ")
    print()
    
    value=[1 , 2, 3, 4, 5, 6, 7, 8, 9] #this is a list with the values for the grid positions

    player = next_player("") #player variable defined 
#this line create a while loop based on winner or tie games.
    while winner(value) == False and tie(value) == False:
        get_grid(value)
        x_o_position(player,value)
        player = next_player(player)
    get_grid(value)
    print("Well played game. Thanks for participating!") 
       
    
#this function creates a grid for tic tac toe
def get_grid(value):

    print(f" {value[0]} | {value[1]}| {value[2]}")
    print(f" --+--+--         ")
    print(f" {value[3]} | {value[4]}| {value[5]}")
    print(f" --+--+--         ")
    print(f" {value[6]} | {value[7]}| {value[8]}")
    print()

# chooses the position of x or o

def x_o_position(player,value):
    move= int(input(f"{player}'s turn to choose a vacant position from the grid (1-9): "))
    value[move-1] = player

 # this function takes the turns of the  players  

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

def winner(value):
    #determine if there is a winner
    #there is winner when there is a complete row , column or diagonal with the same symbol
    #rows
    #(1,2,3)
    if  value[0] == "x" and value[1]  == "x" and  value[2] == "x" or value[0] == "o" and value[1]  == "o" and  value[2] == "o":
        return True
    #(4,5,6)
    elif value[3] == "x" and value[4]  == "x" and  value[5] == "x" or value[3] == "o" and value[4]  == "o" and  value[5] == "o":
        return True
    #(7,8,9)
    elif value[6] == "x" and value[7]  == "x" and  value[8] == "x" or value[6] == "o" and value[7]  == "o" and  value[8] == "o":
        return True

    #columns
    #(1,4,7)
    elif value[0] == "x" and value[3]  == "x" and  value[6] == "x" or value[0] == "o" and value[3]  == "o" and  value[6] == "o":
        return True
    #(2,5,8)
    elif value[1] == "x" and value[4]  == "x" and  value[7] == "x" or value[1] == "o" and value[4]  == "o" and  value[7] == "o":
        return True
    #(3,6,9)
    elif value[2] == "x" and value[5]  == "x" and  value[8] == "x" or value[2] == "o" and value[5]  == "o" and  value[8] == "o":
        return True

    #diagonals
    #(1,5,9)
    elif value[0] == "x" and value[4]  == "x" and  value[8] == "x" or value[0] == "o" and value[4]  == "o" and  value[8] == "o":
        return True
    #(3,5,7)
    elif value[2] == "x" and value[4]  == "x" and  value[6] == "x" or value[2] == "o" and value[4]  == "o" and  value[6] == "o":
        return True
    
    else:
        return False
    
def tie(value):
    #determine if the game is a tie
    #when there is a tie then there is no more options available
    for i in range(9):
        if value[i] != "x" and value[i] != "o":
            return False
    return True    
    
if __name__ == "__main__":
    main()