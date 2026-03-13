import os
import django
import random
from faker import Faker
from django.utils import timezone

# Setup Django environment so this standalone script can access your database
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# Import your models
from tasks.models import Priority, Category, Task, SubTask, Note

def populate_database():
    fake = Faker()

    # 1. Manually add records to Priority and Category 
    priority_names = ["high", "medium", "low", "critical", "optional"]
    category_names = ["Work", "School", "Personal", "Finance", "Projects"]

    print("Creating Categories and Priorities...")
    for p_name in priority_names:
        Priority.objects.get_or_create(name=p_name)
    
    for c_name in category_names:
        Category.objects.get_or_create(name=c_name)

    # Grab the lists of created objects to use them below
    priorities = list(Priority.objects.all())
    categories = list(Category.objects.all())

    # 2. Use faker package in generating fake data for Task, Notes, and SubTask models 
    print("Generating Fake Tasks, Subtasks, and Notes...")
    status_choices = ["Pending", "In Progress", "Completed"]

    # Let's generate 10 fake tasks
    for _ in range(10):
        # Create Task
        task = Task.objects.create(
            title=fake.sentence(nb_words=5),  # Starts with a capital letter and ends with a period [cite: 96, 99, 100]
            description=fake.paragraph(nb_sentences=3),  # Generates a random paragraph with about 3 sentences [cite: 97, 101]
            deadline=timezone.make_aware(fake.date_time_this_month()),  # Converts naive datetime to timezone-aware [cite: 42, 44]
            status=fake.random_element(elements=status_choices),  # Returns a random value from the given sequence [cite: 98, 102]
            category=random.choice(categories),
            priority=random.choice(priorities)
        )

        # Create 1-3 random SubTasks for each Task
        for _ in range(random.randint(1, 3)):
            SubTask.objects.create(
                parent_task=task,
                title=fake.sentence(nb_words=3),
                status=fake.random_element(elements=status_choices)
            )

        # Create 1-2 random Notes for each Task
        for _ in range(random.randint(1, 2)):
            Note.objects.create(
                task=task,
                content=fake.paragraph(nb_sentences=2)
            )

    print("Database population complete! Your board should be full of data.")

if __name__ == '__main__':
    populate_database()