#text = 'Hello, my name is Sam'
#list = [2, 4, 64, 6, 'name']
#search = 'name'
#if search in text:
#    print(f'{search} is in text')
#else:
#    print(f'{search} is not in text')
#if search in list:
#    print(f'{search} is in list')
#else:
#    print(f'{search} is not in list')


#num = int(input('enter a number: '))
#if num % 2 == 0:
#   print('четное')
#else:
#    print('нечетное')

#a =input('enter a. umber: ')
#try:
#    if int(a) > 0:
#        print('Число А является положительным')
#    else:
#        print('число А не является положительным')
#except:
#    print('введите число')
#finally:
#    print('блок try завершен')

#a = input('enter a number: ')
#try:
#    if int(a) % 2 == 0:
#        print(f'{a} is even')
#    else:
#        print(f"{a} is not even")
#except:
#    print('enter a NUMBER')
#finally:
#    b = int(input("enter a number in a correct form: "))
#    if b % 2 == 0:
#        print(f'{b} is even')
#    else:
#        print(f'{b} is not even')


#a = int(input('enter a number: '))
#if a % 2 == 0 and 10 <= a <= 99:
#    print(f'{a} целое положительноке двузначное число')
#else:
#    print(f"{a} либо не целое, либо не положительное, либо не то, не другое") 


# a = 'gvhb'
# b = 'hbvcxcvb'
# print(a+b)

# list = ['apple', 'banana', 'milk']
# word = 'milk'
# if word in list:
#     new_world = word.replace("k", "ch")
#     print(new_world)

# text = 'aTAI'
# new_text = text.swapcase()
# print(new_text)


# text = '   Atai wants to eat pizza '
# new_text = text.strip()
# print(new_text)

# text = 'gbjmm, hgfcfvbgh vf. '
# new_text = text.split()
# print(new_text)

# word = 'kjbvcdxdfgvbhjn'
# print(len(word))

#Task1
# a = '32'
# b = '3.5'
# x = 'True'

#Task2
#text = 'Hello, my friend'

#Task3
# name = input('Write your name: ')
# surname = input('Write your name: ')
# print(f"Hello, {name} {surname}")

#Task 4
# name = input('Write your name: ')
# surname = input('Write your name: ') 
# res = name + f" {surname}"
# print(res)

#Task5
# name = input('enter your name: ')
# score = int(input('enter your score: '))
# print(f'Hello, {name}! Your score is {score}')

#Task6
name = input('enter your name: ')
age = int(input('enter your age: '))
text1 = 'Меня зовут'
text2 = ', и мне'
text3 = 'лет'
final_text = text1+ f' {name}'+text2+f' {str(age)}'+f' {text3}'
print(final_text)