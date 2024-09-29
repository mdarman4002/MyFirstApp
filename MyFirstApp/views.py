from django.http import HttpResponse
from django.shortcuts import render
import datetime
def home(request):
    isActive = True
    if request.method == 'POST':
        #check = request.POST['check']
        check = request.POST.get("check")
        print(check)
        if check is None: isActive = False
        else: isActive = True
    date = datetime.datetime.now()
    
    name = "Arman"
    list_of_program = [
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime number from 1 to 100',
        'WAP to print pascals triangle'
    ]
    student ={
        'student_name' :"Faisal",
        'student_college':"AMZ",
        'student_city':"Motihari"
    }
    data={
        'date' :date,
        'isActive':isActive,
        'name':name,
        'list_of_program':list_of_program,
        'student_data':student
    }
    return render(request,"home.html", data)
   # print("test from views is called")
   # return render(request,"home.html", {})
   # return HttpResponse ("<h1> Hello this is index page </h1>" + str(date))
def about(request):
    date = datetime.datetime.now()
    print("about from views is called")
    return render(request, "about.html", {})
   # return HttpResponse ("<h1> Hello this is about page </h1>" + str(date))

def aboutProject(request):
    date = datetime.datetime.now()
    print("about from views is called")
    return render(request, "about-project.html", {})

def service(request):
    date = datetime.datetime.now()
    print("service from views is called")
    return render(request, "services.html", {})
    #return HttpResponse ("<h1> Hello this is service page </h1>" + str(date))