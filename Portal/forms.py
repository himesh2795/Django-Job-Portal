from django import forms
# from django.contrib.auth.models import User
from . models import *

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = "__all__"


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

    def __init__(self, *args, **kwargs):

        recruiter = kwargs.pop('recruiter_obj', '')
        print("RECRUITER : ", recruiter)
        super(JobPostForm, self).__init__(*args, **kwargs)
        self.fields['recruiter'] = recruiter[0]
        print("\n\n================== self.fields['recruiter'] ", self.fields['recruiter'],"=======\n\n")