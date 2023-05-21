from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Project

class CustomUserCreationForm(UserCreationForm):
    project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        required=False,
        empty_label="Select a project"
    )
    role = forms.CharField(max_length=200)

    # project = forms.ForeignKey(Project, null=True, blank=True)
    # role = forms.CharField(max_length=200)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('project', 'role')