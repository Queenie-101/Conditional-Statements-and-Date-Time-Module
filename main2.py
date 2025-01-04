height=float(input("Enetr your height in metres:"))
weight=float(input("Enter your weight in kg:"))
BMI = weight/(height**2) 
print("Your BMI is:", BMI)
if BMI <= 18.4:
   print("You are underweight.")
elif BMI <=24.9:
   print("You are healthy.")
elif BMI <=29.9:
   print("You are overweight")
elif BMI <39.9:
   print("You are obese")
else:
   print("Invalid Input")