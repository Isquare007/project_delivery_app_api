from rest_framework import serializers
from pd_app.models import Project, Task, User, Milestone, Issue_Action, Project_document, Team, Transaction, Message

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('project_id', 'project_name', 'start_date', 'end_date',
                'ministry', 'contractor', 'local_gov', 'description',
                'contract_sum', 'status','priority'
                )
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('task_id', 'task_name', 'project_id', 'start_date',
                'end_date', 'note', 'status', 'priority'
                )
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'user_name', 'project_id', 'role',
                )
    
class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = ('milestone_id', 'project_id', 'task_id', 'progress',
                'tag'
        )
    
class Issue_ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue_Action
        fields = ('issue_action_id', 'project_id', 'task_id', 'description',
                'committed_by'
                )

class Project_documentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_document
        fields = ('file_name', 'user_id', 'uploaded_by', 'project_id',
                'task_id', 'uploaded_at', 'file_url'
                )

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('team_name', 'projects', 'head', 'members',
                )

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('transaction_id', 'project_id', 'amount_disbursed', 'amount_spent'
                )
    
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('message_id', 'user_id', 'content'
                )
