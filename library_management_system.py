library=[]

while True:
    print("\n----- Library Menu -----")
    print("1 for add book")
    print("2 for view book")
    print("3 for removing book")
    print("4 for exit")
    n=input("Enter you choice: ")
    if n=="1":
        book=input("Enter the name of the book to add: ")
        library.append(book)
        print("Book Added!")
    elif n=="2":
        if library:
            for book in library:
                print(book)   
        else:
            print("Library is empty")  
    elif n=="3":
        book=input("Enter the name of the book to delete: ")
        if book in library:
            library.remove(book)
            print("Book Deleted!")
        else:
            print("Book not present")    

    elif n=="4":
        print("Exiting!")
        break
    else:
        print("invalid choice")
            

    
    
    

