weight = float(input("Input your weight: "))
height = float(input("Input your height: "))

bmi = (weight / height / height) * 10000
bmi_formated = float("%.1f" % bmi)
bmi_words = ""

if bmi_formated < 18.5:
     bmi_words = ("Underweight")
elif bmi_formated >= 18.5 and bmi_formated <=24.9:
     bmi_words = ("Normal weight")
elif bmi_formated >= 25 and bmi_formated <= 29.9:
     bmi_words = ("Overweight")
elif bmi_formated >= 30:
     bmi_words = ("Obesity")

print(f"Your BMI is {bmi_formated}. You have {bmi_words}.")

print("\nUnderweight = <18.5 \nNormal weight = 18.5 – 24.9 \nOverweight = 25 – 29.9 \nObesity = BMI of 30 or greater")

