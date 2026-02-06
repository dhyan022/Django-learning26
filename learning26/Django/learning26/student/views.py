from django.shortcuts import render
 
def marks(request):
    return render(request,"student/marks.html")

def info(request):
    data={"name":"sumit","std":"10th","DOB":10-5,"result":80}
    return render(request,"student/info.html",data)

def faculty(request):
    data={'sub1':'Maths','teacher1':'Dr. Meera Nair',"qual1":"Ph.D. Mathematics",
          'sub2':'English','teacher2':'Piyush Patel',"qual2":"M.A. English  Literatuer",
          'sub3':'Science','teacher3':'Harish singh',"qual3":"Msc. Physics"
          }
    return render(request,"student/faculty.html",data)

# Create your views here.