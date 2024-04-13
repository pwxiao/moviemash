from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from .models import *
import random


# Create your views here.
def index(request):
    return HttpResponse("Hello, world")


def vote_for_movies(request):
    # 从数据库中随机选择两部电影
    movies = list(Movie.objects.all())
    random_movies = random.sample(movies, 2)

    # if request.method == 'POST':
    #     # 处理用户的投票
    #     movie_id = request.POST.get('movie_id')
    #     rating = request.POST.get('rating')
    #     movie = Movie.objects.get(pk=movie_id)
    #     return HttpResponseRedirect('/')

    # 渲染 HTML 模板并传递随机选择的两部电影
    return render(request, 'votes/vote_for_movies.html', {
        'movie1': random_movies[0],
        'movie2': random_movies[1],
        'movie1_votes': random_movies[0].total_votes(),
        'movie2_votes': random_movies[1].total_votes()})


def vote(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        try:
            movie = Movie.objects.get(pk=movie_id)
            movie.vote()  # 调用电影的 vote 方法
            return JsonResponse({'status': 'success'})
        except Movie.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Movie not found'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def rank(request):
    # 获取所有电影
    movies = Movie.objects.all()

    # 创建一个包含电影标题和投票数的字典
    movie_data = [{'title': movie.title, 'total_votes': movie.total_votes()} for movie in movies]

    # 根据投票数对电影列表进行排序
    sorted_movie_data = sorted(movie_data, key=lambda x: x['total_votes'], reverse=True)

    return render(request, 'votes/rank.html', {'movie_data': sorted_movie_data})

