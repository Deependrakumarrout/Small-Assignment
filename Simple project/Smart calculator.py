#Smart calculator

console=["Smart then smarter follow as on insta","My name is Alex",
         "You can give me instruction to calculate","sorry i can't able to recognize your word.."]

def extract_text(text):
    l=[]
    for t in text.split(" "):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def lcm(a,b):
    l=a if a>b else b
    while l<=a*b:
        if  l%a==0 and l%b==0:
            return l
        l+=1

def hcf(a,b):
    h=a if a<b else b
    while h>=1:
        if a%h==0 and b%h==0:
            return h
        h-=1

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mod(a,b):
    return a%b

def div(a,b):
    return a/b

def mult(a,b):
    return a*b

def name():
    print(console[1])
def end():
    exit()

def sorry():
    print(console[3])

command={"add":add,"sum":add,"addition":add,"plus":add,"sub":sub,"subtract":add,
         "minus":sub,"hcf":hcf,"lcm":lcm,"div":div,"division":div,"divide":div,"multiplication":mult,
         "multi":mult,"mod":mod}
token={"name":name,"end":end,"exit":end,"stop":end}

print("-----------"+console[0]+"----------------")
print("-----------"+console[2]+"----------------")

print("")
print("Hii")
print("I can do addition")
print("I can do multiplication")
print("I can do subtraction")
print("I can do division")
print("I can do Lcm")
print("I can do Hcf")
print("I can do name")
print("You can ask me in shortcut word but related to math only..")


def restart():
    print()
    awer=1
    print("You can enter only 3 times...")
    while awer<=3:
        text = input("Enter any quires related to math: ")
        for word in text.split(" "):
            if word.lower() in command.keys():
                try:
                    l=extract_text(text)
                    w=command[word.lower()] (l[0],l[1])
                    print(w)
                    awer += 1
                except:
                    print("Its not going to change please reenter it..")
                finally:
                    break
            elif word.lower() in token.keys():
                token[word.lower()]()
                break
        else:
            sorry()
    prt=input("do you want to restart press Y/N:")
    if prt=='y'.lower():
        restart()
    else:
        print("User want to stop..")
restart()


#A project to create a smart calculator
#what it will do?
#It will detect the things that can be in the form of text as well as number
#so ones the user will write on to it then it will get the correct output ok.

#How to do?
#Implement of list to call by these address.
#First user defined instruction to give the seperated by it.
#Then using of function to get all caculation.
#User input
#Implementing what it will generate in that form by which the user get to insert
#if not then other thing
#Then one more add to get restart.



#This is what how split function work
'''
de="hi,i,have,42,43,23,24"
print(de)

l=de.split(",")
print(l)

#The is for join function is for joining only and nothing else.
j=' joining '.join(l)
print(j)
cbz=','.join(l)
print(cbz)
'''


#smart calculator
'''
response=["Smart then smarter follow as on instagram","My name is furyo",
          "Welcome to newland calculator","sorry i can recognize your word..."]

def extract_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def hcf(a,b):
    h=a if a<b else b
        while h>=1:
            if a%h==0 and b%h==0:
                return h
            h-=1

def hcf(a,b):
    h=a if a<b else b
    while h>=1:
        if a%h==0 and b%h==0:
            return h
        h-=1

def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

def lcm(a,b):
    l=a if a>b else b
    while l<=a*b:
        if l%a==0 and l%b==0:
            return l
        l+=1

def mod(a,b):
    return a%b

def mult(a,b):
    return a*b

def myname():
    print(response[1])

def sorry():
    print(response[3])

formula={"sum":sum,"add":sum,"addition":sum,"plus":sum,"sub":sub,
        "subtraction":sub,"minus":sub,"div":div,"division":div,
         "mod":mod,"modular":mod,"multi":mult,"multiplication":mult,"into":mult,"lcm":lcm}

command={"name":myname}

print("------------"+response[0]+"---------------")
print("-------------"+response[2]+"---------------")


while True:
    print()
    text=input("Enter your enquary:")
    for word in text.split(' '):
        if word.lower() in formula.keys():
            try:
                l=extract_text(text)
                t=formula[word.lower()] (l[0],l[1])
                print(t)


            except:
                print("Incorrect input think little bit")
            finally:
                break
        elif word.lower() in command.keys():
            command[word.lower()]()
            break
    else:
        sorry()
'''



'''
talent=["Hello i am smart calculator","My name is Tedy",
        "i can do any thing related to math","Sorry i the text that you have type is not in my dictionary"]

def extract(text):
    l=[]
    for t in text.split(" "):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def name():
    print(talent[1])
def end():
    exit()

def sory():
    print((talent[3]))


dictionary={"add":add,"sum":add,"plus":add,"sub":sub,"minus":sub,"subtraction":sub}
function={"name":name,"end":end,"exit":end,"stop":end}

print("***************"+talent[0]+"******************")
print("##################"+talent[2]+"################")
while 1:
    text=input("Enter your query:")

    for word in text.split(" "):
        if word.lower() in dictionary.keys():
            try:
                l=extract(text)
                r=dictionary[word.lower()] (l[0],l[1])
                print(r)
                break
        #finally:
         #   pass
            except:
                print("hey you are repeting the same number... ")
        elif word.lower() in function.keys():
            function[word.lower()]()
            break
    else:
        sory()



'''
