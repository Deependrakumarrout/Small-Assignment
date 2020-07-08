print()
Math=int(input("Enter the mark you score in Maths:"))
Phy=int(input("Enter the mark you score in Physics:"))
Chem=int(input("Enter the mark you score in Chemistry:"))
Hindi=int(input("Enter the mark you score in Hindi:"))
IT=int(input("Enter the mark you score in Information Technology:"))
Bio=int(input("Enter the mark you score in Biology:"))

total=Math+Phy+Chem+Hindi+IT+Bio
percentage=(total/600)*100
print("\nThe total mark that the student score:",float(total))
print("The percentage that the student obtained:",float(percentage))

if percentage>60:
    print("\nGRADE A")
elif percentage>50:
    print("\nGRADE B")
elif percentage>40:
    print("\nGRADE C")
else:
    print("\nFAIL")
