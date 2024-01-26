weight=float(input("Enter weight:"))
height=float(input("Enter height:"))
bmi=weight/(height**2)
k=""
if bmi<18.5:
    k="Underweight"
elif 18.5<=bmi<24.9:
    k="Normal weight"
elif 25<=bmi<29.9:
    k="Overweight"
else:
    k="Obese"

print("BMI Calculator")
print(f"\nYour BMI is:{bmi:.2f}")
print(f"Category:{k}")
