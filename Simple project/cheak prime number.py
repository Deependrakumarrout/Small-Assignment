
#Making a function to restart

def restart():
    try:
        num=int(input("Enter a number:"))

        if num>1:
            for i in range (2,num):
                if (num%i)==0:
                    print(num,"is not a prime number..")
                    print(i,"x",num//i,"is",num)
                    break
            else:
                print(num,"is a prime number")

        else:
            print(num,"is not a prime number")
    except:
        print("You have insert a invalid value..")

    data=" "
    while data != 'yes' or 'no':
        data = str(input("Do you want to restart again:"))
        if data=='yes'.lower():

            print("processing..")

            restart()
            break


        elif data=="no".lower():
            print("Dont want to do restart")
            break
        else:
            print("Invalid input")

restart()

#Simple prime program

'''num=int(input("Enter a number to detect prime:"))
if num>=1:
    for i in range (2,num):
        if (num%i)==0:
            print(num,"is not a prime number")
            print(i,"x",num//i,"is",num)
            break
    else:
        print(num,"is a prime number")

else:
    print(num,"is not a prime number")'''



#A even or odd number
'''num=int(input("Enter a number:"))
if num%2:
    print(num,"its a odd number")
else:
    print(num,"is a even number")'''


'''t=(5,'program',1+3)
print("t[1]=",t[0])
print("t[0:3]=",t[0:3])'''



#finding prime number
'''while True:

    num=input("Enter a number to find the prime to not:")


    if num!='q' and num>=str('1'):
        num = int(num)
        for i in range(2,num):


            if (num%i)==0:
                print(num,'is not a prime number')
                print(i,'x',num//i,'is',num)
                break
        else:
            print(num,'is a prime number')

    else:
        print("User want to stop the program\n\n")
        break'''



# Explain the prime number
#we will take 1 which is not a prime number in if statement
#for to repete it to cheak the number which is divisiable by 2,num
#And then the number to put the reminder by giving the (%) opeator to get the reminder
#if it get 0 then it will display is not a prime number
#or if it wil show the 1 of which will be the prime number
#break

'''

num1=int(input("Enter a number:"))
if num1>1:
    for i in range(2,num1):
        if (num1%i)==0:
            print(num1,"is not a prime number")
            print(i,'x',num1//i,'=',num1)
            break

    else:
        print(num1,'is a prime number')
else:
    print(num1,'is not a prime number')

'''
