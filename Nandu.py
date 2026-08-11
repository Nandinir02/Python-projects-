#a=int(input("enter the a value"))
#b=int(input("enter the b value"))
#c=int(input("enter the c value"))
#d=int(input("enter the d value"))
#if(a>b and a>b and a>c):
#    print("a is larges")
#elif(b>a and b>c and b>d):
 #   print("b is largest")
#elif(c>a and c>b and c>d):
#    print("c is largest")
#else:
 #   print("d is largest")


#designation=input("Enter the designation : ")
#if(designation == 'HR'):
  #  print("Welcome HR")
#elif(designation == 'employe'):
 #   print("Welcome empoyee")
#elif(designation == 'teamlead'):
 #   print("Welcome teamlead" )
#else:
 #   print("Welcome manager")


 #indexing
#a="Nandini.R"
# print(a[3])

# #membership
# print('nd' in a)

# #slicing
# print(a[-4])

# #formatting
# print(f"she is {a}")

# #repetation
# print(a *3)

# #nonmembership
# print('sh' in a)

#print(a[2:3:4])''

#upper
# print(a.upper())

# #lower
# print(a.lower())

# #capitalize
# print(a.capitalize())

# #replace
# print(a.replace("Nandini" , 'Nandu'))

# #find
# print(a.find('n'))

# #startswith
# print(a.startswith('Sh'))

# #count
# print(a.count('n'))

# #title
# print(a.title())

# #swapcase
# b=nandiniram
# print(b.swapcase())


# loops
# i=100
# while i<1:
#     print(i)
#     i-=1

# i=1
# while i < 6:
#     print('hello',i)
#     i+=1


# number=[22,78,90,67,88,95,77]
# i=0
# while i<len(number):
#     print(number[i])
#     i+=1

# number=[22,78,90,67,88,95,77]
# i=0
# while i<len(number):
#      print(number[i])
#      if
    
#      i+=1

# x=int(input("Enter the value of x "))
# i=1
# fact=1
# while i<=x:
#     fact = fact * i
#     i+=1
#     print(fact)

# number=[22,78,90,67,88,95,77]
# for num in number:
#   print( "num",number)

# number=[2,4,5,3,8,9,0]
# total=0
# for num in number:
#     total+=num
#     print(total)

# number=[1,4,2,9,6,3,7]
# largest=number[0]
# for num in number:
#     if num > largest:
#         largest=num
# print(largest)

# for i in range (1,101):
#     print(i)

# for i in range (100,0):
#    print(i)


# 
# number =(2,8,9,6,4)
# for i in number:
#     print(i)
  

# 
# numbers=[12,43,56,13,15,9,80]
# x=15
# for i in numbers:
#     if x==numbers [i]:
#        print(numbers(i))
#     break

#APPEND
# x=[30,'nandu',2.233,'8976']
# x.append(33)
# print(x)

#extend
# x=[30,'nandu',2.233,'8976']
# x.extend([7,33])
# print(x)

# pop
# x=[30,'nandu',2.233,'8976']
# x.pop()
# print(x)
 
#  remove
# x=[30,'nandu',2.233,'8976']
# x.remove(30)
# print(x)

# clear
# x=[30,'nandu',2.233,'8976']
# x.clear(30)
# print(x)

# sort
# x=[23,4,2,7,89,40]
# x.sort()
# print(x)

# reverse
# x=[23,4,2,7,89,40]
# x.reverse()
# print(x)

#max
#x=[23,4,2,7,89,40]
#print(max(x))

#descending
# x=[23,4,2,7,89,40]
# x.sort(reverse = True)
# print(x)

#min
#x=[23,4,2,7,89,40]
#print(min(x))

#count
# x=[23,4,2,7,89,40]
# print(x.count(2))

# sum
# x=[23,4,2,7,89,40]
# print(sum(x))


#TUPLE SORT
# x=(1,3,4,5,6,7)
# print(tuple(sorted(x)))

#index
# x=(2,3,6,2,8,4,9)
# print(x.index(4))

#

# x.len()
# print(x.len() arrange with respect to len of name
#       )x=('nandu','bharath','shreshta','ram')


#print a consonents in tuple
# x=('nandu')
# count=0
# vovel=("aeiou")
# for v in x:
#     if v not in vovel:
#         count+=1
# print(count)

#dictionary
# dict={
#        "name":"Nandini",
#       "age":18,
#        "dob":"june29",
#        "studies":{
#                   "edu":"BE",
#                    "college":"sait",
#         }
#   }
#setdefault
#dict.setdefault("year","2007")
#print(dict)

#pop
#dict.pop("college","sait")
#print(dict)

#update
#dict["edu"]:["btech"]
#print(dict)
#dict.update({"edu":"btech"})
#print(dict)
# print(dict.popitem())
# print(dict.keys())
# print(dict.values())


#set
# set={3,5,6,4,7,5,4}
# print(set.pop())
# set={3,5,6,4,7,5,4}
# print(set.clear())


#1.change the value inside the a dict
# dict["edu"]:["btech"]
# print(dict)


#["studies"].update({"year":"2007"})
#print(dict)

#2
#dict.setdefault("studies",{}).update({"college":"BMS"})
#print(dict)

#3
#print(dict["studies"])

#uppercase
# list=['hello','bye','nothing']
# for i in range(len(list)):
#    list[i]=list[i].upper()
# print(list)



# #5
# list=[3,-2,1,2,-3,-5]
# print("the neagtive no")
# count=0
# for i in list:
#     if i<0:
#         print(i)
#         count+=1
# print(count)


#6    


#error
# x=[1,3,4,5,6,9,0]
# for i in x:
#     if i>9:
#      print(i)


#exceptions
# print("hello1")
# print("hello2")
# try:
#     print(1)

# except Exception as err:
#     print(err)
#     print(type(err))

# print("hello4")
# print("hello5")
# print("hello6")


#raise
# age = 1

# if age<0:
#     raise Exception("Age should be positive")
# print(age)
  

#   #raise exception
# cpassword = "1234"
# pasword='1234'

# if cpassword != pasword:
#     raise Exception("Password mismatch")

# print("Welcome")

# print(2+3)
# print("nandu")
# print(77)
# try:
#     a=3
#     b=4
#     if type(a)==int and type(b)==int:
#        print("44"+77)
# except Exception as error:
#     print(error)
#     raise Exception("error")
#     print("welcome")

# p=input("enter p:")
# cp="nandini"
# if p!=cp:
#     raise Exception("error")
# print("welcome")

#bank 

# try:
#    pin=2007
#    balance=7000000
#    Epin=int(input("Enter the 4 digit pin"))
#    if pin !=Epin:
#          raise Exception ("Incorrect pin")
#    print("correct pin")
#    withdrawl_amount=int(input("Enter the withdrawl amount:"))
#    if withdrawl_amount >balance:
#     raise Exception ("innsufficient balance")
#    else:
#      y= balance- withdrawl_amount
#      print(f"balance={y}") 
# except Exception as error:
#  print("error")

# try:
#     PIN=2007
#     CPIN=int(input("enter the pin"))
#     if PIN!=CPIN:
#         print("wrong pin")
#         CPIN2=int(input("renter the pin:"))
#         if PIN!=CPIN2:
#          raise Exception("wrong again")
#         else:
#          bal=7000000
#          withdrawl=int(input("Enter the amount of input"))
#         if withdrawl>bal:
#             raise Exception("insuficient balance")
#         else:
#             print(bal-withdrawl)
#     else:
#      balance=7000000
#     withdrawl=int(input("enter the amount of withdrawl:"))
#     if withdrawl>balance:
#             raise Exception("insufficiesnt")
#     else:
#         print("balance is",bal-withdrawl)
# except Exception as error:
#     print("error")

# a=int(input("Enter the a value:"))
# b=int(input("enter the b value:"))
# n=int(input("enter the num"))
# if n==1:
#     x=a+b
#     print(f"sum",{x})
# elif n==2:
#     x=a-b
#     print(f"diff",{x})
# elif n==3:
#     x=a*b
#     print(f"product,{x}")
# elif n==4:
#     x=a/b
#     print(f"div",{x})
# else:
#     print("enter valid num")

# list={}
# x=int(input("enter the students marks:"))

  
# import numpy as np
# array=np.array([[1,3,4,5],[1,5,0,6],[5,4,7,9],[4,7,8,4]])
# print(array[0:3,3])

# import numpy as np
# array=np.array([[1,3,4,5],[1,5,0,6],[5,4,7,9],[4,7,8,4]])
# print(np.square(array))

# import numpy as np
# array=np.array([[1,3,4,5],[1,5,0,6],[5,4,7,9],[4,7,8,4]])
# print(array.shape)

# import numpy as np
# array=np.array([[1,3,4,5],[1,5,0,6],[5,4,7,9],[4,7,8,4]])
# print(array.ndim)

# import numpy as np
# array=np.array([[1,3.9,4.5,5],[1.8,5.6,0,6.1],[5,4.6,7.9,9],[4,7.8,8.4,4.8]])
# print(array.round())

# import numpy as np
# array=np.array([[1,3,4,5],[1,5,0,6],[5,4,7,9],[4,7,8,4]])
# print(array**2)

# import numpy as np
# array=np.array([[1,3,4,5],[1,5,0,6],[5,4,7,9],[4,7,8,4]])
# print(np.sum(array))

# import numpy as np
# array=np.array([[1,3,4,5],[1,5,0,6],[5,4,7,9],[4,7,8,4]])
# array=array>5
# print(array)

# import numpy as np
# array=np.array([[1,3,4,5],[1,5,0,6],[5,4,7,9],[4,7,8,4]])
# print(array+1)

#match
# import re
# text="nandu,123,bye"
# i=re.match("nandu",text)
# print(i)

# import re
# text="nandu,123,bye"
# i=re.sub("nandu","bye",text)
# print(i)

# import re
# text="colour,color"
# i = re.findall("colou?r",text)
# print(i)
# # 
#starts with
# import re
# text="colour,color"
# i = re.findall("^co",text)
# print(i)

# #ends with
# import re
# text="colour,color"
# i = re.findall("or$",text)
# print(i)

# #repeted
# import re
# text="cool"
# i = re.findall("o+",text)
# print(i)

# import re
# text="Nandini is good girl 77"
# i = re.findall("\w",text)
# print(i)



# import re
# i=input("Enter the email")
# pattern="^[a-zA-Z0-9._]+@[a-z]+\.[a-z]{2,}$"
# match=re.match(pattern,i)
# if match:
#     print("welcome")
# else:
#     print("invalid")



# import re
# i=input("Enter the number")
# pattern="^[0-9]{10,10}$"
# match=re.match(pattern,i)
# if match:
#     print("correct")
# else:
#     print("invalid") 

# import re
# i=input("Enter the password to heart:")
# pattern="^[a-z]{,7}$"
# match=re.match(pattern,i)
# if match:
#     print("welcome")
# else:
#     print("getlost")    
# 


#matplotlib
import matplotlib.pyplot as plt
x=