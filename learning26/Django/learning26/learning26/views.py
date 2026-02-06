from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("hello")
def ContactUs(request):
    return render(request,"contactus.html")
def Homepage(request):
    return render(request,"Home.html")
def AboutUs(request):
    return render(request,"About.html")
def Movies(request):
    return render(request,"movies.html")
def shows(request):
    return render(request,"shows.html")
def news(request):
    return render(request,"news.html")
def recipe(request):
    ingredient=["maggie","tomato"]
    data={"name":"maggie","time":2,"ingredient":ingredient}
    return render(request,"recipe.html",data)

def team(request):
    team=['MS Dhoni','Sanju Samson','Dewald Brevis','Ayush Mhatre','Urvil Patel']
    data={"captain":"RUTUU","Trophy":5,"team":team}
    return render(request,"team.html",data)
