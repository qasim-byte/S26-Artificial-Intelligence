#Tuple containing movie names and their budgets.
movies = (
    ("Dilwale", 20000000),
    ("The Dictator", 29000000),
    ("WWE: Unreal", 14500000),
    ("WWE Raw", 379000000),
    ("FLASH", 365000000),
    ("Student of the year", 356000000),
    ("Incredibles 2", 200000000)
)
#Function to display movie statistics
def display(movies):
    list_price = [individual_movie[1] for individual_movie in movies]
    list_name1 = [individual_movie[0] for individual_movie in movies if individual_movie[1] == max(list_price)]
    list_name2 = [individual_movie[0] for individual_movie in movies if individual_movie[1] == min(list_price)]

    avg = sum(list_price) / len(list_price)
    high = max(list_price)
    low = min(list_price)

    print(f"""Average Budget --> {avg}
    Highest Budget --> {high}{list_name1}
    Lowest Budget -->  {low}{list_name2}""".center(50))

    print("\nMovies with budget higher than average:")
    for individual_movie in movies:
        if individual_movie[1] > avg:
            
            diff = individual_movie[1] - avg        #For Proper Indentation and Good Presentation i have used spaces along with f-strings
            
            print(f"{individual_movie[0]}{" "*(20-len(individual_movie[0]))} | {" "*(20-int(len(str(individual_movie[1]))))}Budget: {individual_movie[1]}{" "*(20-len(str(individual_movie[1])))} | {" "*(20-len(str(individual_movie[1])))}Above Average by: {diff}".ljust(80))
        
        if individual_movie[1] < avg:
            
            diff = avg - individual_movie[1]        #For Proper Indentation and Good Presentation i have used spaces along with f-strings
            
            print(f"{individual_movie[0]}{" "*(20-len(individual_movie[0]))} | {" "*(20-int(len(str(individual_movie[1]))))}Budget: {individual_movie[1]}{" "*(20-len(str(individual_movie[1])))} | {" "*(20-len(str(individual_movie[1])))}Below Average by: {diff}".ljust(80))

#Main Page Function

def main_page():
    user = input("""Enter 1 to see Statistics of the current movies OR
    Enter 2 to add more movies and see updated Statistics --> """)
    if user == "1":
        display(movies)
    elif user == "2":
        more_movies = list(movies)
        name = input("Enter the name of the movie you want to add: ")
        budget = int(input("Enter the budget of the movie you want to add: "))
        more_movies.append((name, budget))
        updated_movies = tuple(more_movies)
        display(updated_movies)
        main_page()
    elif user == "3":
        print("Exiting the program.")
        exit()
    else:
        print("Invalid input. Please enter 1 or 2 or 3")
        print()
        main_page()

main_page()