# Damien Connolly G00340321
# Project for Applied Databases
# Lecturer: Gerard Harrison
# Code for this project adapted from lectures and examples @ https://learnonline.gmit.ie/course/view.php?id=2564

# Import MySQL and Mongo to connect to database and call functions
import mysql
import mongo

# Main function
def main():
    # Call the display menu function
    display_menu()

    while True:
        # Ask user to select option choice
        choice = input("Choice: ")
        
        # 1 - View Films
        if (choice == "1"):
            # Call function from mysql
            films = mysql.view_films()
            # Return to display menu
            display_menu()
        
        # 2 - View Actors by Birth and Gender
        elif (choice == "2"):
            print("View by Age and Gender")
            print("--------------------------")
            # Ask user to input year 
            year = (input("Enter Year: "))
            # Check if input is a number, if not ask user for input until number is entered
            # Adapted from https://www.w3schools.com/python/ref_string_isdigit.asp
            while not year.strip().isdigit():
                year = input("Enter Year: ")

            # Ask user to input gender    
            ActorGender = input("Enter Gender: ")
            # Check if the input is male, female or blank
            # Adapted from https://www.askpython.com/python/examples/in-and-not-in-operators-in-python
            while ActorGender not in ("male", "female", ""):
                # If input is not correct ask again
                ActorGender = input("Please Enter (male/female): ")
                # If input is correct break the loop and continue
                while ActorGender in ("male", "female", ""):
                    break
            # Call the function from mysql
            results = mysql.viewByAgeAndGender(year, ActorGender)
            # Return to display menu
            display_menu()

        # 3 - View Studios
        elif (choice == "3"):
            # Call function from mysql
            mysql.view_studios()
            # Return to display menu
            display_menu()

        # 4 - Add New Country
        elif (choice == "4"):
            print("\nAdd New Country")
            print("--------------------------")
            # Ask user for country id
            CountryID = input("Enter CountryID: ")
            # Check if input is a number, if not ask user for input until number is entered
            # Adapted from https://www.w3schools.com/python/ref_string_isdigit.asp
            while not CountryID.strip().isdigit():
                CountryID = input("Enter CountryID: ")
            # Ask user to enter country name
            CountryName = input("Enter CountryName: ")
            # If country name is not entered ask again until one is entered
            while CountryName == "":
                CountryName = input("Enter CountryName: ")
            # Call function from mysql
            mysql.add_country(CountryID, CountryName)
            # Return to display menu
            display_menu()

        # 5 - View Movies With Subtitles
        elif (choice == "5"):
            print("\nView Movies With Subtitles")
            print("--------------------------")
            # Ask user to enter subtitles being searched for
            subtitles = input("Choose Subtitles: ")
            # If no subtitles are entered return to display menu
            if (subtitles == ""):
                display_menu()
                continue
            

                
            # Call the function from Mongo and store results as results   
            results = mongo.viewMoviesWithSubtitles(subtitles)
            # Create an empty array to append results in
            array = []
            # Loop through results
            for result in results:
                # Append each result in the array as _id
                array.append(result["_id"])
            # Convert the array to a tuple(as search) to pass back to mysql
            # Adapted from https://www.geeksforgeeks.org/python-convert-a-list-into-a-tuple/
            search = tuple(array)
            # Print heading for searched subtitles
            print("\nMovies With", subtitles, "Subtitles")
            print("--------------------------")
            # Call function from mysql
            mysql.filmByID(search)
            # Return to display menu
            display_menu()

        # 6 - Add New MovieScript
        elif (choice == "6"):
            print("\nAdd New MovieScript")
            print("--------------------------")
            # Ask user to input ID
            ID = (input("ID: "))
            # Check if input is a number, if not ask user for input until number is entered
            # Adapted from https://www.w3schools.com/python/ref_string_isdigit.asp
            while not ID.strip().isdigit():
                ID = (input("ID: "))
        
            # Create empty array to store each word
            array = []
            while True:
                # Ask user to input keywords
                words = input('Keywords(-1 to end): ')
                # If user enters -1 then quit
                if words == "-1":
                    break
                # Append words to array
                array.append(words)
            # Store array as keywords
            keywords = array

            # Create empty array to store each subtitle
            array = []
            while True:
                # Ask user to input subtitle
                subtitle = input('Subtitles(-1 to end): ')
                # If user enter -1 then quit
                if subtitle == "-1":
                    break
                # Append subititles to array
                array.append(subtitle)
            # Store array as subtitles  
            subtitles = array
           
            # Insert new movie into Mongo database
            mongo.addNewMovieScript(ID, keywords, subtitles)
            # Return to display menu
            display_menu()

        # Exit program if user enters x
        elif (choice == "x"):
            break


# Function for display menu 
def display_menu():
    print(f"\n-------------------------------------------")
    print(f"----------------MAIN MENU--------------")
    print(f"-------------------------------------------")
    print(f"\n")
    print(f"        PLEASE SELECT AN OPTION            ")
    print(f"-------------------------------------------")
    print(f"\n")
    print(f"\n1 - View Films\n")
    print(f"\n2 - View Actors by Birth and Gender\n")
    print(f"\n3 - View Studios\n")
    print(f"\n4 - Add New Country\n")
    print(f"\n5 - View Movie with Subtitles\n")
    print(f"\n6 - Add New MovieScript\n")
    print(f"\nX - Exit Application\n")
    print(f"\n")



main()