# Damien Connolly G00340321
# Project for Applied Databases
# Lecturer: Gerard Harrison
# Code for this project adapted from lectures and examples @ https://learnonline.gmit.ie/course/view.php?id=2564


# Import pymongo
import pymongo
# Store in a variable myclient - it is global so it can be used in different functions. The current value is None.
myclient = None

# Function to connect to Mongo database 
def connect():
    global myclient
    myclient = pymongo.MongoClient(host="localhost", port=27017)
    # Used to check if mongo has connected successfully
    myclient.admin.command('ismaster')

# Function for viewing movies with subtitles
def viewMoviesWithSubtitles(subtitles):
    # Check if the function is connected
    if (not myclient):
        # If it is not connected this function is called to connect            
        connect()        
    # Database name
    db = myclient["movieScriptsDB"]
    # Collection name
    col = db["movieScripts"]
    # Mongo query - Search for subtitles entered by user
    # Code adapted from https://docs.mongodb.com/manual/reference/operator/aggregation/regexMatch/
    query = {"subtitles": { "$regex": "\\b" + subtitles + "\\b", "$options": 'i'}}
    # Mongo projection - project _id
    proj = {"_id":1}
    # Call function, store output as results
    results = col.find(query, proj)
    # Return results
    return results

# Function to add new movie script to database   
def addNewMovieScript(ID, keywords, subtitles):
    # Check if the function is connected
    if (not myclient):
        # If it is not connected this function is called to connect            
        connect()        
    # Database name
    db = myclient["movieScriptsDB"]
    # Collection name
    col = db["movieScripts"]
    # New movie script document
    newMS = {"_id": ID, "keywords": keywords, "subtitles": subtitles}
    
    try:
        # When the function is called try to insert new document into database
        col.insert_one(newMS, False) 
        # Exception added here to print errors  
    except pymongo.errors.DuplicateKeyError as e: 
        # Error when existing _id entered 
        print("*** ERROR ***: _id DATA already exists, please try again.") 
    except Exception as e:
        # Other errors
        print("Error:", e)


# Main function used to connect to database and call functions
def main():
    if (not myclient):
        try:
            connect()
        except Exception as e:
            print("error", e)
        
        viewMoviesWithSubtitles(subtitles)

        addNewMovieScript(ID, keywords, subtitles)

# The main function called
if __name__ == "__main__":  
	main()