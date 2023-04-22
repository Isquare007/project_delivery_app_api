from django.contrib import admin
from pd_app.models import Project, Task, User, Milestone, Issue_Action, Project_document, Team, Transaction, Message 

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    pass

class TaskAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    pass

class MilestoneAdmin(admin.ModelAdmin):
    pass

class Issue_ActionAdmin(admin.ModelAdmin):
    pass

class Project_documentAdmin(admin.ModelAdmin):
    pass

class TeamAdmin(admin.ModelAdmin):
    pass

class TransactionAdmin(admin.ModelAdmin):
    pass

class MessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Milestone, MilestoneAdmin)
admin.site.register(Issue_Action, Issue_ActionAdmin)
admin.site.register(Project_document, Project_documentAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Message, MessageAdmin)
