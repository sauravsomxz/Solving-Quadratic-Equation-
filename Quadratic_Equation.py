# Author : Saurav Ranjan Maharana
# Date : 23rd November, 2019
# Purpose : Learning Py!
# Contact : saurav.maharana07@gmail.com
# Title : Solving Quadratic Equation using Py!
# ax^2 + bx + c = 0 :Form
# Formulae : X = (-b +/- (b^2.4a*c) ** 0.5)/2*a
import math
def my_quad():
    print("")
    #Taking input of 'a', 'b' anc 'c'
    a = float(input("Enter value of a : ")) 
    b = float(input("Enter value of b : "))
    c = float(input("Enter value of c : "))
    print("----------------------------------------")
    #Display as form of ax^2 + bx + c = 0 
    term_1 = print("First Term is : " , + a,  "x2") 
    term_2 = print("Second Term is : " , + b,  "x")
    term_3 = print("Third Term is : ", c)
    print("Form is : ", a, "x2", "+", b, "x" "+", c, "= 0")   
    #Calculate X; where x1 = root 1 and x2 = root 2.
    #print(form) 
    print("----------------------------------------")
    while(a==0 or b==0 or c==0):
        print("Not Possible")
        break
    while a!=0 and b!=0 and c!=0:
        x1 = (-b-(b**2 - 4*a*c)**0.5)/2*a #if Input is a(1),b(1),c(1) then by PEDMAS rule, answer will be 0.75 #{[]{()}}
        print("First Root is ", round(x1,2))
        x2 = (-b+(b**2 - 4*a*c)**0.5)/2*a
        print("Second Root is : ", round(x2,2))
        break
    try_again = input("Do you want to continue ? (Y/N): ")
    if try_again[0] == "Y" or try_again[0] == "y":
        my_quad()
    elif try_again == "N" or try_again == "n":
        print("Thanks for using! (:")
status = input("Start ? (Y/N): ")
if status[0] == "Y" or status[0] == "y":
    my_quad()
else:
    print("Thanks for using! (:")
