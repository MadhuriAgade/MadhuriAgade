#WAP to convert minutes into hours and print it
#Exampe: 135 is 2 hours 15 minutes
minutes = int (input("Enter your minutes :"))
# print(minutes ,"is",  minutes//60 ,"hours", minutes%60 ,"minutes")
print(f"{minutes} is  {minutes//60} hours {minutes%60} minutes")