def calculate_bmi(W,H):
    result = W/(H*H)
    return result

weight = float(input("Weight (kg):"))
height = float(input("Height (m):"))
bmi = calculate_bmi(weight, height)
print("Result: " + str(bmi))
