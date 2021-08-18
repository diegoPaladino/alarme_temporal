# stuents_records_1

# List is stored
list1 = []

# Program prompts you to login
username = input("Enter a Username\n")
password = "password"
password = input("Enter Password\n")
if (password == "password"):
    print("Password Accepted")
    print("Welcome - Access Granted")
else:
     print("Password Denied")
while(password == "password"):

    # Program displays a menu
    print("GRAFFINS COLLEGE")
    print("CAPS DEPARTMENT")
    print("[1] Record Marks")
    print("[2] Displays Performance List")
    print("[3] Display Transcripts")
    print("[4] Exit")
    print("Please Enter an Option")

    # Input an option from the menu
    option = int(input("Option: "))

    # For option 1
    if option == 1:

        # Prompt to enter the number of students
        # Input number of students
        print("Enter the number of students to record")
        no_of_students = int(input("Number of students: "))

        # Initialize count
        count = 0

        # Loop to repeat while count is less than the number entered
        while count < no_of_students:

            # Prompt to enter Student's Admission Number
            # Input Admission Number
            print("\nEnter student's admission number")
            adm_number = input("Adm. Number: ")

            # Prompt to enter Student's Name
            # Input Student's name
            print("\nEnter student's name")
            std_name = input("Student's Name: ")

            # Prompt to enter windows marks
            # Input windows marks
            print("\nEnter Performance in Windows")
            windows = int(input("Windows: "))

            # Prompt to enter word marks
            # Input word marks
            print("\nEnter Performance in Word")
            word = int(input("Word: "))

            # Prompt to enter excel marks
            # Input excel marks
            print("\nEnter Performance in Excel")
            excel = int(input("Excel: "))

            # Prompt to enter access marks
            # Input access marks
            print("\nEnter Performance in Access")
            access = int(input("Access: "))

            # Prompt to enter powerpoint marks
            # Input powerpoint marks
            print("\nEnter Performance in Powerpoint")
            powerpoint = int(input("Powerpoint: "))

            # Prompt to enter internet marks
            # Input internet marks
            print("\nEnter Performance in Internet")
            internet = int(input("Internet: "))

            # The list is defined
            list1 = [adm_number, std_name, windows, word, excel, access, powerpoint, internet]

            # Count increment
            count = count + 1

    # For option 2
    elif option == 2:

        # Command to display the list
        print(list1)

        # Calculation of the total marks
        total = windows + word + excel + access + powerpoint + internet

        # Prompt to display the total marks
        print("Total marks: ")
        print(total)

        # Calculation of mean marks
        mean = total / 6

        # Prompt to display mean
        print("Mean marks: ")
        print(mean)

        # Condition to check whether students has passed or failed
        if mean > 60:
            comment = "pass"
        else:
            comment = "fail"

        # The comment display prompt
        print("Mean grade: ")
        print(comment)

    # For option 3
    elif option == 3:

        # Prompt to enter Student's Admission Number
        # Admission Number input
        print("Enter admission number of student: ")
        adm_number = input("Adm Number: ")

        # Condition to search for the admission number
        for adm_number in list1:
            # List is displayed
            print("Adm_number\tName\twindows\tword\texcel\taccess\tpowerpoint\tinternet")
            print(list1)

    # For option 4
    elif option == 4:

        # Program terminates
        break