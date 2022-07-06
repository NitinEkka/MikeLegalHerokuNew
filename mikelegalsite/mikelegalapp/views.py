from django.shortcuts import render , redirect
from .forms import MovieForm
from .models import Movie_List
# Create your views here.
def movie_list(request):
    context = {'movie_list':Movie_List.objects.all()}
    return render(request, "mikelegalapp/movie_list.html", context)

def movie_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = MovieForm()
        else:
            movie = Movie_List.objects.get(pk=id)
            form = MovieForm(instance=movie)
        return render(request, "mikelegalapp/movie_form.html", {'form': form})
    else:
        if id == 0:
            form = MovieForm(request.POST)
        else:
            movie = Movie_List.objects.get(pk=id)
            form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
        return redirect('/movie/list')


def movie_delete(request, id):
    movie = Movie_List.objects.get(pk=id)
    movie.delete()
    return redirect('/movie/list')