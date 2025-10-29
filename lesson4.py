# Библиотека math
import math as mt # можно просто: import math
#num1 = 5.45
#num2 = 5.99
#print(mt.ceil(num1)) #ceil - округление вверх
#print(mt.floor(num2)) #floor - округление вниз

# Radians and degrees
#import math as mt
#num1 = mt.radians(30)
#num2 = mt.degrees(mt.ceil(0.5235987755982988))
#print(num1)
#print(num2)

# Степени
#num1 = mt.pow(2, 4)
#num2 = mt.sqrt(16)
#print(num1)
#print(num2)

# max and min
#list = [876, 86, 8765]
#print(max(list))
#print(max(654, 756, 5, 8))
#print(min(67, -786, -8765))

#l = float(input("l "))
#w = float(input("w "))
#r = float(input("r "))
#h = float(input("h "))
#v1 = l*w*h
#v2 = ((mt.pi*r**2*h)/3)
#v3 = mt.pi*r**2*h
#v4 = (4*(mt.pi*r**3)/3)
#print(f" v1 = {v1}, v2 =  {v2}, v3 = {v3}, v4 = {v4}")

#numbers = [1, 2, 3, 4 ,5]
#people = ['Tom', 'Sam', 'Freak']
#name_list = people[1]*10
#print(name_list)

#student1 = ['Tom', 'phone', True, 2000, 'bank']
#name_list = (student1[0])*10
#price_list = (student1[3])*10
#student1[-2] = 3000
#print(len(student1))
#print(name_list)
#print(price_list)

#people = ['Tom', 'Sara', 'John', 'Ami', 'Sam']
#people.append("Bob")
#slice_people = people[1:4]
#people[4:] = people[0:2]
#print(slice_people)
#print(people)

#people.insert(2, 'Alex')
#print(people)

#people = ['Tom', 'Sara', 'John', 'Ami', 'Sam']
#people1 = ['Alex', 'Eve', 'Jack']
#people.extend(people1)
#print(people)
#people.remove('Jack')
#print(people)
#people1.clear()
#print(people1)
#eve_index = people.index('Eve')
#people[eve_index] = 'Eleanor'
#print(people)

#people = ['aaa', 'bbb', 'ccc', 'ddd']
#slice_people = people[-2::-1]
#print(slice_people)

# Bool
#num1 = 2 > 1
#num2 = 1 == 3
#num3 = num1 != num2
#print(num3)
#a = num1 + num2
#print(a)

#num1 = 4
#num2 = 5
#print(num1<=num2)
#print(num1>=num2)

#age = int(input("Enter your age: "))
#a = age % 10 == 0 or age >= 50
#print(a)


#person = input("status of the person: ")
#if person == 'student' or person == 'school 10th' or person == 'school 11th':
 #   print(f"{person} is 15 or older")   
#elif person == 'working':
 #   print(f'{person} has a job')    
#else:
#    print(f'{person} is younger than 15')


age = int(input("Enter your age:"))
try:
   age = int(age)
except:    
   print("enter your age correctly")
if age < 18:        
     print('child')
elif 18>=age>35:
   print('adult')
elif 35>=age>60:
   print('old') 
else:
  print('pensioner')


#list1 = [2, 3, 4, 5]
#list1.append('Sacha')
#if 'Sacha'  not in list1:
#    print('no')
#else:
#    print('yes')

#name = 'today is rainy'
#if 'rainy' in name:
 #   print('you need to take an umbrella') 
 
 

 
