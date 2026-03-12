import os
import django
from faker import Faker
import random

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from tasks.models import Category, Priority, Task, Note, SubTask
from django.utils import timezone

def populate_data():
    fake = Faker()
    
    # 1. Manually add records to Priority (high, medium, low, critical, optional) [cite: 79, 80]
    priorities = ['High', 'Medium', 'Low', 'Critical', 'Optional']
    for p_name in priorities:
        Priority.objects.get_or_create(name=p_name)
    
    # 2. Manually add records to Category (Work, School, Personal, Finance, Projects) [cite: 80, 81]
    categories = ['Work', 'School', 'Personal', 'Finance', 'Projects']
    for c_name in categories:
        Category.objects.get_or_create(name=c_name)

    all_priorities = list(Priority.objects.all())
    all_categories = list(Category.objects.all())
    status_choices = ["Pending", "In Progress", "Completed"]
    
    print("Generating tasks...")

    # 3. Generate Fake Data for Tasks
    for _ in range(15):  
        task = Task.objects.create(
            # For task title use sentence() [cite: 96]
            # Generates a random sentence consisting of about 5 words [cite: 99]
            title=fake.sentence(nb_words=5), 
            
            # For task description use paragraph() [cite: 97]
            # Generates a random paragraph with about 3 sentences [cite: 101]
            description=fake.paragraph(nb_sentences=3), 
            
            # Generates a random datetime object within the current month and makes it timezone-aware [cite: 42, 43, 44]
            deadline=timezone.make_aware(fake.date_time_this_month()), 
            
            # For status use random_element() [cite: 98]
            # Returns a random value from the given sequence [cite: 102]
            status=fake.random_element(elements=status_choices), 
            
            category=random.choice(all_categories),
            priority=random.choice(all_priorities)
        )

        # 4. Generate Fake Data for Notes
        for _ in range(random.randint(1, 3)): 
            Note.objects.create(
                task=task,
                content=fake.paragraph(nb_sentences=2)
            )

        # 5. Generate Fake Data for SubTasks
        for _ in range(random.randint(0, 4)): 
            SubTask.objects.create(
                parent_task=task,
                title=fake.sentence(nb_words=4),
                status=fake.random_element(elements=status_choices)
            )
            
    print("Database successfully populated!")

if __name__ == '__main__':
    populate_data()