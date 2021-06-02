# Damien Connolly G00340321
# Project for Applied Databases
# Lecturer: Gerard Harrison
# Code for this project adapted from lectures and examples @ https://learnonline.gmit.ie/course/view.php?id=2564


# Import mysql
import pymysql

# Function for viewing movies and actornames in groups of 5
def view_films():
    # Connect to mysql database
    db = pymysql.connect(host = "localhost", user = "root", password = "", db = "moviesdb", cursorclass = pymysql.cursors.DictCursor)
    # sql query to get filmname and actor name from database
    sql = "select * from filmcast inner join actor a on castactorid = a.actorid inner join film f on castfilmid = f.filmid order by f.filmname asc, a.actorname asc"
    
    with db:
        # Activate the cursor
        cursor = db.cursor()
        # Execute the sql query
        cursor.execute(sql)
        while True:
            # Store outputs as films and retrive in groups of five
            films = cursor.fetchmany(size = 5)
            # Loop through results and print filmname and actorname for each result
            for film in films:
                print(film["FilmName"],"","", film["ActorName"])
            # Set quit as q
            quit = input("-- Quit (q) --")
            # If the user enter "q" break the loop and return to the main menu
            if quit == "q":  
                print("---------------------------")
                print("Returning to the Main Menu")
                print("---------------------------")
                break

# Function to find film by ID(using the input as the Mongo function (viewMoviesWithSubtitles) results)
def filmByID(search):
    #  Connect to mysql database
    db = pymysql.connect(host = "localhost", user = "root", password = "", db = "moviesdb", cursorclass = pymysql.cursors.DictCursor)
    # Sql query to get filmname and first 30 characters of filmsynopsis
    sql = "select filmname, substring(filmsynopsis, 1, 30) as FilmSynopsis from film where FilmID in {};".format(search)
    
    with db:
        # Activate the cursor
        cursor = db.cursor()
        # Execute the sql query
        cursor.execute(sql)
        # Store results as films
        films = cursor.fetchall()
        # Loop through results and print filmname and filmsynopsis for each result
        for film in films:
            print(film["filmname"], "","",":", "", "", film["FilmSynopsis"])

# Function used to retrieve film id
def matchFilmID():
    # Connect to mysql database
    db = pymysql.connect(host = "localhost", user = "root", password = "", db = "moviesdb", cursorclass = pymysql.cursors.DictCursor)
    # Sql query to find film with input id
    sql = "select filmid from film;" #.format(ID)

    with db:
        # Activate the cursor
        cursor = db.cursor()
        # Execute the query
        cursor.execute(sql)
        # Store output as results
        results = cursor.fetchall()
        # Return results
        return results
    #except pymysql.err.AttributeError as e:
            #print(e)
        #except Exception as e:
            #print(e)



# Function for viewing actor by year of birth and gender
def viewByAgeAndGender(year, ActorGender):
    # Connect to mysql database
    db = pymysql.connect(host = "localhost", user = "root", password = "", db = "moviesdb", cursorclass = pymysql.cursors.DictCursor)
    # Sql query to select actor by year of birth and gender, and return actorname, month of birth and gender
    sql = "select actorname, monthname(actordob), actorgender from actor where year(actordob) = (%s) and ActorGender = (%s)"
    

    with db:
        # Activate the cursor
        cursor = db.cursor()
        # Execute the query
        cursor.execute(sql, (year, ActorGender))
        # Store the output as results
        results = cursor.fetchall()
        # Loop through the results and print actorname, birth of month and gender for each result
        for result in results:
            print("-------------------------------------------")
            print(result["actorname"],"","",":", "", "", result["monthname(actordob)"],"","",":", "", "", result["actorgender"])
            
# Function for viewing studios from database                 
def view_studios():
    # Connect to mysql database
    db = pymysql.connect(host = "localhost", user = "root", password = "", db = "moviesdb", cursorclass = pymysql.cursors.DictCursor)
    # Sql query to retrieve studio id and studio name in order of studio id ascending
    sql = "select studioid, studioname from studio order by studioid asc"

    with db:
        # Activate the cursor
        cursor = db.cursor()
        # Execute the query
        cursor.execute(sql)
        # Store outputs as studios
        studios = cursor.fetchall()
        print("\n------------------------------")
        print("     STUDIOS")
        print("------------------------------\n")
        # Loop through studios and print studio id and studio name for each studio
        for s in studios:
            print(s["studioid"], s["studioname"])

# Function to add new country to database
def add_country(CountryID, CountryName):
    # Connect to mysql database
    db = pymysql.connect(host = "localhost", user = "root", password = "", db = "moviesdb", cursorclass = pymysql.cursors.DictCursor)
    # Sql query used to insert a new country into database
    sql = "insert into country values (%s, %s)"

    with db:
        try:
            # Try activate the cursor
            cursor = db.cursor()
            # Execute sql query
            cursor.execute(sql, (CountryID, CountryName))
            # Add to database
            db.commit()
            # Printout to confirm country added to database
            print("Country:", CountryID, ",", CountryName, "has been added to the database")
        # Return errors when country name or country id already exist in database
        except pymysql.err.IntegrityError as e:
            print(e)
        except Exception as e:
            print(e)

