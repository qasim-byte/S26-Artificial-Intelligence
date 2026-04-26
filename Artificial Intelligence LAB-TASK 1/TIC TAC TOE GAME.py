def custom_sum(a, b, c):
    return a + b + c
def printboard(first_player,second_player):
    zero = "X" if first_player[0] else ("O" if second_player[0] else 0)
    one = "X" if first_player[1] else ("O" if second_player[1] else 1)
    two = "X" if first_player[2] else ("O" if second_player[2] else 2)
    three = "X" if first_player[3] else ("O" if second_player[3] else 3)
    four = "X" if first_player[4] else ("O" if second_player[4] else 4)
    five = "X" if first_player[5] else ("O" if second_player[5] else 5)
    six = "X" if first_player[6] else ("O" if second_player[6] else 6)
    seven = "X" if first_player[7] else ("O" if second_player[7] else 7)
    eight = "X" if first_player[8] else ("O" if second_player[8] else 8)
    print(f"\t\t\t   {zero}     |  {one}    |   {two}    ")
    
    print("\t\t\t---------|-------|-------")
    print(f"\t\t\t   {three}     |  {four}    |   {five}    ")
    
    print("\t\t\t---------|-------|-------")
    
    print(f"\t\t\t   {six}     |  {seven}    |   {eight}    ")
def checkwin(first_player,second_player):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(custom_sum(first_player[win[0]], first_player[win[1]], first_player[win[2]]) == 3):
            print("""\n\n\t\t
                    **************************
                        ❌ won the Match !🎉
                    **************************""")
            return 1
        if(custom_sum(second_player[win[0]], second_player[win[1]], second_player[win[2]]) == 3):
            print("""\n\n\t\t
                    **************************
                        ⭕ won the Match !🎉
                    **************************""")
            return 0 
    return -1   




if __name__ == "__main__":
    first_player = [0,0,0,0,0,0,0,0,0]
    second_player = [0,0,0,0,0,0,0,0,0]
     
    print("\t\t | Welcome To Tic Tac Toe! |\n")
    print("\t\t | Player 1 is '❌' and Player 2 is '⭕' |\n")
    print("--> Who starts first will be decided by toss😉🤞!\n ")
import random
toss = random.randint(0,1)
if (toss == 1):
    print("Player 1 --> '❌' wins the toss ✨ and will start first\n\n")
    turn = 1
else:
    print("Player 2 --> '⭕' wins the toss ✨ and will start first\n\n")
    turn = 0
while(True):
        printboard(first_player,second_player)
        if turn == 1:
            print("\n\t\t.................")
            print("\n\t\t|  ❌'s Turn !   |")
            print("\n\t\t.................\n")
            try:
                value = int(input("\n\t\tPlease Enter any Value : "))
            except ValueError:
                print("\n\t\tInvalid input! Enter a number from 0  to 8")
                continue
            if value < 0 or value > 8:
                print("\n\t\tInvalid Move !🎃 Try Again")
                continue
            if first_player[value] == 1 or second_player[value] == 1:
                print("\n\t\tInvalid Move !🎃 Try Again")
                continue
            first_player[value] = 1
        else :
            print("\n\t\t.................")
            print("\n\t\t|  ⭕'s Turn !   |")
            print("\n\t\t.................\n\n")
            try:
                value = int(input("\t\tPlease Enter any Value : "))
            except ValueError:
                print("\n\t\tInvalid input! Enter a number from 0  to 8")
                continue
            if value < 0 or value > 8:
                print("\n\t\tInvalid Move !🎃 Try Again")
                continue
            if first_player[value] == 1 or second_player[value] == 1:
                print("\n\t\tInvalid Move !🎃 Try Again")
                continue
            second_player[value] = 1
        cwin = checkwin(first_player,second_player)
        if cwin!=-1:
            print("""\n\n\t\t\t
                  **************************
                  Match Over !
                  Game made with ❤ by Qasim
                  **************************""")
            break
        # Check for draw
        if sum(first_player) + sum(second_player) == 9:
            printboard(first_player, second_player)
            print("It's a draw! 🤝")
            break
        turn = 1 - turn
        