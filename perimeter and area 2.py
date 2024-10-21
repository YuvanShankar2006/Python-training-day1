def rectangle(l,b):
    area=l*b
    perimeter=(2*(l+b))
    if(choice==1):
       return (f"The area of the rectangle is {area}")
    else:
       return ("The perimeter and area of the reactangle is",perimeter,area)
l=int(input("enter a length of the rectangle :"))
b=int(input("eneter a breadth of the rectangle :"))
choice=int(input("enter a number :"))
result=rectangle(l,b)
print(result)