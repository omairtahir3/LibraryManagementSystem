def mainmenu():
    print("==========================LIBRARY MANAGEMENT SYSTEM=======================")
    print()
    print("1. LIBRARIAN")
    print("2. BORROWER")
    mainoption=int(input("Select one from above: "))
    while(mainoption<1 or mainoption>2):
        print("Your selected option is not within the range.")
        mainoption = int(input("Select the option 1-2: "))
    if (mainoption==1):
        menu1()
    elif (mainoption==2):
        menu2()
def menu1():
    print("1. Add Book")
    print("2. Register Borrower")
    print("3. Generate Report")
    option1=int(input("Select the option 1-3:"))
    while(option1<1 or option1>3):
        print("Your selected option is not within the range.")
        option1 = int(input("Select the option 1-3: "))
    if (option1==1):
        booktitle=input("Enter the title of the book: ")
        author=input("Enter the author of the book: ")
        bookid=input("Enter the book id: ")
        addbook(booktitle, author, bookid)
        showbooks()
    elif (option1==2):
        name=input("Enter your name: ")
        email=input("Enter the email address: ")
        borrowerid=input("Enter the borrower's id: ")
        regborrowers(name,email,borrowerid)
    elif (option1==3):
        reports()
def menu2():
    print("1. Avaiable Books")
    print("2. Borrow Book")
    print("3. Return Book")
    option2=int(input("Select the option: "))
    while(option2<1 or option2>2):
        print("Your selected option is not within the range.")
        option2 = int(input("Select the option 1 or 2: "))
    if (option2==1):
        bookid=input("Enter the book id:")
        availablebooks(bookid)
    elif(option2==2):
        borrowersid = input("Enter the borrower's id: ")
        booksid = input("Enter the book id: ")
        eligible(booksid, borrowersid)
    elif(option2==3):
        returnbooktitle=input("Enter the title of the book you are returning: ")
        returnbookid = input("Enter the Book ID of the book you want to return: ")
        returnborrowerid= input("Enter the Borrower ID of the borrower: ")
        bookreturn(returnbooktitle,returnbookid,returnborrowerid)
def addbook(booktitle,author,bookid):
    book=False
    books = [booktitle,',',author,',',bookid + "\n"]
    file = open('addbooks.txt', 'a')
    read = open("addbooks.txt", "r")
    for line in read:
        if bookid in line:
            readslines = line
            seperate=readslines.split(',')
            book=True
            break
    if (book == True):
        print("This Book ID already exists.")
    else:
         file = open('addbooks.txt', 'a')
         for i in books:
            file.write(i)
         file.close()
         read_file = open("addbooks.txt", "r")
         print("The book is added to the library successfully!")

def showbooks():
    file=open('addbooks.txt', 'r')
    read=file.read()
    print(read)

def regborrowers(name, email, borrowerid):
    borrow = False
    borrowersinfo = [name,',' ,email,',',borrowerid + '\n']
    file = open('borrowersinfo.txt', 'a')
    read = open("borrowersinfo.txt", "r")
    for line in read:
        if borrowerid in line:
            readslines = line
            seperate=readslines.split(',')
            borrow=True
            break
    if (borrow== True):
        print("This Borrower ID already exists.")
    else:
        file = open('borrowersinfo.txt', 'a')
        for i in borrowersinfo:
            file.write(i)
        file.close()
        read_file = open("borrowersinfo.txt", "r")
        print("Borrower is added successfully!")
def borrowbook(booksid,borrowersid):
    newspace='\n'
    file1 = open('borrowersinfo.txt','r')
    searchline=file1.readline()
    file2 = open('bookborrower.txt', 'a')
    for line in file1:
        if borrowersid in line:
            lineread= line
            seperate = lineread.split(',')
            file2.write(seperate[0]+","+seperate[2])

    file = open('addbooks.txt', 'r')
    searchline = file.readline()
    file3 = open('borrowbook.txt', 'a')
    for line in file:
        if booksid in line:
            linereads2 = line
            seperate2 = linereads2.split(',')
            file3.write(seperate2[0]+","+seperate2[2])
            file3.close()
def searchbook(booksid,borrowersid):
    availability=input("Enter the name of book you need: ")
    file=open('borrowbook.txt','r')
    borrow=False
    borrow1=False
    for lines in file:
        if (availability in lines):
          borrow=True
          break
    if (borrow==False):
        file1 = open('addbooks.txt', 'r')
        for lines in file1:
            if (availability in lines):
              borrow1 = True
              break
        if (borrow1==True):
            print("Book Borrowed Successfully!")
            borrowbook(booksid, borrowersid)
        elif (borrow1==False):
            print("The book is currently unavailable in the library!")
    elif (borrow==True):
       print("The book is not available for borrowing.")
def availablebooks(bookid):
    borrowbooks=False
    addbooks=False
    file=open('borrowbook.txt','r')
    for lines in file:
        if (bookid in lines):
            borrowbooks=True
            break
    file1=open('addbooks.txt','r')
    for lines in file1:
        if (bookid in lines):
            addbooks=True
            break 
    if (addbooks==True and borrowbooks==False):
        print("This book is available for borrowing!")
    elif (addbooks==True and borrowbooks==True):
        print("This book is unavailable for borrowing.")
    elif (addbooks==False and borrowbooks==False):
        print("This book is currently unavailable in the library.")
def eligible(booksid,borrowersid):
    file=open('bookborrower.txt','r')
    eligibility=True
    for line in file:
        if borrowersid in line:
            eligibility=False
            break
    if (eligibility==False):
        print("The borrower is ineligible for borrowing.")
    elif (eligibility==True):
        searchbook(booksid, borrowersid)

def bookreturn(returnbooktitle,returnbookid,returnborrowerid):
    returnbook=False
    borrowbook=False
    bookreturned = [returnbooktitle,',',returnborrowerid,',',returnbookid + "\n"]
    if (returnbook==False):
        file = open('returnbook.txt', 'r')
        for line in file:
            if returnborrowerid in line:
                returnbook=True
                break
    if (returnbook==True):
        print("The book is already returned to the library!")
    else:
        file = open('bookborrower.txt', 'a')

        read = open("bookborrower.txt", "r")
        for line in read:
            if returnborrowerid in line:
              borrowbook = True
              break
        if (borrowbook == True and returnbook==False):
            file = open('returnbook.txt', 'a')
            for i in bookreturned:
                file.write(i)
            read_file = open("returnbook.txt", "r")
            print("The book is returned to the library successfully!")
        elif (borrowbook==False and returnbook==False):
                print("The book you are are returning doesnot match the Book ID!")

def reports():
    print("==========================LIBRARY MANAGEMENT SYSTEM=======================")
    print("===================================REPORTS================================")
    reportdata = [['Book ID', 'Book Name']]
    file = open('addbooks.txt', 'a')
    file=open('addbooks.txt','r')
    searchline = file.readline()
    for line in file:
        seperate = line.split(',')
        reportdata.append([seperate[2],seperate[0]])

    print()
    print("  ","==", "All Books","==")
    print()
    for i in reportdata:
        print('{:<10} {:<25}'.format(*i))

    reportdata2 = [['Borrowers ID', 'Borrowers Name']]
    file2 = open('bookborrower.txt', 'a')
    file2 = open('bookborrower.txt', 'r')
    searchline = file2.readline()
    for line in file2:
        seperate2 = line.split(',')
        reportdata2.append([seperate2[1],'   '+seperate2[0]])
    print()
    print("    ","==", "Book Borrowers","==")
    print()
    for i in reportdata2:
        print('{:<15} {:<20}'.format(*i))
    reportdata3 = [['Book Title']]
    file3 = open('borrowbook.txt', 'a')
    file3 = open('borrowbook.txt', 'r')
    searchline = file3.readline()
    for line in file3:
        seperate3 = line.split(',')
        reportdata3.append([seperate3[0]])
    print()
    print("    ","==" ,"Books Borrowed","==")
    print()
    for i in reportdata3:
        print('{:<15}'.format(*i))

    reportdata4 = [['Book Title','Borrowers ID']]
    file4 = open('bookborrower.txt', 'a')
    file4 = open('bookborrower.txt', 'r')
    searchline = file4.readline()
    for line in file4:
        seperate4 = line.split(',')
        reportdata4.append([seperate4[0],'   '+seperate4[1]])
    print()
    print("  ","==","Books Returned","==")
    print()

    for i in reportdata4:
        print('{:<15} {:<20}'.format(*i))





print(mainmenu())

