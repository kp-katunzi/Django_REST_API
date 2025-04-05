from django.core.management.base import BaseCommand
from students.models import Student, Subject

class Command(BaseCommand):
    help = "Seed the database with students and subjects"

    def handle(self, *args, **kwargs):
        # Clear existing data
        Student.objects.all().delete()
        Subject.objects.all().delete()

        # Add Students
        students = [
            {"Student_name": "Alice Allen", "program": "Software Engineering"},
            {"Student_name": "Bob Jck", "program": "Data Science"},
            {"Student_name": "Charlie Charles", "program": "Cyber Security"},
            {"Student_name": "David Daniel", "program": "Software Engineering"},
             {"Student_name": "John bakari", "program": "Multmedia"},
            {"Student_name": "Bob", "program": "Information science"},
            {"Student_name": "Charles paul", "program": "Cyber Security Engineering"},
            {"Student_name": "Davidson Downson", "program": "Software Engineering"},
            {"Student_name": "kp paul", "program": "Cyber Security Engineering"},
            {"Student_name": "Davies Downson", "program": "Software Engineering"},
        ]
        for student in students:
            Student.objects.create(**student)

        # Add Subjects
        subjects = [
            {"course_name": "Intro to Programming", "year": 1},
            {"course_name": "Data Structures", "year": 2},
            {"course_name": "Databases", "year": 3},
            {"course_name": "Machine Learning", "year": 4},
            {"course_name": "Intro to Nertworking", "year": 1},
            {"course_name": "Intro php ", "year": 2},
            {"course_name": "Spring boot", "year": 3},
            {"course_name": "Artificial Intelligence", "year": 4},
            {"course_name": "Intro Software", "year": 1},
            {"course_name": "computer theory", "year": 2},
            {"course_name": "Android", "year": 3},
            {"course_name": "Cloud computing", "year": 4},
            {"course_name": "Intro to Software", "year": 1},
            {"course_name": "computer theory", "year": 2},
            {"course_name": "Linux", "year": 3},
            {"course_name": "System Development", "year": 4},
        ]
        for subject in subjects:
            Subject.objects.create(**subject)

        self.stdout.write(self.style.SUCCESS("✅ Database Seeded Successfully!"))
