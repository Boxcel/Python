#Warning, this code will be ugly, horrible, and barely relate to itself, this is a warning for my and everyones sanity, Best regards, Boxcel.
#All code was written as practice from BroCodes python tutorial.
#This is my pycharm notes section, as I use this IDE I will leave notes as to shortcuts and things I've learned myself about it.
#
#WARNING, THIS CODE RUNS EXTREMLY SLOW DUE TO ALL OF IT BEING CLUMPED!

print("Hello World!")

#Variable section.
print("") #This is only a blank space.
First_name = "Boxcel" #A string variable.
Last_name = "Gutto" #Use underscores for spaces in variables, it's nice to the eyes unlike this code.
Full_name = First_name +" "+Last_name #These two variables were combined to make a whole new one.
print("Hello " +Full_name)
print(type(Full_name)) #This will print the data type to the terminal.

age = 18 #This is a int data type, int's are whole numbers, always whole numbers.
#age = age + 1, This will add 1 to "age" base number.
age += 1 #This is a shorter way to do Line 16
print(age)
print("Your age is: "+str(age))#This allowed the int data type to happen along a str, this is only possible due to str().
print(type(age)) #Will print a int data type into terminal.
height = 6.5 # Floats unlike int's hold decimal points.
print("Your height is: "+str(height)+"ft")
print(type(height)) # This will print the float data type.

human = True #This is a boolean variable, it stands for true or false, I chose true but false can also work.
print(human)
print("Are you a human?: "+str(human))
print(type(human))#This will print the boolean data type.

#Multiple assignments section.
print("")
Name, Age, Looks = "Box", 20, True #Str, int, boolean.
A = B = C = D = 30 #If all have the same variabe, this is how to list them.
print(A, B, C, D)

#String methods section.
print("")
Nombre = "Boxx"
print(len(Nombre)) #This will print the length of our name variable (length = len).
print(Nombre.find("B")) #This will find the selected index (In our case B).
print(Nombre.capitalize()) #This will capitalize the first letter in your string.
print(Nombre.upper()) #This will make all letters uppercase.
print(Nombre.lower()) #This will lower all letters.
print(Nombre.isdigit()) #This will return true or false, if numbers are detected = true, if numbers arent detected = false.
print(Nombre.isalpha()) #This will check to see if before .isalpha are letters (Nombre = Boxx = true for .isalpha)
print(Nombre.count("o")) #This will count how many of selected char is in your str.
print(Nombre.replace("B","C")) #This will replace selected char, with other selected char.
print(Nombre*3) #This will just display your str by whatever multiple you selected.

#Type Casting section.
print("")
x = 1 #int
y = 2.0 #float
z = "3" #str

x = float(x) #This becomes a perm shift.
y = str(y) #This becomes a perm shift.
z = int(z) #This becomes a perm shift.

print(x)
print(y)
print(z)

#User Input Section.
print("")
navn = input("What is your name?: ")
alder = int(input("How old are you?: ")) #This is how to get a number user input to work.
høyde = float(input("How tall are you?")) #This is how we get a decimal input.
alder += 1
print("Hello " +navn) #Whenever we accept user input it is of the str data type.
print("You are "+str(alder) +" years old.") #This will allow for you to display the number
print("You are "+str(høyde)+"ft tall")

#Math section.
import math
print("")
pi = 3.14
x = 10
y = 50
z = 100

print(round(pi)) #This will round the selected value or variable.
print(math.ceil(pi)) #This will round the selected value or variable up to the nearest whole int.
print(math.floor(pi)) #This will round the selected value or varible down to the nearest whole int.
print(abs(pi)) #This will give you the absolute value of selected value or variable.
print(pow(pi,9)) #This will raise to the selected power.
print(math.sqrt(pi)) #This will give you the square root.
print(max(x,y,z)) #This will find the largest value of selected values.
print(min(x,y,x)) #This will find the lowest value of selected values.

#
print("")
