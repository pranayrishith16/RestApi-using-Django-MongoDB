from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from .models import Movie
from .serializers import MovieSerializer

# Create your views here.


@csrf_exempt
def movie_list(request, id=0):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Adding Unsuccessful", safe=False)
    elif request.method == 'DELETE':
        movies = Movie.objects.get(id=id)
        movies.delete()
        return JsonResponse("Delete Successfully", safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        movie = Movie.objects.get(id=data['id'])
        serializer = MovieSerializer(movie, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Updating Unsuccessful", safe=False)
