z=0
x=0
y=0
while z<=100:
    if z==100:
        print("you win")
        break
    else:
        x=int(input("enter the number player 1:"))
        if x<=10:
            z=x+z
            if z>100:
                print("error")
                break
        else:
                print("error")
                break
        y=int(input("enter the number player 2 :"))
        if y<=10:
                        z=z+y
        else:
                        print("error")
                        break    







                        