from enum import Enum
import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Status(Enum):
    """status enumerator"""
    IN_PROGRESS = 'in progress'
    DONE = 'done'

class Priority(Enum):
    """priority enumerator"""
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    
class Schedule(Enum):
    """schedule enumerator"""
    ON_SCHEDULE = 'on schedule'
    BEHIND_SCHEDULE = 'behind schedule'
    
# Create your models here.

class Project(models.Model):
    """stores a project information"""
    project_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_name = models.CharField(max_length=500)
    user_assigned = models.ManyToManyField('User', blank=True, related_name='projects')
    start_date = models.DateField()
    end_date = models.DateField()
    ministry = models.CharField(max_length=500)
    contractor = models.CharField(max_length=500)
    local_gov = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    contract_sum = models.DecimalField(max_digits=20, decimal_places=2)
    status_choices = [(tag.name, tag.value) for tag in Status]
    status = models.CharField(max_length=20, choices=status_choices)
    priority_choices = [(tag.name, tag.value) for tag in Priority]
    priority = models.CharField(max_length=20, choices=priority_choices)
    
    objects = models.Manager()
    
    def __str__(self) -> str:
        return (f'{self.project_id} ({self.project_name})')
        # return str(self.project_id)
    
class Task(models.Model):
    """stores information of tasks"""
    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task_name = models.CharField(max_length=500)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    users_assigned = models.ManyToManyField('User', blank=True, related_name='tasks')
    start_date = models.DateField()
    end_date = models.DateField()
    note = models.CharField(max_length=500)
    status_choices = [(tag.name, tag.value) for tag in Status]
    status = models.CharField(max_length=20, choices=status_choices)
    priority_choices = [(tag.name, tag.value) for tag in Priority]
    priority = models.CharField(max_length=20, choices=priority_choices)
    
    objects = models.Manager()

    def __str__(self) -> str:
        return (f'{self.task_id} ({self.task_name})')
    
class User(models.Model):
    """stores a user information"""
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=500)
    project_assigned = models.ManyToManyField(Project, related_name='users')
    role = models.CharField(max_length=500)
    
    objects = models.Manager()
    
    def __str__(self) -> str:
        return self.user_name + " " + self.role
    
class Milestone(models.Model):
    """stores information about a milestone"""
    milestone_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='milestone')
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='milestone')
    progress = models.DecimalField(
        max_digits=5, decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    tag_choices = [(tag.name, tag.value) for tag in Schedule]
    tag = models.CharField(max_length=20, choices=tag_choices)
    
    objects = models.Manager()
    
    def __str__(self) -> str:
        return self.tag + " " + str(self.progress)
    
class Issue_Action(models.Model):
    """stores issues and action onformations"""
    issue_action_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issue')
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='issue')
    description = models.CharField(max_length=2000)
    committed_by = models.CharField(max_length=500)
    
    objects = models.Manager()
    
    def __str__(self) -> str:
        return Task.task_name + " " + self.description
    
class Project_document(models.Model):
    """stores project document data"""
    file_name = models.CharField(max_length=500)
    uploaded_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='pd')
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='pd')
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='pd')
    uploaded_at = models.DateField()
    file_url = models.CharField(max_length=1000)
    
    objects = models.Manager()
    
    def __str__(self) -> str:
        return self.file_name + " " + Project.project_name
    
    
class Team(models.Model):
    """stores team information"""
    team_name = models.CharField(max_length=500)
    projects = models.ManyToManyField(Project)
    head = models.CharField(max_length=500)
    members = models.CharField(max_length=500)
    
    objects = models.Manager()
    
    def __str__(self) -> str:
        return self.team_name + " " + self.head
    
class Transaction(models.Model):
    """stores transaction details"""
    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='transactions')
    amount_disbursed = models.DecimalField(max_digits=20, decimal_places=2)
    amount_spent = models.DecimalField(max_digits=20, decimal_places=2)
    
    objects = models.Manager()
    
    def __str__(self) -> str:
        return (f"{self.project_id} - {self.amount_spent}")
    
class Message(models.Model):
    """message information"""
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message')
    content = models.CharField(max_length=2500)
    
    objects = models.Manager()
    
    def __str__(self) -> str:
        return self.user_id + " " + self.content
