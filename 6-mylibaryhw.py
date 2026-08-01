books = ["Maths", "Physics", "Biology", "Chemistry", "History"]
print("Original List:", books)

books.append("Economics")
print("After Append:", books)

books.insert(2 , "Geography")
print("After Insert:", books)

books.remove("History")
print("After Remove:", books)

books.sort()
print("After Sort:", books)

books.reverse()
print("After Revese:", books)

print("Total Books:", len(books))
