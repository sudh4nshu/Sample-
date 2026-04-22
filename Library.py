def library():
    while True:
        print("MENU")
        print("1.Add Book")
        print("2.Show Books")
        print("3.Issue Book")
        print("4.Return Book")
        print("5.Exit") 
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_book()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print("Thank You")
            break
#DATABASE
books = []
issued_books = []
#add function
def add_book():
    name = input("Enter book name:")
    books.append(name)
    print("Book added successfully!")
#show function
def show_books():
    if len(books) == 0:
        print("No books available.")
    else:
        print("Available Books:")
        for book in books:
            print(book) 
#Issue function
def issue_book():
    if len(books)==0:
        print("No books available to issue.")
        return
    else:
        name = input("Enter book name to issue:")
        if name in books:
            books.remove(name)
            issued_books.append(name)
            print(name," issued successfully!")
        else:
            print("Book not available.")
#Return function
def return_books():
    name = input("Enter book name you want to return:")
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print(name," returned successfully!")
    else:
        print(name,"This book is not issued.")

library()