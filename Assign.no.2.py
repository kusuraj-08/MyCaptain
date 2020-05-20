                #Assignment No. 2
#.......................Fibonacci Series......................!

num=int(input("Enter the number:"))
a=0
b=1
sum=0
count=1
print("Fibonacci series are:",end=" ")
while(count<=num):
    print(sum,end=" ")
    count+=1
    a=b
    b=sum
    sum=a+b
