from django.db import models
# from django.contrib.auth.models import User, Group


# Create your models here.
# class User(models.Model):


#     def __str__(self):
#         return self.email

class RecruiterTbl(models.Model):
    # user = models.OneToOneField(User, related_name='recruiter', on_delete=models.CASCADE)
    first_name = models.CharField(null=False, max_length=250)
    last_name = models.CharField(null=False, max_length=250)
    email = models.CharField(null=False, max_length=250, unique=True)
    password = models.CharField(null=False, max_length=250)
    profile = models.CharField(max_length=250, null=True)
    number = models.IntegerField(null=True)
    organization = models.CharField(null=False, max_length=250)
    location = models.CharField(max_length=250, null=False)
    # profile = models.CharField(max_length=250, null=False)

    # user_type = models.CharField(max_length=250, null=True)

    class Meta:
        verbose_name = "Recruiter"
        verbose_name_plural = "Recruiters"

    def __str__(self):
        return self.email


class JobSeekerTbl(models.Model):
    # user = models.OneToOneField(User, related_name='job_seeker', on_delete=models.CASCADE)
    # user_type = models.CharField(max_length=250, null=True)
    # profile = models.CharField(max_length=250, null=True)
    first_name = models.CharField(null=False, max_length=250)
    last_name = models.CharField(null=False, max_length=250)
    email = models.CharField(null=False, max_length=250, unique=True)
    password = models.CharField(null=False, max_length=250)
    profile = models.CharField(max_length=250, null=True)
    number = models.IntegerField(null=True)
    resume = models.FileField(upload_to='documents/', null=True, blank=True)
    resume_name = models.CharField(null=True, blank=True, max_length=500)

    class Meta:
        verbose_name = "Job Seeker"
        verbose_name_plural = "Job Seekers"

    def __str__(self):
        return self.email


class JobPost(models.Model):
    recruiter = models.ForeignKey(
        RecruiterTbl, related_name="recruiter", on_delete=models.CASCADE)
    position = models.CharField(max_length=250)
    organization = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    salary = models.CharField(max_length=500)
    skills = models.CharField(max_length=1000)

    responsibilites = models.TextField()
    profile = models.TextField()
    education = models.TextField()

    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.position

class AppliedJobsTbl(models.Model):
    job_post = models.ForeignKey(JobPost, related_name='job_post', on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(JobSeekerTbl, related_name='job_seeker', on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Applied Job"
        verbose_name_plural = "Applied Jobs"

