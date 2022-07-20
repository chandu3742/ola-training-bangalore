
#armstrong using oop concept
class math :
    def __init__(self, number):
        self.number= number

    def armstrong(self,number):
        temp=self.number
        result=0
        while(temp!=0):
            rem = temp% 10
            result +=rem**3
            temp//=10
        if self.number ==result :
            print(self.number," is armstrong number")
        else :
            print(self.number," is not armstrong number")

number=156
check=math(number)

check.armstrong(number)


#creating 3 functions
# function sum
def sum(a,b):
    print(a+b)
#function1 prime
def prime(a):
    for i in range(2,a):
        if(a%i==0):
           print(False)
    print(True)
#function2 multiply
def multiply (a,b):
    print(a*b)
# main.py
from function import sum as s
from function1 import prime as p 
from function2 import multiply as m

s.sum(6,7) 
p.prime(7) 
m.multiply(6,7)