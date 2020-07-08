
#A folder path is given and we will take that folder path as input.
#Create a function and that function will take string input as path it will see all the file of the folder.
#Along this take input as dictionary file - and in that file it will contain some word that we will not change anything.
#Another thing will be as input is one file format like jpg.

#def silder("c://","hello.txt","jpg"):

#
# import os
# #os.mkdir("code_pro")
# for i in range(10):
#     f=open(f"abc.jpg_{i}","a")
#     f.close()
# os.listdir("C:/Users/user/.PyCharmCE2019.1/config/scratches/code_pro")

'''
import os
def soilder(path,file,formate):
    os.chdir(path)
    i=1
    files=os.listdir(path)

    with open (file) as q:
        file_list=q.read().split("\n")

    for file in files:
        if file not in file_list:
            os.rename(file,file.capitalize())

        if os.path.splitext(file)[1]==formate:
            os.rename(file,f"{i} {formate}")
            i+=1
soilder("C:/Users/user/.PyCharmCE2019.1/config/scratches/code_pro","dart.txt",".jpg")
'''

'''
import os
def soilder(path,file,format):
    os.chdir(path)
    i=1
    files=os.listdir(path)

    with open (file) as d:
        file_list=d.read().split("\n")

    for file in files:
        if file not in file_list:
            os.rename(file,file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file,f"{i} {format}")
            i+=1
'''
#soilder()



import os
def soilder(path,file,formate):
    os.chdir(path)
    files=os.listdir(path)

    i=1
    with open (file) as op:
        f=op.read().split("\n")

    for file in files:
        if file not in f:
            os.rename(file,file.capitalize())

        if os.path.splitext(file)[1]==formate:
            os.rename(file,f"{i} {formate}")
            i+=1

user_path=input("Enter the path:")
file_name=input("Enter the name of the file:")
formate=input("Enter the format:")
soilder(user_path,file_name,formate)


#user_input=(input("Enter a decimal number:"))
binary=["000","001","010","011","100","101","110","111"]
j=0
while(j<8):
    for i in binary:
        print(i,j)
        j+=1














