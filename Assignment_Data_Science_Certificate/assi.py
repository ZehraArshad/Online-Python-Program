## Task 1 

# age = 23
# name = 'Zehra'
# is_student=False

# print(age+25)
# print(name+' '+'Smith')
# print(not is_student)

## -------------------------------------------

## Task 2

# width = 5.5
# height = 3.25
# area=width*height
# print(area)

# Temp=int(input('Enter temperature in Celcius '))
# Fahrenheit = (Temp*(9/5))+32
# print(Fahrenheit)


# Radius = int(input('Enter radius: '))
# Unit = (input('Enter the unit of radius: '))
# Area = 3.14159*(Radius**2)
# print(str(Area) + Unit+"\u00b2") 

## -------------------------------------------

## Task 3

# list_fruits = ["apple","banana","cherry","date", "strawberry","fig","grape"]
# list_fruits.pop(0)

# # sometimes, we might not know the index to last element

# list_fruits.pop(len(list_fruits)-1)
# print('list after popping ')
# print(list_fruits)

# list_2_fruits = ["kiwi","lemon","mango"]
# list_fruits[2:5]=list_2_fruits
# print(list_fruits)



## -------------------------------------------

## Task 4

# capitals ={'USA':'Washington D.C.','France':'Paris','Japan':'Tokyo'}
# print(capitals) 

# capitals['Germany']='Berlin'
# print(capitals)

# if 'France' in capitals:
#     print('France is present')
# else:
#     print('France is not present')


## -------------------------------------------

## Task 5

# number = int(input('Enter a number '))
# if number>0:
#     print('The number is positive')
#     if number%2==0:
#         print('It is an even number')
#     else:
#         print("An odd number")
# else:
#     print('The number is negative')


# student_age = 20
# cgpa = 2.9
# if student_age>=18 and (cgpa>=3.0 and cgpa<4.0):
#     print('Eligible for admission')
# else:
#     print("Not eligible for admission")


## -------------------------------------------
## Task 6

# sentence = "Python programming is fun and powerful!"
# print(sentence.upper())
# x = sentence.replace('fun', 'exciting')
# print(x)
# word = 'python' 
# if word in sentence.lower():
#     print('It contains')
# else:
#     print("It is not present")
# print(sentence.rstrip('!').split()[-1])
# print(sentence.replace('programming ', ''))



email = 'user@example.com'
print(email.split('@'))
## this splitting will always have 2 elements
print('part before @ '+ email.split('@')[0])
print('part after the @ '+email.split('@')[-1])

email_lst = email.split('@')
service = email_lst[-1].split('.')[-2]
if 'example' in service.lower():
    print("we have this service ("+ service.lower()+")")
else:
    print("We don't have that service")



