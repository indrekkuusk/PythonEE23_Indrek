#5. BMI - Write program that calculates body mass index (bmi = weight / (height*height)). Weight(kg) and height(meters) would be passed by user input.

weight = float(input("Please provide number of weight in kg: "))
#input("Enter :)")
height = float(input("Please provide number of height in meters: "))
#input("Enter :)")
bmi = weight/(height ** 2)

if 0 < bmi <= 18.5:
    print("Underweight")
elif bmi <= 25.0:
    print("Normal")
elif bmi <= 30.0:
    print("Overweight")
elif bmi > 30:
    print("Obese")