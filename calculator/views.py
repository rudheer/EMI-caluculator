from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')
def doit(request):
    p1=int(request.POST["num1"])
    r1=int(request.POST["num2"])
    t1=int(request.POST["num3"])
    p = p1
    t= t1
    r= r1
    r = r/100
    r = r/12
    t= t*12
    num = (1+r)**t
    num = num*p*r
    den = (1+r)**t-1
    res = num/den
    import math
    res = math.ceil(res)
    return render(request, 'results.html', {'result': res,'p': p1,'r': r1,'t': t1})
