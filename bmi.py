def calculate_bmi(height, weight):
    print ("Height = " + str(height))
    print ("Weight = " + str(weight))
weight=float(input("Weight ="))
height=float(input("Height ="))

bmi = weight / height / height
print ("BMI = " + str(bmi))

if bmi < 18.5 :
    print("You Are Underweight")
if bmi > 25.0 :
    print ("You Are Overweight")
else : print ("You Are Normal Weight")



