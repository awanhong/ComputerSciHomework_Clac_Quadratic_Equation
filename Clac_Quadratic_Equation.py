import math

def work(a,b,c):
    if(a==0):
        return
    d=b*b-4*a*c
    if(d<0):
        print("No real solutions :(")
        print("What a sad story OAO")
        return
    x1=((-1)*b+math.sqrt(d))/(2*a)
    x2=((-1)*b-math.sqrt(d))/(2*a)
    if(d==0):
        print("There are two equal solutions,yeah!")
        print("And they are",x1,"(s)")
    else:
        print("There are two inequal solutions, yooooo!")
        print("And they are",x1,"and",x2)

def chkchk():
    chk=input("BTW, are u a teacher? (y/n)")
    if(chk[0]=="n" or chk[0]=="N"):
        return 0
    else:
        print("Oh,hello")
        return 1


def douwo():
    if(chkchk()):
        return
    print("...")
    input()
    print("T^T")
    input()
    print("大哥输入二次方程啊")

def youdouwo():
    if(chkchk()):
        return
    print("我去")
    input()
    print("不输入方程就算了")
    input()
    print("您那个等式能成立嘛....")

def dabai():
    if(chkchk()):
        return
    print("0=0")
    input()
    print("(●—●)")
    input()
    print("However,")
    input()
    print("你搞出来个大白并没有什么卵用")

def inputandwork():
    a=float(input("Please enter a: "))
    b=float(input("Please enter b: "))
    c=float(input("Please enter c: "))
    print("Your input is ",a,"X^2+",b,"X+",c,"=0")
    if(a==0 and b==0 and c!=0):
        youdouwo()
    if(a==0 and b!=0):
        douwo()
    if(a==0 and b==0 and c==0):
        dabai()
    work(a,b,c)

inputandwork()
