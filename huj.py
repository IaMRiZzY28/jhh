class Student:
    def __init__(self, name):
        """
        Constructor to initialize the student's name and grades.
        :param name: The name of the student.
        """
        self.name = name
        self.grades = []  
    def add_grade(self, grade):
        """
        Method to add a grade to the student's record.
        :param grade: The grade to be added.
        """
        if grade < 0 or grade > 100:
            print("Invalid grade. Please enter a grade between 0 and 100.")
        else:
            self.grades.append(grade)
            print(f"Grade {grade} added for {self.name}.")

    def calculate_average(self):
        """
        Method to calculate the average grade.
        :return: The average grade of the student.
        """
        if not self.grades:
            return 0  
        return sum(self.grades) / len(self.grades)

    def feedback(self):
        """
        Method to provide feedback based on the average grade.
        """
        avg = self.calculate_average()
        if avg >= 90:
            print(f"{self.name} has an excellent performance with an average grade of {avg:.2f}.")
        elif avg >= 70:
            print(f"{self.name} is doing well with an average grade of {avg:.2f}.")
        elif avg >= 50:
            print(f"{self.name} has a passing average grade of {avg:.2f}.")
        else:
            print(f"{self.name} needs improvement. The average grade is {avg:.2f}.")


def main():
    students = []  

    while True:
        
        name = input("Enter student's name (or 'exit' to stop): ")
        if name.lower() == 'exit':
            break  

        
        student = Student(name)

        
        try:
                grade = float(input(f"Enter a grade for {name} (or 'done' to finish): "))
                student.add_grade(grade)
            except ValueError:
                break  

        
        student.feedback()

        
        students.append(student)

    
    print("\nSummary of all students:")
    for student in students:
        print(f"{student.name}: Average Grade = {student.calculate_average():.2f}")


if __name__ == "__main__":
    main()
