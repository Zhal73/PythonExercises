math = int(input("Enter the maths marks: "))
chemistry = int(input("Enter the chemistry marks: "))
physics = int(input("Enter the physics marks: "))

percentage = (math + chemistry + physics)*100/300
print("Your percentage is",percentage)
if percentage >= 70.0:
    print("You score a grade of: A")
elif percentage >= 60:
    print("You score a grade of: B")
elif percentage >= 50:
    print("You score a grade of: C")
elif percentage >= 40:
    print("You score a grade of: D")
else:
    print("You Failed")