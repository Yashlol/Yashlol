# App_43_3/forms.py
from django import forms
from .models import Resume, Experience, Skill, Project, Education

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'title', 'email', 'phone', 'about']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'company', 'date_range', 'description']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'link']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'year']
