print("Hello World")

name="ABCD"
age=30

name="esther"
age=20.6

is_correct=True

x=2+3j
print(name)
print(x)

lists=[1,2,3]
tuples=(1,4,5)
sets={1,5,6,7}
disct={"name":"esther","age":"20.6"}

a=input("Enter your name:")
print("Hello" + a)

b=input("Enter your birth year: ")
c=int(b)+2
print(c)

#esther
#True,False,None,or,not,if,else,elif,for,while

import keyword
print(keyword.kwlist)

x=int(input("Enter first number: "))
y=int(input("Enter second number: "))

sum=x+y
print(sum)

name="ESTHer"
print(name.lower())
print(name.upper())
print(name.find("r"))
print(name.replace("r","R"))
print("e" in name)
print(5//2)
print(2>6)

print(2>3 and 4>3 )
birth_year=2000
if birth_year>2000:
   print("new generation")
elif birth_year==2000:
    print("middle generation")
else:
    print("old generation")

i=0
while i<100:
    print(i)
     #i+=1

for i in range(101):
    print(i)

age=[10,12,23,30,45,29]
print(age[0:5])
age.append(50)
age.insert(1,30)
print(len(age))
for ages in age:
    if ages==23:
        continue
    print(ages)

age=(10,23,45,45,45,45,45)
print(age.count(45))
print(age.index(45))
def greet():
    print("hello")
greet()