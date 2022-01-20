



def main():

    value=[1 , 2, 3, 4, 5, 6, 7, 8, 9]
    
    print(tie(["x" , "x", "x", "o", "o", "o", "x", "x", "x"]))
  
def tie(value):
    #determine if the game is a tie
    #when there is a tie then there is no more options available
    for i in range(9):
        if value[i] != "x" and value[i] != "o":
            return False
    return True    
    
main()