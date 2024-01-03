import csv
import matplotlib.pyplot as plt

class Student:
    def __init__(self, name, age, major, courses):
        self.name = name
        self.age = age
        self.major = major
        self.courses = courses

class StudentDTO:
    def __init__(self, name, average_grade):
        self.name = name
        self.average_grade = average_grade

class StudentMapper:
    @staticmethod
    def map_to_dto(student):
        # Laske kurssien keskiarvo
        courses = student.courses
        total_grade = sum(grade for _, grade in courses)
        average_grade = total_grade / len(courses) if courses else 0
        return StudentDTO(student.name, average_grade)


def read_student_data(csv_file):
    students = []

    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file, fieldnames=['Name', 'Age', 'Major', 'Courses'])
        next(reader, None)

        for row in reader:
            name = row['Name']
            age = int(row['Age'])
            major = row['Major']
            
            # Tarkista, että 'Courses'-sarake on olemassa
            if 'Courses' in row:
                # Jaa kurssiarvosanat ja käsittele ne erikseen
                courses_data = row['Courses'].split(';')
                courses = []
                for course_data in courses_data:
                    course_parts = course_data.split(':')
                    if len(course_parts) == 2:
                        course_name, grade = course_parts
                        courses.append((course_name.strip(), float(grade)))
                    else:
                        print(f"Varoitus: Virheellinen kurssin tiedot opiskelijalta {name}: {course_data}")

            else:
                print(f"Varoitus: 'Courses'-sarake puuttuu opiskelijalta {name}.")
                courses = []

            student = Student(name, age, major, courses)
            students.append(student)

    return students



def visualize_data(student_dtos):
    # Erottele opiskelijoiden nimet ja keskiarvot listoiksi
    names = [student_dto.name for student_dto in student_dtos]
    average_grades = [student_dto.average_grade for student_dto in student_dtos]

    # Luo pylväsdiagrammi
    plt.bar(names, average_grades)
    plt.ylabel('Kurssien keskiarvo')
    plt.title('Opiskelijoiden kurssien keskiarvot')
    plt.show()

# Käytetään funktioita tehtävän suorittamiseen
csv_file_path = 'students_data.csv'
students = read_student_data(csv_file_path)
student_dtos = [StudentMapper.map_to_dto(student) for student in students]
visualize_data(student_dtos)
