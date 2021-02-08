from django import forms
from .models import *


class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = JobSeekerTbl
        exclude = ("resume", "resume_name")


class RecruiterForm(forms.ModelForm):
    class Meta:
        model = RecruiterTbl
        fields = "__all__"


class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        exclude = ("posted_on",)
