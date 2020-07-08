
#Basice calculator
'''num_1=int(input("Enter the first number:"))
op=input("Enter a operator:")
num_2=int(input("Enter the second number:"))

if op=='+':
    print(num_1+num_2)
elif op=='-':
    print(num_1-num_2)
elif op=='*':
    print(num_1*num_2)
elif op=='/':
    print(num_1/num_2)
else:
    print("Invalid input number..")'''

#Gassing game

'''password='25iwritecode'
Guess=input("Guess a password:")

if Guess== password:
    print("Logging in...")
else:
    print("incorrect password")'''

#Guess
'''staff_name='Ragav'
guess=" "
while guess != staff_name:
    guess=input("What is the name of the staff:")
    if guess != staff_name:
         guess
    else:

        print("Oo i see he is working well...")'''

#Buliding a guess game:

'''password='default code'
guess=" "
guess_limit=3
start_count=1
end_of_guess=False


while guess != password and not end_of_guess:
    if start_count <=guess_limit:
        guess=input("Please Enter your password:")
        start_count+=1
    else:
        end_of_guess=True
if end_of_guess:
    print("You have insert maximum time incorrect password\n"
          "please wait for 5 min we are fetching out.")
else:
    print("Logging you in...")'''

'''
#A dictornay of year
def main():
    var=''
    start_count=1

    month_year={'jan':'janauary',
                'feb':'febuary',
                'mar':'march',
                'apr':'april',
                'may':'may',
                'jun':'june',
                'jul':'july',
                'agu':'aguest',
                'sept':'september',
                'oct':'october',
                'nov':'november',
                'dec':'december',
                    }
    try:
        print(month_year[input("Enter a any year:" )])
        while var != month_year :
            if start_count<7:
                print(month_year[input("Enter a any year:""")])
                start_count += 1
            else:
                print("You can't able to type in..")
    except:
            print("invalid input")
            var=input("Do you want to restart the game:")
            if var=='yes'.lower():
                print("restaring")
                main()
            elif var=='no'.lower():
                print("player don't want to restart it..")
            else:
                print("Invalid input")
main()
'''


#print(month_year["jan"])
#An example

'''C1='Jamil'
C2="Ranger"
Jamil= input(str(C1)+ " Enter your strength:")
print(C1,"Enter your strength:",Jamil)
Falli=input(str(C2)+" Enter your skill:")
print(C2," Enter your skill:",Falli)'''





'''def main():
    while True:
        var=input("Enter anything:").lower()
        if var=='yes':
            print("restarting")
main()'''


var=input("Up_to how many number of table you want type here:")
var=int(var)
for j in range(1,var+1):
    for i in range(10+1):
        print(end=" ")
        print(j,"x",i,"=",i*j)


#Or we can write like this -
num=int(input("Enter a number:"))
for i in range(1,num+1):
    for j in range(1,11):
        print(end=" ")
        print(f"{i} * {j} = {i * j}")


# num=int(input("Enter over here:"))
# for i in range(1,11):
#     print(num,"x",i,"=",num*i)

