from django.shortcuts import render, redirect
from Portal.models import *
from django.core.files.storage import FileSystemStorage
from Portal.forms import *
import os


def JobSeekerHomePage(request):
    if not request.session.get('id'):
        return redirect('loginpage')
    job_seeker_id = request.session.get('id')
    job_seeker_obj = JobSeekerTbl.objects.filter(id=job_seeker_id)
    if not job_seeker_obj:
        return redirect('loginpage')

    jobs = JobPost.objects.all().order_by('-posted_on')
    applied_jobs = AppliedJobsTbl.objects.filter(job_seeker=job_seeker_obj[0])
    data = []
    for job in jobs:
        found_applied = False
        for applied_job in applied_jobs:
            if job == applied_job.job_post:
                found_applied = True

        if not found_applied:
            data.append(job)

    return render(request, "job_seeker/home.html", {"first_name": job_seeker_obj[0].first_name, "jobs": data})


def JobSeekerProfilePage(request):
    if not request.session.get('id'):
        return redirect('loginpage')
    job_seeker_id = request.session.get('id')
    job_seeker_obj = JobSeekerTbl.objects.filter(id=job_seeker_id)
    if not job_seeker_obj:
        return redirect('loginpage')

    if request.method == "POST":
        if request.FILES and request.FILES.get('resume'):
            resume = request.FILES['resume']

            fs = FileSystemStorage()
            filename = fs.save(resume.name, resume)
            uploaded_file_url = fs.url(filename)

            job_seeker_obj[0].resume = uploaded_file_url
            job_seeker_obj[0].resume_name = filename
            job_seeker_obj[0].save()

            write_path = os.getcwd() + "/media/media/"
            read_path = os.getcwd() + "/media/"

            with open(read_path + filename, "rb") as f:
                res_file = f.read()
                f.close()

            with open(write_path + filename, "wb") as f:
                f.write(res_file)
                f.close()
        else:
            pass

    return render(request, "job_seeker/profile.html", {"user": job_seeker_obj[0]})


def ProfileEdit(request):
    if not request.session.get('id'):
        return redirect('loginpage')
    job_seeker_id = request.session.get('id')
    job_seeker_obj = JobSeekerTbl.objects.filter(id=job_seeker_id)
    if not job_seeker_obj:
        return redirect('loginpage')

    if request.method == "POST":

        job_seeker_form = JobSeekerForm(
            request.POST, instance=job_seeker_obj[0])
        if job_seeker_form.is_valid():
            job_seeker = job_seeker_form.save()
        else:
            form_error = job_seeker_form.errors

            return render(request, "job_seeker/edit.html", {"msg": form_error, "user": job_seeker_obj[0]})

        return redirect("jonseekerprofilepage")
    return render(request, "job_seeker/edit.html", {"user": job_seeker_obj[0]})


def ViewDetails(request, pk=None):
    logged = True
    if not request.session.get('id'):
        logged = False

        # return redirect('loginpage')
    # job_seeker_id = request.session.get('id')
    # job_seeker_obj = JobSeekerTbl.objects.filter(id=job_seeker_id)
    # if not job_seeker_obj:
    #     return redirect('loginpage')

    post = JobPost.objects.filter(pk=pk)
    if post:
        post[0].responsibilites = [line.strip(
            '-') for line in post[0].responsibilites.split("\n") if line.strip()]
        post[0].profile = [line.strip(
            '-') for line in post[0].profile.split("\n") if line.strip()]
        post[0].education = [line.strip(
            '-') for line in post[0].education.split("\n") if line.strip()]

        if logged: 
            job_seeker_obj = JobSeekerTbl.objects.filter(id=request.session.get('id'))
            exist = AppliedJobsTbl.objects.filter(
                job_post=post[0], job_seeker=job_seeker_obj[0])
            if exist:
                return render(request, "recruiter/job_details.html", {"post": post[0], "msg": "Applied"})

        return render(request, "job_seeker/job_details.html", {"post": post[0], "logged":logged, "login_msg":"Login to Apply"})
    else:
        return redirect('jobseekerhomepage')


def ApplyJob(request, pk=None):
    if not request.session.get('id'):
        return redirect('loginpage')
    job_seeker_id = request.session.get('id')
    job_seeker_obj = JobSeekerTbl.objects.filter(id=job_seeker_id)
    if not job_seeker_obj:
        return redirect('loginpage')

    if pk:
        job_post = JobPost.objects.filter(pk=pk)
        if job_post:
            try:
                applied_job = AppliedJobsTbl.objects.create(
                    job_post=job_post[0], job_seeker=job_seeker_obj[0])
            except Exception as e:
                return render(request, "job_seeker/job_details.html", {"post": job_post[0], "msg": str(e)})

        return redirect('jobseekerhomepage')

    applied_jobs = AppliedJobsTbl.objects.filter(job_seeker=job_seeker_obj[0])
    job_posts = [job.job_post for job in applied_jobs]

    return render(request, "job_seeker/applied_jobs.html",
                  {"jobs": job_posts, "first_name": job_seeker_obj[0].first_name})
