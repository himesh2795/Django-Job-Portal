from django.contrib import admin
from django.urls import path
from . views import views

urlpatterns = [
    path("", views.IndexPageView, name="indexpage"),
    path("login/", views.LoginPageView, name="loginpage"),
    path('register/', views.RegisterPageView, name='registerpage'),
    path('about/', views.AboutView, name='aboutpage'),
    path('logout/', views.LogoutView, name='logout'),
    path('search/', views.SearchJobView, name="search"),

    # Job Seeker
    path('job/home', views.JobSeekerViews.JobSeekerHomePage, name="jobseekerhomepage"),
    path('job/profile', views.JobSeekerViews.JobSeekerProfilePage, name='jonseekerprofilepage'),
    path('job/edit', views.JobSeekerViews.ProfileEdit, name='jobseekeredit'),
    path('job/details/<int:pk>', views.JobSeekerViews.ViewDetails, name='jobdetails'),
    path('job/apply/<int:pk>', views.JobSeekerViews.ApplyJob, name='applyjob'),
    path('job/apply', views.JobSeekerViews.ApplyJob, name='applied_jobs'),

    # Recruiter
    path('recruiter/home', views.RecruiterViews.RecruiterHomePage, name="recruiterhomepage"),
    path('recruiter/profile', views.RecruiterViews.RecruiterProfilePage, name='recruiterprofilepage'),
    path('recruiter/edit', views.RecruiterViews.ProfileEdit, name='recruiteredit'),
    path('recruiter/add_post', views.RecruiterViews.AddPost, name='addpost'),
    path('recruiter/details/<int:pk>', views.RecruiterViews.ViewDetails, name='details'),
    path('recruiter/applicants/<int:pk>', views.RecruiterViews.ApplicantsView, name='applicants'),
]
