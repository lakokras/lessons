FILENAME = "Books.csv"
file = open(FILENAME, "a")

names = [
    "To Kill a Mockingbird",
    "A Brief History of Time",
    "The Great Gatsby",
    "The Man Who Mistook His Wife for a Hat",
    "Pride and Prejudice"]

authors = [
    "Harper Lee", 
    "Stephen Hawking",
    "F. Scott Fitzgerald",
    "Oliver Sacks",
    "Jan Austen"]
    
ages = [1960, 1988, 1922, 1985, 1813]

for i in range(len(names)):
    newRecord = names[i] + ", " + authors[i] + ", " + str(ages[i]) + "\n"
    file.write(str(newRecord))
file.close()
file = open("Books.csv", "r")
for row in file:
    print(row)  
file.close()