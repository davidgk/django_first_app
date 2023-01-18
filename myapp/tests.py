from django.contrib.staticfiles.finders import find
from django.test import TestCase

from myapp.models import Project, Task


# Create your tests here.
class ProjectTestCase(TestCase):
    def setUp(self):
        pass
    def test_project_create_and_save(self):
        """Project Saving """
        name_project = 'my First Project'
        project_01 = Project.objects.create(name=name_project)
        project_01.save()
        project_saved = Project.objects.get(name=name_project)
        self.assertEqual(project_saved.id, 1)
        self.assertEqual(project_saved.name, name_project)

    def test_project_with_task(self):
        """Project Saving """
        name_project = 'my First Project'
        project_01 = Project.objects.create(name=name_project)
        project_01.save()
        task_01 = Task(title='t1', description='d1', project=project_01)
        task_01.save()
        task_02 = Task(title='t2', description='d2', project=project_01)
        task_02.save()
        project_saved = Project.objects.get(name=name_project)
        self.assertEqual(project_saved.id, 1)
        tasks = Task.objects.all()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(len(project_saved.task_set.all()), 2)
        project_saved.task_set.create(title='t3', description='d3')
        self.assertEqual(len(project_saved.task_set.all()), 3)
        taskFiltered = project_saved.task_set.filter(title='t3').first()
        project_saved.task_set.create(title='t4', description='some thing than')
        taskFiltered = project_saved.task_set.filter(description__startswith='some').first()
        self.assertEqual(taskFiltered.id, 4)


