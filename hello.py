from otp_generator import generate_otp 
from rollno import * 
details = {}
temp = 101
while True:
    print("Choose your options: ")
    print("1. Add Student")
    print("2. Display Student Details")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Enter Student Details: ")1
        name = input("Name: ")
        email = input("Email: ")
        marks = int(input("Marks: "))
        otp = generate_otp(email)
        cotp = int(input("Enter OTP: "))
        if cotp == otp:
            roll = temp 
            temp = temp + 1
            details[roll] = [name, email, marks]
            print(f"Student added with Roll Number: {roll}")
        else:
            print("Invalid OTP. Student not added.")
    elif choice == 2:
        if len(details) == 0:
            print("No student details available.")
        else:
            print("Student Details:")
            for x in details:
                print(f"Roll Number: {x}")
                print(f"Name: {details[x][0]}")
                print(f"Email: {details[x][1]}")
                print(f"Marks: {details[x][2]}")
                print()
    else:
        print("Thank You")
        break
