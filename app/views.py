from django.shortcuts import render

# Create your views here.

def condition(request):
    d={'a':120,'b':178,'c':190}
    return render(request,'condition.html',context=d)




def loop(request):
    d={'name':'VENKY'}
    return render(request,'loop.html',d)