from django.shortcuts import render, redirect
from Portal.serializers import *
from . import JobSeekerViews
from . import RecruiterViews
from Portal.forms import *
from datetime import datetime


# Create your views here.
def IndexPageView(request):
    if request.session.get('id'):
        if request.session['user_type'] == "job_seeker":
            id = request.session.get('id')
            obj = JobSeekerTbl.objects.filter(id=id)
            if obj:
                return redirect('jobseekerhomepage')

        if request.session['user_type'] == "recruiter":
            id = request.session.get('id')
            obj = RecruiterTbl.objects.filter(id=id)
            if obj:
                return redirect("recruiterhomepage")

    return render(request, "index.html")


def LoginPageView(request):
    if request.session.get('id'):
        if request.session['user_type'] == "job_seeker":
            id = request.session.get('id')
            obj = JobSeekerTbl.objects.filter(id=id)
            if obj:
                return redirect('jobseekerhomepage')

        if request.session['user_type'] == "recruiter":
            id = request.session.get('id')
            obj = RecruiterTbl.objects.filter(id=id)
            if obj:
                return redirect("recruiterhomepage")

    if request.method == "POST":
        if request.POST.get('user_type') == "job_seeker":
            user = JobSeekerTbl.objects.filter(email=request.POST.get('email'))
            if not user:
                return render(request, "login.html",
                              {"msg" + "_" + request.POST.get('user_type'): "Email id does not exist"})

            if user[0].password != request.POST.get('password'):
                return render(request, "login.html",
                              {"msg" + "_" + request.POST.get('user_type'): "Password is incorrect"})

            request.session['id'] = user[0].id
            request.session['user_type'] = request.POST.get('user_type')
            return redirect("jobseekerhomepage")

        if request.POST.get('user_type') == "recruiter":
            user = RecruiterTbl.objects.filter(email=request.POST.get('email'))
            if not user:
                return render(request, "login.html",
                              {"msg" + "_" + request.POST.get('user_type'): "Email id does not exist"})

            if user[0].password != request.POST.get('password'):
                return render(request, "login.html",
                              {"msg" + "_" + request.POST.get('user_type'): "Password is incorrect"})

            request.session['id'] = user[0].id
            request.session['user_type'] = request.POST.get('user_type')

            return redirect("recruiterhomepage")

    return render(request, "login.html")


def RegisterPageView(request):
    if request.session.get('id'):
        if request.session['user_type'] == "job_seeker":
            id = request.session.get('id')
            obj = JobSeekerTbl.objects.filter(id=id)
            if obj:
                return redirect('jobseekerhomepage')

        if request.session['user_type'] == "recruiter":
            id = request.session.get('id')
            obj = RecruiterTbl.objects.filter(id=id)
            if obj:
                return redirect("recruiterhomepage")

    try:
        if request.method == "POST":

            # To Check Password
            if request.POST.get('password') != request.POST.get('cpwd'):
                return render(request, "register.html", {
                    "msg" + "_" + request.POST.get('user_type'): "Password and Confirm Password Must be same"})

            # For Job Seeker
            if request.POST.get('user_type') == "job_seeker":
                # To find existing email
                user = JobSeekerTbl.objects.filter(email=request.POST.get('email'))
                if user:
                    return render(request, "register.html",
                                  {"msg" + "_" + request.POST.get('user_type'): "Email is already registered."})

                job_seeker_form = JobSeekerForm(request.POST)
                if job_seeker_form.is_valid():
                    job_seeker = job_seeker_form.save()
                    return redirect('loginpage')
                else:
                    form_error = job_seeker_form.errors
                    return render(request, "register.html", {"msg" + "_" + request.POST.get('user_type'): form_error})

            # For Recruiter
            if request.POST.get('user_type') == "recruiter":
                user = RecruiterTbl.objects.filter(email=request.POST.get('email'))
                if user:
                    return render(request, "register.html",
                                  {"msg" + "_" + request.POST.get('user_type'): "Email is already registered."})

                recruiter_form = RecruiterForm(request.POST)
                if recruiter_form.is_valid():
                    recruiter = recruiter_form.save()
                    return redirect('loginpage')
                else:
                    form_error = recruiter_form.errors
                    return render(request, "register.html", {"msg" + "_" + request.POST.get('user_type'): form_error})

        return render(request, "register.html")
    except Exception as e:
        try:
            user.delete()
        except:
            pass
        return render(request, "register.html", {"msg" + "_" + request.POST.get('user_type'): str(e)})


def AboutView(request):
    return render(request, "about.html")


def LogoutView(request):
    try:
        del request.session['id']
    except:
        pass

    try:
        del request.session['user_type']
    except:
        pass

    return redirect("indexpage")
