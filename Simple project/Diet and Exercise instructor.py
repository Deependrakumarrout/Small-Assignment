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

    #Option for log or retrieve
    print()
    print("sir/Ma'am what you want to do [log or retrieve] :")
    for key,value in log_or_retrieve.items():
        print(f"Press {key} for {value}")
    log_or_retrieve_input=int(input("Enter here:"))

    #if User select log then it will create a new file for that.
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

    #if retrieve then it will show what the instructor gave the advice to client.
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


class Library:

    def __init__(self,list_of_books,library_name):
        self.list_of_books=list_of_books
        self.library_name=library_name
        self.lend_dict={}


    def display_book(self):
        print("These are the list of books available in our library:")
        for book in self.list_of_books:
            print(book)

    def lend_books(self,book,user):
        if book in self.list_of_books:
            if book not in self.lend_dict.keys():
                self.lend_dict.update({book:user})
                print("Successfully lend..")
            else:
                print(f"Sorry it is lend by {self.lend_dict[book]}")
        else:
            print("Sorry this kind of books we don't sell.")

    def add_books(self,book):
        self.list_of_books.append(book)

    def return_book(self,book):
        self.lend_dict.pop(book)
        print("Thanks for returning")


if __name__ == '__main__':
    Decode=Library(["Study Junction","Vinayak","ClassMate","BatchMath","Robbin","Strderio","Study Function","Neural Network",
                                                "Surviover","Lengend Story"],"Deename")

    while True:
        print(f"Welcome of {Decode.library_name} Library")
        list_of_option={1:"display_books",2:"lend_books",3:"Add_books",4:"return_books"}
        for key,value in list_of_option.items():
            print(f"Press {key} for {value}")
        user_input =int(input("Enter you choice:"))
        print()
        if user_input == 1:
            Decode.display_book()
            print()
        elif user_input == 2:
            book_name=input("Please enter the name of the book:")
            user_name=input("Enter your name:")
            Decode.lend_books(book_name,user_name)
            print()
        elif user_input ==3:
            book_name=input("Enter the name of the book that you want to add:")
            Decode.add_books(book_name)
            print()
        elif user_input == 4:
            book_name=input("Enter the name of the book that you want to return book:")
            Decode.return_book(book_name)
            print()
        else:
            print("Please insert a valid number")

        user_start=""
        while user_start != "y" and user_start != "n":
            user_start=input("Enter y to continue or n to stop:")
            if user_start == "n":
                exit()
            elif user_start == "y":
                continue
