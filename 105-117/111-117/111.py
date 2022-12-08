fileName = "Books.csv"
file = open(fileName, "a")

books = [
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
    
year = [1960, 1988, 1922, 1985, 1813]

for i in range(len(books)):
    newBook = books[i] + ", " + authors[i] + ", " + str(year[i]) + "\n"
    file.write(str(newBook))

file.close()
file = open("Books.csv", "r")

for row in file:
    print(row)  
file.close()
