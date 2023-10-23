def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height*height)
    print("bmi =" + str(bmi))
    if bmi<18.5:
        print("Underweight")
    elif bmi >=18.5 and bmi <=25.0:
        print("Normal Weight")
    else:
        print("Overweight")

calculate_bmi(weight=57, height=1.73)