#Copyright (c) 2026 FizzBuzz Game by Qasim Ashfaq
def fizzbuzz_game():
    player_1 = input("Enter Player 1 name: ").strip() or "Player 1"
    player_2 = input("Enter Player 2 name: ").strip() or "Player 2"
    players = [player_1, player_2]
    # 0 -> player1, 1 -> player2 (turn indicator logic)
    turn = 0  
    n = 1

    while True:
        if n % 15 == 0:
            expected = "FizzBuzz"
        elif n % 3 == 0:
            expected = "Fizz"
        elif n % 5 == 0:
            expected = "Buzz"
        else:
            expected = str(n)

        ans = input(f"{players[turn]} - {n} --> ").strip()
        if ans != expected:
            print(f"Wrong! Expected '{expected}'. {players[turn]} is eliminated.")
            print(f"{players[1 - turn]} wins!")
            break

        # if the correct answer is given; the program demands the next number
        n += 1
        turn = 1 - turn

if __name__ == "__main__":  #The Dunder Method is used to run the code only if the file is executed directly
    fizzbuzz_game()
