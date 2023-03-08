#write a program that ask for ur weight and converts it to kg or lbs
weight =int(input("Weight: "))
Unit =input("(K)g or (L)bs: ")
if Unit.upper() =="K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted =weight * 0.45
    print("Weight in kgs: " + str(converted))
