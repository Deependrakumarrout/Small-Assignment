# create library class
# then define a method to display
# If any customer want to lend a book then define a method
# If the book is not available (then i have to say to who had taken that book)
# If anyone want to donate any book then then define a add_book named function(a book will be add in that liberary)
# If i want to return this book to any person then define a return function

#Maintain a dictionary that which person has took which book.(books:name__of_person)
#create a main function and run an infinite while loop asking user for their input


#Upload on github
class Library:
     def __init__(self,list_of_books,library_name,):
         self.list_of_books=list_of_books
         self.library_name=library_name
         self.dict={}

     def display_books(self):
         print("There are the list of books available here -")
         for books in self.list_of_books:
             print(books)

     def lend_books(self,books,user):
         if books in self.list_of_books:
            if books not in self.dict.keys():
                 self.dict.update({books:user})
                 print("ok sir/Ma'am this book is successfully lend by you")
            else:
                 print(f"Sorry Sir/Ma'am its already lend by {self.dict[books]} ")
         else:
            print("Please check the spelling of the book that you type in.")

     def add_books(self,books):
         self.list_of_books.append(books)
         print("Thanks for donating this book.")

     def return_books(self,books):
         if books in self.dict.keys():
             self.dict.pop(books)
             print("We are thankful that you are returning this book on time.")
         else:
             print("You have not lended this book from our library.")
             print("Sorry we can't received it..")

if __name__ == '__main__':
    lib_name = Library(["Jungle book ", "The secrete", "Fury of sun", "Five lies my teacher told me", "Neural_network",
                        "Effective english"], "Robbin donner Library")
    while True:
        print(f"\nWelcome to {lib_name.library_name}")
        user_input={1:"to display available books",2:"to lend book",3:"to add book",4:"to return book"}
        for key,value in user_input.items():
            print(f"Press {key} {value}")

        raw_input=int(input("Enter to select:"))
        if raw_input not in [1,2,3,4]:
            print("Kindly enter the correct input..")
            continue

        print()
        if raw_input == 1:
            lib_name.display_books()
            print()
        elif raw_input == 2:
            book_name1 = input("Enter the name of the book you want to lend:")
            user_name=input("Please enter your name sir/maam:")
            lib_name.lend_books(book_name1,user_name)

        elif raw_input == 3:
            book_name2=input("Enter the name of the book you want to add:")
            lib_name.add_books(book_name2)

        elif raw_input == 4:
            book_name3=input("Please enter the name of the book you want to return:")
            lib_name.return_books(book_name3)

        print("Ok anything else you want from us. Please enter [yes or no]:")
        restart=""
        while restart != "yes" and restart != "no":
            restart = input("Enter the correct key to proceed:")
            if restart == "yes".lower():
                continue
            elif restart =="no".lower():
                print("Thanks for giving us a change {Please visit us again}")
                exit()



'''
class Library:
    def __init__(self, list_of_books, library_name):
        self.data = {}
        self.list_of_books = list_of_books
        self.library_name = library_name


        for books in self.list_of_books:
            self.data[books]=None

    def display_books(self):
        for index,books in enumerate(self.list_of_books):
            print(f"{index}) {books}")


    def lend_books(self,book,author):
        if book in self.list_of_books:
            if self.data[book] is None:
                 self.data[book]=author
            else:
                print(f"Sorry this book is lended by {self.data[book]} ")
        else:
            print(f"You have written wrong book name")


    def add_books(self,book_name):
        self.list_of_books.append(book_name)
        self.data[book_name]=None

    def return_book(self,book_name,author):
        if book_name in self.list_of_books:
            if self.data[book_name] is not None:
                self.data.pop(book_name)
            else:
                print("Sorry but This book name is not lended")
        else:
            print("You have written wrong book name")


    def delete_book(self,book_name):
            # if self.data[book_name] == self.add_books(book_name):
            #     print("Sorry can't delete this book it is landed by someone ")
            # else:
                self.list_of_books.remove(book_name)

        #self.data.pop(book_name)

# lst_of_books=Library.list_of_books=["Jungle book ","The secrete","Fury of sun","Five secrete","All of Neutral_network","Effective english"]

def main():
    lib_name = "Ration Library"
    Library_=["Jungle book ","The secrete","Fury of sun","Five secrete","All of Neutral_network","Effective english"]
    dee=Library(Library_,lib_name)
    print(f"Welecome To {lib_name} \nDisplay Book Using 'd' and add lend book using 'l' and Return a Book using 'r' \nAdd Book Using 'a' and del to delete book\n")

    exit=False
    while (exit is not True):
        raw_input=input("option")
        print("\n")
        if raw_input == "q":
            exit=True

        elif raw_input == "d":
            dee.display_books()

        elif raw_input == "l":
            input_2=input("Sir/Maam please enter your name: ")
            input_3=input("Which book you want to land: ")
            print("\n Book Lend \n")
            dee.lend_books(input_3,input_2)

        elif raw_input == "a":
            # input(Library.add_books("a"))
            input_2=input("Enter the book name you want to add: ")
            dee.add_books(input_2)

        elif raw_input == "r":
            #rt = input(Library.return_books("r"))
            input_2=input("Enter your name:")
            input_3=input("Name of the book you want to return:")
            dee.return_book(input_3,input_2)

        elif raw_input == "del":
            try:
                input_2=input("Enter the book name you want to delete:")
                dee.delete_book(input_2)
            except ValueError:
                print("Try to insert right book")

if __name__ == '__main__':
    main()

'''


'''
class Library():
    def __init__(self, list_of_books, Library_name):
        # creating a dictionary of all books keys
        self.lend_data = {}
        self.list_of_books = list_of_books
        self.library_name = Library_name

        # adding books to dictionary
        for books in self.list_of_books:
            # none means No author have lend this book
            self.lend_data[books] = None

    def display_books(self):
        for index, books in enumerate(self.list_of_books):
            print(f"{index}){books}")

    def lend_book(self, book, author):
        if book in self.list_of_books:
            if self.lend_data[book] == None:
                self.lend_data[book] = author
            else:
                print(f"Sorry This book is lend by {self.lend_data[book]}")
        else:
            print("You have written wrong book name")

    def return_book(self, book, author):
        if book in self.list_of_books:
            if self.lend_data[book] is not None:
                self.lend_data.pop(book)
            else:
                print("Sorry but This book is not Lend")
        else:
            print("You have written wrong book name")

    def add_book(self, book_name):
        self.list_of_books.append(book_name)
        self.lend_data[book_name] = None

    def delete_book(self, book_name):
        self.list_of_books.remove(book_name)
        self.lend_data.pop(book_name)


def main():
    # By default variables
    list_books = ['Cookbook', 'Motu Patlu', 'Chacha_chaudhary', 'Rich Dad and Poor Dad']
    Library_name = 'Harry'
    secret_key = 123456

    Harry = Library(list_books, Library_name)

    print(f"Welecome To {Harry.library_name} library\n\nq for exit \nDisplay Book Using 'd' and add lend book using 'l' and Return a Book using 'r' \nAdd Book Using 'a' and Delete Book using 'del' \n ")


    Exit = False
    while (Exit is not True):
        _input = input("option:")
        print("\n")

        if _input == "q":
            Exit = True

        elif _input == "d":
            Harry.display_books()

        elif _input == "l":
            _input2 = input("What is your name:")
            _input3 = input("Which Book Do you want to lend:")
            print("\n Book Lend \n")
            Harry.lend_book(_input3, _input2)

        elif _input == "a":
            _input2 = input("Book name:")
            Harry.add_book(_input2)

        elif _input == "del":
            _input_secret = int(input("Write the secret key to delete:"))
            if (_input_secret == secret_key):
                _input2 = input("Book Which you want to delete:")
                Harry.delete_book(_input2)
            else:
                print("Sorry We can't Delete the Book")

        elif _input == "r":
            _input2 = input("What is your name:")
            _input3 = input("Which Book Do you want to return:")
            Harry.return_book(_input3, _input2)

if __name__ == "__main__":
   main()


#I can't leave without you ok for me you are everything i have learn much more with you i just want to be a part of you.
#i want my reason why i can't able to do project which is stucking me .
#I am not going to leave you ok.
#If there will be any problem i will always be there to shot it out. Bec i want to do so just walk with me.
#No more excuse for solving problem or any kind of things that get stuck to me.(BREAK ALL THE OBSTACAL)
#YUP i can do programming because i have some interest to do something with it ok.
#NO i can stop me to do programming.
#If any obstacal i get i will be happy to make him my friend so that we can easily find that solution.



from pygame import mixer
from datetime import datetime
from time import time

def loop(path,stop):
    mixer.init()
    mixer.music.load(path)
    mixer.music.play(-1)
    while True:
        user_input=input("")
        if user_input == stop:
            mixer.music.stop()
            break

def data_store(txt):
    with open("data_file.txt","a") as dee:
        dee.write(txt + str(datetime.now())+"\n")


if __name__ == '__main__':
    eyes_exercise = time()
    water_time = time()
    physical_exercise = time()

    eyes=10
    water=45
    physical_exer=69

    while True:
        if time()-eyes_exercise>eyes:
            print("Sir it's time for eyes exercise. Please enter the 'done' to stop")
            loop("C:/Users/user/Downloads/water.mp3","done")
            eyes_exercise = time()
            data_store("Record of doing exercise:")
'''



'''
class Library:
    #A constructor
    def __init__(self,books_list,name):
        self.books_list=books_list
        self.name=name
        #creating a blank dictionary which means detect who took which book.
        self.lendDict={}


    #A function to display books
    def display_books(self):
        print(f"There are the available books in our library:{self.name}")
        for book in self.books_list:
            print(book)

    #This lend book function will first take user and then book
    def lend_book(self,user,book):
    #To lend a book first i will check that it will in the keys
        if book not in self.lendDict.keys():
            #update function update the dictionary
            self.lendDict.update({book:user})#The update method updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs.
            #The update() method adds elements(s) to the dictionary if the key is not in the dictionary if the key is in the dictionary, it updates the key with the new value.
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")


    #To add only a book so i have written as a parameter
    def add_book(self,book):
        self.books_list.append(book) #The append method adds an item ot the end of the list. the append method adds a single item to the existing list.
        print("Book has been added to the book list")

    #What is pop?
    #pop is an inbuilt function in python that removes and return last value from the list or the given index value.
    #If the index is not given, then the last element is popped out and removed.
    def return_book(self,book):
        self.lendDict.pop(book) #Here pop will remove


if __name__ ==  '__main__':
    #Creating a object here to give an argument
    deepak=Library(['Jungle book','The secrete','Fury of sun','Five secrete','All of Neutral_network','Effective english'],"Awesome")

    while True:
        print(f"Welcome to the {deepak.name}")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        try:
            user_choice = int(input())

            if user_choice == 1:
                deepak.display_books()
            elif user_choice == 2:

                book=input("Enter the name of the book you want to lend:")
                user=input("Enter your name:")
                deepak.lend_book(user,book)

            elif user_choice == 3:
                book=input("Enter the name of the book you want to add:")
                deepak.add_book(book)

            elif user_choice == 4:
                book=input("Enter the name of the book you want to remove:")
                deepak.return_book(book)
            else:
                print("Not a valid option")
        except:
            print("Number error please insert the correct number to type select an option")

        print("Press q to quit and c to continue")
        user_choice2=" "
        while (user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            if user_choice2 =="c":
                continue
'''


'''
def getdate():
    import datetime
    return datetime.datetime.now()

print("Please select one of the client name")
client_name={1:"Raju",2:"suraj",3:"Tarun"}
for key,value in client_name.items():
    print(f"Press {key} for {value}")
client_list=int(input("Enter here:"))

if client_list == 1:
    print(f"you have selected to {client_name[client_list]}")
elif client_list == 2:
    print(f"You have selected to {client_name[client_list]}")
elif client_list == 3:
    print(f"You have selected to {client_name[client_list]}")

print()

print("Ok which type of things you want from him like - FOOD OR EXERCISE (so for that) -")
condition_list={1:"Food",2:"Exercise"}
for key,value in condition_list.items():
    print(f"Press {key} for {value}")
client_input=int(input("Enter here:"))

if client_input == 1:
    print(f"you have selected for {condition_list[client_input]}")
elif client_input == 2:
    print(f"You have selected for {condition_list[client_input]}")

print()

Operation_list={1:"log",2:"retrieve"}
for key,value in Operation_list.items():
    print(f"Press {key} for {value}")
user_input=int(input("Enter here:"))

if user_input ==1:
    print(f"You have select to {Operation_list[user_input]}")
    print(f"Enter the {condition_list[client_input]} that you want to recommend:")
    f = open(client_name[client_list]+"_"+condition_list[client_input]+".txt","a")
    u="y"
    while (u is not "n"):# print(f"Enter {condition_list[client_input]}")
        text=input()
        f.write("["+str(getdate())+"]" + text +"\n")
        u=input("Press y to continue or n to stop:")
        continue
    f.close()

elif user_input == 2:
    print(f"You have selected to {Operation_list[user_input]}")
    print(client_name[client_list]+"-"+condition_list[client_input]+" REPORT")
    f = open(client_name[client_list]+"_"+condition_list[client_input]+".txt","rt")
    conents=f.readlines()
    for line in conents:
        print(line,end=" ")
    f.close()
else:
    print("Invalid input !!!")

'''
    # raw_input=input()
    # with open (client_name[client_list]+"_" + condition_list[client_input], "a") as op:
    #     op.write(str([getdate()])+raw_input+"\n")
    # op.close()




#Upload on github
'''
#A function to show the recent time.
def getdate():
    import datetime
    return datetime.datetime.now()

#Dictionary of client.
client_list={1:"Mohan",2:"Rajan",3:"Lathor"}
#Instructor recommended list.
recommended_list={1:"Diet",2:"Exercise"}
#To log or retrieve option.
log_or_retrieve={1:"log",2:"retrieve"}

#Client dictionary process-
print()
print("Please select one of the client:")
for key,value in client_list.items():
    print(f"Press {key} for {value}")
try:
    client_name=int(input("Enter here:"))

    if client_name == 1 or client_name == 2 or client_name == 3:
        print(f"You have selected to {client_list[client_name]}")

    #Instructor recommended dictionary process-
    print()
    print("Please select the recommended option:")
    for key,value in recommended_list.items():
        print(f"Press {key} for {value}")
    recommended_name=int(input("Enter here:"))
    if recommended_name == 1 or recommended_name == 2:
        print(f"You have selected to {recommended_list[recommended_name]}")


    print()
    print("sir/Ma'am what you want to do [log or retrieve] :")
    for key,value in log_or_retrieve.items():
        print(f"Press {key} for {value}")
    log_or_retrieve_input=int(input("Enter here:"))


    if log_or_retrieve_input == 1:
        print("You have selected to log:")
        print("Generating: "+client_list[client_name]+"_"+recommended_list[recommended_name]+" type schedule:")
        file=open(client_list[client_name]+"_"+recommended_list[recommended_name]+".txt","a")
        repeat="y"
        while repeat not in "n":
            input_txt=input(f"Enter the recommended to do {recommended_list[recommended_name]}:")
            file.write("["+str(getdate())+"]" + input_txt + "\n")
            repeat=input("Press y to continue or n to stop:")
            continue
        file.close()


    elif log_or_retrieve_input == 2:
        print("You have selected to retrieve:")
        print(client_list[client_name]+"_"+recommended_list[recommended_name]+" Report:")
        file=open(client_list[client_name]+"_"+recommended_list[recommended_name]+".txt","rt")
        contant=file.readlines()
        for line in contant:
            print(line,end="")
        file.close()
    else:
        print("Please put the correct number to proceed")
except:
    print("[You are not allow to give these option see above you have type wrong input..]")
'''

