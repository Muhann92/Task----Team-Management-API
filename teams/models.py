from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(blank=True)
    

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    members = models.ManyToManyField(User, related_name="teams", through='Membership')
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name


class Membership(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Adminstrator'),
        ('member', 'Member'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role = models.CharField(choices=ROLE_CHOICES, default='member')

    def __str__(self):
        return ""

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('niedrig', 'Niedrig'),
        ('mittlere', 'Mittlere'),
        ('hoch', 'Hoch'),
    ]
    STATUS_CHOICES = [
        ('zu_tätigen', 'Zu Tätigen'),
        ('in_bearbeitung', 'In Bearbeitung'),
        ('erledigt', 'Erledigt'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default='zu_tätigen')
    priority = models.CharField(choices=PRIORITY_CHOICES, default='mittlere')

    # Beziehungen
    assigned_to = models.ManyToManyField(User, related_name='tasks')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.priority} - {self.status} - {self.team} - {self.due_date}"