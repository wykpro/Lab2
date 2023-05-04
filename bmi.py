def calculate_bmi(height, weight):
    print ("Height = " + str(height))
    print ("Weight = " + str(weight))
    bmi = weight / height / height
    print ("BMI = " + str(bmi))

    if bmi < 18.5 :
        return -1
    if bmi > 25.0 :
        return 1
    else : return 0


x = calculate_bmi(weight=57,height=1.73)
print(x)



