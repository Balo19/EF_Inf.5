print("Dezimal 2 Binary")
#Get the number
numb= input("Which number do u want converted")
#change t an intn
integer_numb=int(numb)

number = integer_numb
liste = []
#Algorithm
while number > 0:
    rest = number % 2
    number = number // 2
    liste.insert(0,rest)

    print (number, rest)

#generate output
output = ''
for i in liste:
    output += str(i)

print(output)