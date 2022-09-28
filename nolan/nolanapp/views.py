from tkinter.tix import Form
from django.shortcuts import render,redirect,get_object_or_404
from nolanapp.models import Movie
from nolanapp import forms

# Create your views here.
def index(request):
    data = Movie.objects.all()
    query = request.GET.get("Movie")
    if query:
        data = data.filter(name__icontains=query)
    return render(request,"index.html",{"all":data})


def add_movie(request):
    data = forms.MovieForm()
    if request.method == "POST":
        data = forms.MovieForm(request.POST,request.FILES)
        
        if data.is_valid():
            data.save()
            return redirect('/')
        else:
            print('Error')
            
    return render(request,"add_movie.html",{"form":data})

def imdb(request):
    return render(request,'imdb.html')

def detail(request,id):
    bk = Movie.objects.get(id=id)
    return render(request,"detail.html",{"pro":bk})


def update(request,id):
    data = forms.MovieForm()
    if request.method == "POST":
        obj = get_object_or_404(Movie,id=id)
        data = forms.MovieForm(request.POST,request.FILES,instance=obj)
        if data.is_valid():
            data.save()
            return redirect('/')
        else:
            print("Error")
            
    return render(request,"update.html",{"form":data})

def delete(request,id):
    data = get_object_or_404(Movie,id=id)
    if request.method =="POST":
        data.delete()
        return redirect('/')    
    return render(request,"delete.html")