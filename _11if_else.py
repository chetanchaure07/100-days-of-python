#it is used to make decision in your program.
#it helps the computer choose what to do based on conditions.
#if something is true - to this 
#otherwise do something else

#check the no is +,-,or zero
a = int(input("Enter a number (positive, negative or zero): "))
if a > 0:
    print("Your number is positive")
elif a < 0:
    print("Your number is negative")
else:
    print("Your number is zero")



#check person is eligible to vote
b = int(input("Enter Your Age: "))
if b >= 18:
    print("You are eligible for vote: ")
else:
    print("Your are not eligible, \"right now\"")
    print("Wait for your 18th birthday")




#print two number and check which is greater
c = int(input("Enter your first number: "))
d = int(input("Enter your second number: "))
if c > d:
    print(f"{c} is greater then {d}")
else:
    print(f"{d} is greater then {c}")


#take input and give the grade.
# (I want to take it an advance calculate all the marks of 10th class and then create there result)
e = int(input("Enter your mark of \"Hindi\" subject: "))
f = int(input("Enter your mark of \"English\" subject: "))
g = int(input("Enter your mark of \"Maths\" subject: "))
h = int(input("Enter your mark of \"social science\" subject: "))
i = int(input("Enter your mark of \"science\" subject: "))
j = int(input("Enter your mark of \"sanskrit\" subject: "))

total_marks =  (e + f + g + h + i + j) / 6

attandance = int(input("Enter your attandace: "))


print(f"You got {total_marks}%")
if attandance >= 75:
    if total_marks > 95:
        print("A+")
        print("Congratulation")
    elif total_marks >= 75 :
        print("A")
    elif total_marks >= 60:
        print("B")
    elif total_marks >= 45:
        print("C")
    elif total_marks >= 33:
        print("D")
    else:
        print("You Are Fail In This Year!")
else:
    print("Fail(Low attandance)!")


#check if number is divisible by both 2 & 3
k = int(input("Enter the number(check the number is divide with 2 & 3)"))
if ( k % 2 == 0) and ( k % 3 == 0):
    print("The number is divisible with 2 & 3")
else: 
    print("The number is not divisible with 2 & 3")


#leap year cheack
l = int(input("Enter year (eg. 2024)"))
if (l % 4) == 0:
    if (l % 100) == 0:
        if (l % 400) == 0:
            print(f"{l} is leap year")
        else:
            print(f"{l} is not leap year")
    else:
        print(f"{l} is leap year")
else:
        print(f"{l} is not leap year")


#Largest of Three Numbers
m = int(input("Enter the number: "))
n = int(input("Enter the number: "))
o = int(input("Enter the number: "))
if (m > n) and (m > o):
    print("m is greater number")
elif (n > m) and (n > o):
    print("n is greater number")
else:
    print("o is greater number")


#Character Check Input a single character and check whether it is a vowel, consonant, digit, or special symbol.
p = input("press any one button from keyboard: ")
if p.isalpha():
    if p in 'aeiouAEIOU':
        print(f"{p} is vowel")
    else:
        print(f"{p} is consonent")
elif p.isdigit():
    print(f"{p} is digit")
else:
    print(f"{p} is special character")


# Odd-Even and Multiple of 3
q = int(input("Enter the number: "))
if (q % 2) == 0:
    type_num = "even"
else:
    type_num = "odd"
if (q % 3) == 0:
    multi3 = "multiple of 3"
else:
    multi3 = "not multiple of 3"

print(f"its {type_num} and {multi3}")


# Electricity Bill Calculation Based on units consumed:
r = int(input("Enter the electricity(in unit): "))
if r <= 100:
    print(f"For {r} units, total payable amount is ₹{r * 5}.")
elif r <= 200:
    print(f"For {r} units, total payable amount is ₹{r * 7}.")
else:
    print(f"For {r} units, total payable amount is ₹{r * 10}.")


# login system
username = "admin"
password = 1234

user_name = input("Enter your username: ")
pass_word = input("Enter your password: ")

if username == user_name:
    if password == pass_word:
        print("log in successfully")
    else:
        print("password error (3 chance left!)")


# Triangle Problem
s = int(input("Enter first side of triangle: "))
t = int(input("Enter second side of triangle: "))
u = int(input("Enter third side of triangle: "))
if (s + t) > u and (t + u) > s and (u + s) > t:
    if ( s == t == u ):
        print("Equilateral triangle")
    elif ( s == t or t == u or u == s):
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("These are not the triangle sides")


