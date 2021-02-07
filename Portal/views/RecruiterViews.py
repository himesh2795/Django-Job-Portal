from django.shortcuts import render, redirect
from Portal.forms import *
from Portal.models import *

def RecruiterHomePage(request):
    if not request.session.get('id'):
        return redirect('loginpage')
    id = request.session.get('id')
    obj = RecruiterTbl.objects.filter(id=id)
    if not obj:
        return redirect('loginpage')

    posts = JobPost.objects.filter(recruiter=obj[0]).order_by('-posted_on')
    return render(request, "recruiter/home.html", {"first_name":obj[0].first_name, "posts":posts})

def RecruiterProfilePage(request):
    if not request.session.get('id'):
        return redirect('loginpage')
    id = request.session.get('id')
    obj = RecruiterTbl.objects.filter(id=id)
    if not obj:
        return redirect('loginpage')

    return render(request, "recruiter/profile.html", {"user": obj[0]})

def ProfileEdit(request):
    if not request.session.get('id'):
        return redirect('loginpage')
    id = request.session.get('id')
    obj = RecruiterTbl.objects.filter(id=id)
    if not obj:
        return redirect('loginpage')
    
    if request.method== "POST":
        form = RecruiterForm(request.POST, instance=obj[0])
        if form.is_valid():
            user = form.save()
        else:
            form_error = form.errors
            
            # print({"msg"+"_"+request.POST.get('user_type'):form_error})
            return render(request, "recruiter/edit.html", {"msg":form_error, "user":obj[0]})
        

        return redirect("recruiterprofilepage") 
    return render(request, "recruiter/edit.html", {"user":obj[0]})

def AddPost(request):
    if not request.session.get('id'):
        return redirect('loginpage')
    id = request.session.get('id')
    obj = RecruiterTbl.objects.filter(id=id)
    if not obj:
        return redirect('loginpage')
    
    if request.method=="POST":
        print("\n\nREQUEST DATA : ", request.POST)
        # form = JobPostForm(request.POST, recruiter_obj=obj)
        # print("\n\nFORM : ", form, "/n/n")
        # print("Form Fields : ", form.fields, "/n/n")
        # if form.is_valid():
            # job_post = form.save()
        # else:
        try:
            position = request.POST.get('position')
            organization = request.POST.get('organization')
            location = request.POST.get('location')
            salary = request.POST.get('salary')
            skills = request.POST.get('skills')
            responsibilites = request.POST.get('responsibilites')
            profile = request.POST.get('profile')
            education = request.POST.get('education')

            job_post_obj = JobPost.objects.create(
                recruiter = obj[0],
                position=position, 
                organization=organization, 
                location=location, 
                salary=salary, 
                skills=skills, 
                responsibilites=responsibilites, 
                profile = profile,
                education = education
            )

        except Exception as e:
            return render(request, "recruiter/add_post.html", {"msg":str(e), "user":obj[0]})

        return redirect('recruiterhomepage')
    return render(request, "recruiter/add_post.html", {"user":obj[0]})

def ViewDetails(request, pk=None):
    if not request.session.get('id'):
        return redirect('loginpage')
    id = request.session.get('id')
    obj = RecruiterTbl.objects.filter(id=id)
    if not obj:
        return redirect('loginpage')

    post = JobPost.objects.filter(pk=pk)
    print("POST : ", post)
    if post:
        print("\n RESPONS : ", post[0].responsibilites.split("\n"))
        post[0].responsibilites = [line.strip('-') for line in post[0].responsibilites.split("\n") if line.strip()]
        post[0].profile = [line.strip('-') for line in post[0].profile.split("\n") if line.strip()]
        post[0].education = [line.strip('-') for line in post[0].education.split("\n") if line.strip()]
        return render(request, "recruiter/job_details.html", {"post":post[0]})
    else:
        return redirect('recruiterhomepage')

def ApplicantsView(request, pk=None):
    if not request.session.get('id'):
        return redirect('loginpage')
    id = request.session.get('id')
    obj = RecruiterTbl.objects.filter(id=id)
    if not obj:
        return redirect('loginpage')

    applicants = AppliedJobsTbl.objects.filter(job_post=pk)
    return render(request, "recruiter/applicants.html", {"applicants":applicants,"first_name":obj[0].first_name})

