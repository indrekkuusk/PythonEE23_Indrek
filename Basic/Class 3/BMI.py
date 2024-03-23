#5. BMI - Write program that calculates body mass index (bmi = weight / (height*height)). Weight(kg) and height(meters) would be passed by user input.

# if bmi <= 18.5 print "Underweight"
# if bmi <= 25.0 print "Normal"
# if bmi <= 30.0 print "Overweight"
# if bmi > 30 print "Obese"


#5. BMI - Write program that calculates body mass index (bmi = weight / (height*height)). Weight(kg) and height(meters) would be passed by user input.

#cats = int(input("Please provide number of cats: "))
weight = int(input("Please provide number of weight: "))
#input("Enter :)")
height = float(input("Please provide number of height in meters: "))

#use float(input())
#input("Enter :)")
bmi = weight/(height*height)
if bmi < 18.5:
        print("Underweight")
if bmi <= 25.0:
        print("Normal")
if bmi > 30.0:
        print("Overweight")
if bmi > 30:
        print("Obese")

print(bmi, round(bmi,2))
print(round(bmi,2))