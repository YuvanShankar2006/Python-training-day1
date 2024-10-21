print("Employ details")
print("Welcome to your employee page :")
salary=int(input("enter your salary :"))
experience=int(input("enter your experience :"))
bonus=0

def salaryinfo(salary,experience,bonus):
  if(experience>=3 and experience<=5):
     salary+=5000
     bonus+=5000
  elif(experience>5 and experience<10):
     salary+=8000
     bonus+=8000
  else:
     salary+=10000
     bonus+=10000
  return salary,bonus
print("(1)salary details")
print("(2)experience details")
print("(3)bonus details")

choice=int(input("enter your choice :"))
newsalary=salaryinfo(salary,experience,bonus)
newbonus=salaryinfo(salary,experience,bonus)
if(choice==1):
   print(f" your salary is Salary :{newsalary}")
elif(choice==2):
   print(f"your experience is {experience}")
else:
   print(f"The bonus you have earned is : {newbonus}")

   