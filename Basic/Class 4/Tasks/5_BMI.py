#5. BMI - Write program that calculates body mass index (bmi = weight / (height*height)). Weight(kg) and height(meters) would be passed by user input.

weight = int(input("Please provide number of weight in kg: "))
#input("Enter :)")
height = int(input("Please provide number of height in meters: "))
#input("Enter :)")
bmi = weight/(height*height)
print(bmi)
if bmi <= 18.5:
        print("Underweight")
if bmi <= 25.0:
    print("Normal")
if bmi <= 30.0:
    print("Overweight")
if bmi > 30:
    print("Obese")

