# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Olivier Richer, 6/01/2025, created script
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #
# importing the out of the box json capabilities
import json


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants

FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants

students: list = []  # a table of student data

menu_choice: str = ''  # Hold the choice made by the user.
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    O.Richer, 6/01/2025,Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str):
        """ This function reads data from a json file and loads it

            ChangeLog: (Who, When, What)
            O.Richer, 6/01/2025,Created function

         """

# Extract the data from the file
        try:
           file = open(FILE_NAME, "r")
           student_data = json.load(file)
           file.close()

        except Exception as e:
          IO.output_error_messages("this file doesn't exist! Trying to open it again after creating... ", e)
        finally:
           if file.closed == False:
            file.close()
        return student_data


    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """This function writes  data into a json file
        ChangeLog: (Who, When, What)
            O.Richer, 6/01/2025,Created function
        """


        try:
           file = open(FILE_NAME, "w")
           json.dump(students, file, indent=2)
           file.close()
           print("The following data was saved to file!")
           for student in students:
              print(f'Student {student["FirstName"]} '
                    f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            if file.closed == False:
               file.close()
            IO.output_error_messages("Please check that the file is not open by another program.", e)


class IO:
   """ A collection of presentation layer functions that manage user input and output
            ChangeLog: (Who, When, What)
            O.richer, 6/01/2025
   """

   @staticmethod
   def output_error_messages(message: str, error: Exception = None):
            """ This function displays the custom error messages to the user
                ChangeLog:(Who, When, What)
                O.Richer, 6/01/2025, Created function
                return: None
            """
            print(message, end="\n\n")
            if error is not None:
                print("---Technical Error Message---")
                print(error, error.__doc__, type(error), sep='\n')

   @staticmethod
   def output_menu(menu: str):
                    """This function print out the menu
                        ChangeLog:(Who, When, What)
                        O.richer,6/01/2025, Created function
                        Return: None
                    """
                    print()
                    print(menu)
                    print()


   @staticmethod
   def input_menu_choice():
     """ This function gets a menu choice from the user
        ChangeLog:(Who, When, What)
       O.Richer, 6/01/2025, Created function
        Return: string with the users choice
     """
     choice = "0"
     try:
        choice = input("Enter your choice: ")
        if choice not in ("1", "2", "3", "4"):
            raise Exception("Please only choose option 1, 2, 3, or 4")
     except Exception as e:
        IO.output_error_messages(e.__str__())
     return choice

   @staticmethod
   def input_student_data(student_data:list):
        """ This function takes student first and last name + the course  input from the user
            ChangeLog:(Who, When, What)
            O.richer,6/01/2025, Created function
            Return: student registered data
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha() and student_first_name.find(" ")== -1:
                raise ValueError("The first name can only have alphabetic character.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha() and student_last_name.find(" ") == -1:
                raise ValueError("The last name can only have alphabetic character.")

            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}. ")
        except ValueError as e:
            IO.output_error_messages("Please do not enter numbers.", e)
        except Exception as e:
            IO.output_error_messages("errors.", e)
        return students




   @staticmethod
   def output_student_courses(student_data:list):
        """ This function process the data to create and display a custom message
            ChangeLog:
            O.richer,6/01/2025, Created function
            Return: student registered data
        """
        print("-" * 50)
        print("\nThe current data is:")
        for student in students:
            print(f'Student {student["FirstName"]} '
                f'{student["LastName"]} is enrolled in {student["CourseName"]}')

        print("-" * 50)


# Main Program
students = FileProcessor.read_data_from_file(FILE_NAME)
while True:
    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data = students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data = students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    

print("Program Ended")
