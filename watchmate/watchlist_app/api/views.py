from rest_framework.response import Response
from rest_framework.views import APIView
from watchlist_app.models import Watchlist,StreamPlatform
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer
from rest_framework import status






class WatchListAV(APIView):
    def get(self,request):
        movies = Watchlist.objects.all()
        serializer = WatchListSerializer(movies,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class WatchDetailAV(APIView):
    def get(self,request,pk):
        try:
            movie = Watchlist.objects.get(pk = pk)
        except Watchlist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    def put(self,request,pk):
        try:
            movie = Watchlist.objects.get(pk = pk)
        except Watchlist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        movie = Watchlist.objects.get(pk = pk)
        movie.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
    
class StreamiPlatformListAV(APIView):
    def get(self,request):
        plotform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(plotform, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StreamPlatformSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class StreamPlatformDetailAV(APIView):
    def get(self,request,pk):
        try:
            platfrom = StreamPlatform.objects.get(pk = pk)
        except StreamPlatform.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platfrom)
        return Response(serializer.data)
    def put(self,request,pk):
        try :
            platform = StreamPlatform.objects.get(pk =pk)  
        except StreamPlatform.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    
          
        
        
    
            
  

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def movie_details(request, pk):
#     try:
#         movie = Movie.objects.get(pk=pk)
#     except Movie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
