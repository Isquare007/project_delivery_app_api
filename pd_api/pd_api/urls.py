"""pd_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

from pd_app.views import project, task, user, milestone, home

urlpatterns = [
    # path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', home.home, name='home'),
    path('api_schema', get_schema_view(title='Project Delivery API',
         description='Documentation for the Project Delivery app rest api'), name='Project Delivery API'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url': 'api_schema'}
    ), name='swagger-ui'
    ),
    # project urls
    path('project', project.project_getpost),
    path('project/<uuid:project_id>', project.projects),
    # tasks urls
    path('project/<uuid:project_id>/task', task.task_getpost),
    path('project/<uuid:project_id>/task/<uuid:task_id>', task.tasks),
    # user urls
    path('users', user.list_users),
    path('users/<uuid:user_id>', user.list_users),
    path('project/<uuid:project_id>/user', user.user_getpost),
    path('project/<uuid:project_id>/user/<uuid:user_id>', user.users),
    # user urls
    path('milestones', milestone.list_milestones),
    path('milestones/<uuid:milestone_id>', milestone.list_milestones),
    path('project/<uuid:project_id>/milestone', milestone.milestone_getpost),
    path('project/<uuid:project_id>/milestone/<uuid:milestone_id>',
         milestone.milestones),
]

urlpatterns += staticfiles_urlpatterns()
