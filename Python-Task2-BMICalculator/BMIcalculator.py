def calculate_bmi(weight, height):
   bmi=weight/(height**2)
   return round(bmi, 2)

def check_bmi_category(bmi):
   if bmi < 18.5:
       return "Underweight"
   elif 18.5 <= bmi < 24.9:
       return "Normal weight"
   elif 25 <= bmi < 29.9:
       return "Overweight"
   else:
       return "Obese"

print("Welcome to the BMI Calculator!")

try:
    weight=float(input("Please enter your weight in kilograms: "))
    height=float(input("Please enter your height in meters: ")) 
    bmi=calculate_bmi(weight, height)
    category=check_bmi_category(bmi)
    print(f"Your BMI is: {bmi}. Category: {category}.")
except ValueError:
    print("Invalid input. Please enter numbers only.")