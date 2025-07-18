import uuid
from django.db import models
from manage_user.models import User


class Project(models.Model):
    BACK_END = "BACK-END"
    FRONT_END = "FRONT-END"
    IOS = "IOS"
    ANDROID = "ANDROID"
    TYPE_CHOICES = (
        (BACK_END, "Back-End"),
        (FRONT_END, "Front-End"),
        (IOS, "IOS"),
        (ANDROID, "Android"),
    )

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    project_contributor = models.ManyToManyField(to=User, blank=True, related_name="contributed_projects")
    project_type = models.CharField(max_length=30, choices=TYPE_CHOICES, verbose_name="Type du projet")
    time_created = models.DateTimeField(auto_now_add=True)


class Issue(models.Model):
    TO_DO = "TO DO"
    IN_PROGRESS = "IN PROGRESS"
    FINISHED = "FINISHED"
    STATUs_CHOICES = (
        (TO_DO, "To do"),
        (IN_PROGRESS, "In progress"),
        (FINISHED, "Finished"),
    )

    BUG = "BUG"
    FEATURE = "FEATURE"
    TASK = "TASK"
    TAG_CHOICES = (
        (BUG, "Bug"),
        (FEATURE, "Feature"),
        (TASK, "Task"),
    )

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    PRIORITY_CHOICES = (
        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High"),
    )

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    issue_contributor = models.ManyToManyField(to=User, blank=True, related_name="contributed_issues")
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    project_status = models.CharField(max_length=30, choices=STATUs_CHOICES, default=TO_DO, verbose_name="Statut du projet")
    project_tag = models.CharField(max_length=30, choices=TAG_CHOICES, verbose_name="Balise du projet")
    project_priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, verbose_name="Priorité du projet")


class Comment(models.Model):
    description = models.TextField(max_length=2048)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time_created = models.DateTimeField(auto_now_add=True)
