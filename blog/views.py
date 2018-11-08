from django.shortcuts import render

# Create your views here.


def main(request):
    print("hello")
    return render(request,'blog/blog.html')