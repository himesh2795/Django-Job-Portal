from django.contrib import admin
from .models import *

@admin.register(RecruiterTbl)
class RecruiterTblAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name", "email", "profile", "number")
    list_filter = ("organization",)

@admin.register(JobSeekerTbl)
class JobSeekerTblAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name", "email", "profile", "number", "resume")
    list_filter = ("email", )


@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ("recruiter", "position", "organization", "location", "posted_on")
    list_filter = ("recruiter", "position")

@admin.register(AppliedJobsTbl)
class AppliedJobsTblAdmin(admin.ModelAdmin):
    list_display = ("job_seeker","job_post", "applied_on")
    list_filter = ("job_post","job_seeker")