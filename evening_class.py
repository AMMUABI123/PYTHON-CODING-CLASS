# pattern
n=int(input("enter the number:")) 
for i in range(1,n+1):
    for j in range(1,i):
        print(i,end="")
    print()


#print abc
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()


#range
n=[1,8,9,10,5]
for i in range (n):
    if n<i:
        print(i)


#perfect square
n=int(input("enter the num:"))
s=n**2
if s%2==0:
    print("it is perfect square:",s)
else :
    print("it is not a perfect square",s)


#count
n=[1,3,2,5,9,11,10]
n_1=n[0]
n_2=n[1]
for i in n:
    if i<n_1:
        n_1=i
print(n_1)
for j in n:
    if j<n_2 and j>n_1:
        n_2=j
print(n_2)
        
        
#len function
str=input("enter the value:")
lenght=len(str)
print(lenght)


#index
str="Raja raja cholan"
print(str.index("j"))

#concadination
str="Raja raja"
str_1=" cholan"
print(str+str_1)


#def function
def add(a,b):
    c=a+b
    return c
x=add(10,20)
print(x)

#with para and with return
def sum():
    a=20
    b=20
    c=a+b
    return c
x=sum()
print(x)


#with para nad without return
def add (a,b):
    c=a+b
    print(c)
add(10,20)


#palindrom
str="madam"
slice=str[::-1]
print(slice)
if str==slice:
    print("it is a palindrome")
else:
    print("it is not a palindrome")


#count string
str="hello world"
print(str.count("hello"))


#slice
str="my name is abirami"
slice=(1,5)
print(slic[str])


#slice another method
s1="string"
slicing=slice(1,2)
sliced=s1[slicing]
print(sliced)


#slice another method
str="my name is abirami"
slice=(str(1,5))
print(slice)



#join method
str1=["ammu","abi"]
str2=""
print(str2.join(str1))

#join another method
str1="ammu"
str2="abi"
add="abc".join(str1)
print(add)

#split
str="ammu abi"
str2=(str.split())
print(str2)


#string
n=int(input("enter the number:"))
total=0
for i in str(n):
    total +=int(i)
    print(total)


#swap
a=5
b=8
a,b=b,a
print(a,b)


#list
list=[4,5,9,1,2,10,7]
sum=0
for i in list:
    sum+=i
print(sum)


#lambda
x=lambda a,b:a+b
print(x(5,6))

#paragraph
file=open("notes.txt","r")
print(file.read(100))
for each in files:
    print (each)

#file read
file=open("txt.py","r")
print(file.read())
for each in file:
    print(each)


# print(1 1 2 1 2 3 1 2 3 4)
n=5
num=1
for i in range(1,5):
     for j in range(1,i+1):
      print(j,end=" ")
      j+=1


#right angle star patten
n=int(input("enter the number:"))
for i in range (1,n+1):
    for j in range (i):
        print("*",end=" ")
    print()
    

#prime
n=[1,2,3,4,5,6]
num=0
for i in n:
    if i%2==0:
        num+=i
    if n in num:
       print("num id prime")
    else:
        print("num is not a prime")
    

#triangle
n=int (input("enter the num:"))
for i in range(1, n + 1):
    # Print spaces
    print(' ' * (n - i), end='')
    # Print stars
    print('* ' * i)

#multiplication
n=int(input("enter the number:"))
for i in range(1,n):
    for count in range(1,11):
        print(n,"x",count,"=",n*count)



#vowels
str="ammu"
vowels="aeiouAEIOU"
count=0
for char in (str):
    if char in (vowels):
            count+=1
print(count)

#reverse the string
num="hello,world!"
n=num[::-1]
print(n)

#print with ans
n_1=int(input("enter the number:"))
n_2=int(input("enter the number:"))
n_3=int(input("enter the number:"))
n_4=(n_1+n_2+n_3)
print(n_4,"","(",n_1,"+",n_2,"+",n_3,")")


#range
for i in range (1,51):
    if i%2==0:
        print(i)
    
#print star
n=int(input("enter the number:"))
for i in range (1,n):
    for j in range (n,0,):
        print(""*()+i*"")



        
n=int(input("enter the number:"))
for i in range (1,n):
    for j in range (1,i):
        print("*")
    



#smallest num
n_1=int(input("enter the number:"))
n_2=int(input("enter the number:"))
n_3=int(input("enter the number:"))
n_4=int(input("enter the number:"))
n_5=int(input("enter the number:"))
if n_1<n_2 and n_1<n_3 and n_1<n_4 and n_1<n_5:
    print("this is the smallest number",n_1)
elif n_2<n_1 and n_2<n_3 and n_2<n_4 and n_2<n_5:
    print("this is the smallest number",n_2)
elif n_3<n_1 and n_3<n_2 and n_3<n_4 and n_3<n_5:
    print("this the smallest number",n_3)
elif n_4<n_1 and n_4<n_2 and n_4<n_3 and n_4<n_5:
    print("this is the smallest number",n_4)
else:
    print("this is the smallest number",n_5)


##n=5
for i in range (1,8):
    for j in range (n,0,-1):
        print(" "*(n-i)+i*"")

# 1 2 3 4 5 6 7 8
n=5
num=1
for i in range(1,5):
    for j in range(1,i+1):
         print(j,end="")
         j+=1
    print()
num=1
for i in range(1,10):
     print(num)
     num+=1

#print string
x="sentence"
n=len(x)
num=0
for i in range(1,4):
    for j in range(1,i+1):
        print(x[num],end="")
        num+=1
    print()

#print list one by one
str1=["1","2","3","4"]
for i in str1:
    print(i)
    

#samllest num
str1=["1","2","3","4"]
for i in str1:
    print(i)


#
        
    