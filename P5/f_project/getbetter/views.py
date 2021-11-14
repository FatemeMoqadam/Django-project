from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render , get_object_or_404
from .models import solution,feeling, solutionsong



def home_page(request):
    template = loader.get_template('getbetter/home_page.html')
    return render(request, 'getbetter/home_page.html')

def finish(request):
    template = loader.get_template('getbetter/finish.html')
    return render(request, 'getbetter/finish.html')


def feel(request):
    lfl = feeling.objects.order_by('-pub_date')[:9]
    return render(request, 'getbetter/feel.html',{'latest_feeling_list': lfl})

def result(request,id):
    sol = get_object_or_404(feeling, pk=id)
    return render (request, 'getbetter/result.html',{'feeling': sol})

def post_info(request):
    lfl = feeling.objects.all()
    if request.method == "POST":
       data = request.POST
       c = feeling.objects.get(feeling_text=data['feeling'])
       a = solution.objects.create(suggested_movie=data['suggested_movie'] , link=data['link'] , feeling = c)
       b = solutionsong.objects.create(suggested_song=data['suggested_song'] , link=data['link'] , feeling = c)       
       a.save()
       b.save()
       c.save()
       return render (request, 'getbetter/finish.html')
    if request.method == "GET":
        return render (request, 'getbetter/post_info.html',{'latest_feeling_list': lfl} )

def search(request):
    if request.method == "POST":
        query_name= request.POST["text"]
        if query_name:
            results=feeling.objects.filter(text_contains=query_name)
            return render (request, 'result2.html', {"result":results})
    return render(request, 'getbetter/search.html')        