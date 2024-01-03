import csv
import matplotlib.pyplot as plt

class Student:
    def __init__(self, name, age, major, courses):
        self.name = name
        self.age = age
        self.major = major
        self.courses = courses

class MajorDTO:
    def __init__(self, major_name, average_age):
        self.major_name = major_name
        self.average_age = average_age

class MajorMapper:
    @staticmethod
    def map_to_dto(major_name, students):
        # Laske pääaineen opiskelijoiden keski-ikä
        total_age = sum(student.age for student in students)
        average_age = total_age / len(students) if students else 0
        return MajorDTO(major_name, average_age)

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

def visualize_data(major_dtos):
    # Erottele pääaineiden nimet ja keski-iät listoiksi
    major_names = [major_dto.major_name for major_dto in major_dtos]
    average_ages = [major_dto.average_age for major_dto in major_dtos]

    # Aseta diagrammin koko
    plt.figure(figsize=(len(major_names)*2, 6))

    # Luo pylväsdiagrammi
    plt.bar(major_names, average_ages)
    plt.xlabel('Pääaineen nimi')
    plt.ylabel('Opiskelijoiden keski-ikä')
    plt.title('Pääaineiden keski-iät')

    # Käännä x-akselin tekstit pystysuuntaan
    plt.xticks(rotation='vertical')

    plt.show()

# Käytetään funktioita tehtävän suorittamiseen
csv_file_path = 'students_data.csv'
students = read_student_data(csv_file_path)

# Ryhmittele opiskelijat pääaineittain
majors_dict = {}
for student in students:
    major_name = student.major
    if major_name not in majors_dict:
        majors_dict[major_name] = []
    majors_dict[major_name].append(student)

# Luo MajorDTO-oliot ja laske pääaineiden keski-iät
major_dtos = [MajorMapper.map_to_dto(major_name, students) for major_name, students in majors_dict.items()]

# Visualisoi pääaineiden keski-iät pylväsdiagrammina
visualize_data(major_dtos)
