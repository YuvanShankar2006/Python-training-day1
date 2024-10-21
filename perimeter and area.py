def perimeter(l,b):
    return(2*(l+b)) 
def area(l,b):
    return l*b
l=int(input("Enter a length for the rectangle : "))
b=int(input("Enter the breadth fo the rectangle :"))
c=int(input("Enter the choice : "))
if(c==1):
    peri=perimeter(l,b)
    print(peri)
if(c==2):
    areas=area(l,b)
    print(areas)
    
