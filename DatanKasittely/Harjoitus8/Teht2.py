import csv
import matplotlib.pyplot as plt

class Student:
    def __init__(self, name, age, major, courses):
        self.name = name
        self.age = age
        self.major = major
        self.courses = courses

class CourseDTO:
    def __init__(self, course_name, average_grade):
        self.course_name = course_name
        self.average_grade = average_grade

class CourseMapper:
    @staticmethod
    def map_to_dto(course_name, students):
        # Laske kurssin opiskelijoiden keskiarvo
        total_grade = sum(grade for _, grade in students)
        average_grade = total_grade / len(students) if students else 0
        return CourseDTO(course_name, average_grade)

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

                student = Student(name, age, major, courses)
                students.append(student)

            else:
                print(f"Varoitus: 'Courses'-sarake puuttuu opiskelijalta {name}.")

    return students

def visualize_data(course_dtos):
    # Erottele kurssien nimet ja keskiarvot listoiksi
    course_names = [course_dto.course_name for course_dto in course_dtos]
    average_grades = [course_dto.average_grade for course_dto in course_dtos]

    # Aseta diagrammin koko
    plt.figure(figsize=(len(course_names)*2, 6))

    # Luo pylväsdiagrammi
    plt.bar(course_names, average_grades)
    plt.xlabel('Kurssin nimi')
    plt.ylabel('Opiskelijoiden keskiarvo')
    plt.title('Kurssien keskiarvot')

    # Käännä x-akselin tekstit pystysuuntaan
    plt.xticks(rotation='vertical')

    plt.show()



# Käytetään funktioita tehtävän suorittamiseen
csv_file_path = 'students_data.csv'
students = read_student_data(csv_file_path)

# Ryhmittele opiskelijat kursseittain
courses_dict = {}
for student in students:
    for course_name, grade in student.courses:
        if course_name not in courses_dict:
            courses_dict[course_name] = []
        courses_dict[course_name].append((student.name, grade))

# Luo CourseDTO-oliot ja laske kurssien keskiarvot
course_dtos = [CourseMapper.map_to_dto(course_name, students) for course_name, students in courses_dict.items()]

# Visualisoi kurssien keskiarvot pylväsdiagrammina
visualize_data(course_dtos)
