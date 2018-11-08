from django.shortcuts import render

# Create your views here.


def main(request):
    print("inside")
    return render(request,'home/index.html')