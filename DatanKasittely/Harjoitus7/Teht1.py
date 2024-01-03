import csv


class Student:
    def __init__(self, name, age, major, courses):
   
        self.name = name
        self.age = age
        self.major = major
        self.courses = courses
    
    def __str__(self):
        return f"{self.name}, {self.age}, {self.major}, {self.courses}"

#Tee mapper, joka muuntaa Student-oliot StudentDTO-olioiksi,
#  jotka sisältävät opiskelijan nimen ja kurssien keskiarvon.

class StudentDTO:
    def __init__(self, name, age, major, courses):
        self.name


file_path = 'students_data.csv'

# Tyhjä lista
students_data = []

# Avaa CSV-tiedosto ja lue se
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    # Käy läpi jokainen tieto
    for row in csv_reader:
        name, age, major, courses = row
        courses = courses.split(',')

        #Student object
        student = Student(name, int(age), major, courses)
        students_data.append(student)

        #Kurssien keskiarvo
        courses_list = [course.split(":") for course in courses.split(";")]
        total_courses = len(courses_list)
        total_points = sum(int(points) for _, points in courses_list)
        average = total_points / total_courses if total_courses > 0 else 0

for student in students_data:
    print(student)
    print(average)
