x=int(input("Enter x : "))
y=int(input("Enter y : "))
x2=1
x1=0
a=x
y2=0
y1=1
b=y
print("Round-1 : ")
print("--------")
print("a=",a)
print("b=",b)
print ("x2=",x2)
print("x1=",x1)
print("y2=",y2)
print("y1=",y1)

round=2
while(b!=0):
    print("round-",round)
    print("-------")
    round+=1
    q=a//b
    print("q=a/b","=",a,"/",b,"=",q)
    r=a-(q*b)
    print("r=a-(q*b)=",a,"-","(",q,"*",b,")=",r)
    x=x2-(q*x1)
    print("x=x2-(q*x1) = ",x2,"-","(",q,"*",x1,")=",x)
    y=y2-(q*y1)
    print("y=y2-(q*y1) = ",y2,"-","(",q,"*",y1,")=",y)
    x2=x1
    x1=x
    a=b
    y2=y1
    y1=y
    a=b
    b=r
    print ("x2=",x2)
    print("x1=",x1)
    print("y2=",y2)
    print("y1=",y1)
    print("a=",a)
    print("b=",b)
    print("-------")


print("gcd=",a,"x2=",x2,"y2=",y2)
