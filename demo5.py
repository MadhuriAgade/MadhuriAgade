#WAP to check if a person is eligible for discount the criteria is he
#  must be a student and age must be below 21
# input values to take are role and age
# example : Eligible : True
Age = int(input("Enter your age :"))
role = input("Enter your role :")
print( "Eligible:", Age<=21 and role=='student')