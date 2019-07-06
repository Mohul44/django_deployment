from django.shortcuts import render

# Create your views here.
def index(request):
    citext_dict={'text':'hello world','number':4444}
    return render(request,'basic_app/index.html',context=citext_dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url.html')
