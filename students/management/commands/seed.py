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
            {"name": "Alice Allen", "program": "Software Engineering"},
            {"name": "Bob Jck", "program": "Data Science"},
            {"name": "Charlie Charles", "program": "Cyber Security"},
            {"name": "David Daniel", "program": "Software Engineering"},
             {"name": "John bakari", "program": "Multmedia"},
            {"name": "Bob", "program": "Information science"},
            {"name": "Charles paul", "program": "Cyber Security Engineering"},
            {"name": "Davidson Downson", "program": "Software Engineering"},
            {"name": "kp paul", "program": "Cyber Security Engineering"},
            {"name": "Davies Downson", "program": "Software Engineering"},
        ]
        for student in students:
            Student.objects.create(**student)

        # Add Subjects
        subjects = [
            {"name": "Intro to Programming", "year": 1},
            {"name": "Data Structures", "year": 2},
            {"name": "Databases", "year": 3},
            {"name": "Machine Learning", "year": 4},
             {"name": "Intro to Nertworking", "year": 1},
            {"name": "Intro php ", "year": 2},
            {"name": "Spring boot", "year": 3},
            {"name": "Artificial Intelligence", "year": 4},
             {"name": "Intro Software", "year": 1},
            {"name": "computer theory", "year": 2},
            {"name": "Android", "year": 3},
            {"name": "Cloud computing", "year": 4},
            {"name": "Cloud computing", "year": 4},
        ]
        for subject in subjects:
            Subject.objects.create(**subject)

        self.stdout.write(self.style.SUCCESS("✅ Database Seeded Successfully!"))
