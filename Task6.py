11# A console based student score management system

student_name=[]
student_score=[]

def add_student_name():
    name=input("Add students name:")
    while True:
        score=int(input("Enter score(0-100)"))
        if 0<=score<=100:
            break
        elif 0>=score>=100:
            print("score must be between 0 and 100")
        else:
            print("invalid input")
    
    student_name.append(name)
    student_score.append(score)
    print("Students details added successfully.\n")

# defining view students:
# Adds a student name and score to the lists
    # Includes validation for score input

def view_students():
    if not student_name:
        print("No student records found.\n")
        return

    print("\nStudent Scores:")
    for i in range(len(student_name)):
        print(f"{i + 1}. {student_name[i]} - {student_score[i]}")
    print()


# defining statistics. 
    # Displays highest, lowest, average score and grade distribution


def show_statistics():
   
    if not student_score:
        print("No student records found.\n")
        return

    highest = max(student_score)
    lowest = min(student_score)
    average = sum(student_score) / len(student_score)

    # Grade counters
    grade_a = grade_b = grade_c = grade_d = 0

    for score in student_score:
        if 80 <= score <= 100:
            grade_a += 1
        elif 60 <= score <= 79:
            grade_b += 1
        elif 40 <= score <= 59:
            grade_c += 1
        else:
            grade_d += 1

    print("\nStatistics:")
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")
    print(f"Average Score: {average:.1f}")
    print("Grades:")
    print(f"A: {grade_a}")
    print(f"B: {grade_b}")
    print(f"C: {grade_c}")
    print(f"D: {grade_d}\n")


while True:
    print("Student Score Management System")
    print("1. Add student score")
    print("2. View all scores")
    print("3. Show statistics")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        add_student_name()
    elif choice == "2":
        view_students()
    elif choice == "3":
        show_statistics()
    elif choice == "4":
        print("Goodbye! Thank you for using the system.")
        break
    else:
        print("Invalid choice. Please select 1–4.\n")


    
   

