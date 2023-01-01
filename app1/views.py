from django.shortcuts import render

# Create your views here.
def opeartions(request):
    d={'a':22,'b':20,'c':30}
    return render(request,'operations.html',d)

