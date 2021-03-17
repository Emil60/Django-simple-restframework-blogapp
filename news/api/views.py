from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from news.models import News, Author
from .serializers import NewsSerializer, AuthorSerializer
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class AuthorListCreateAPIView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True, context={'request': request})
        return Response(serializer.data)


    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class based views
class NewsListCreateAPIView(APIView):
    def get(self, request):
        news = News.objects.filter(is_active=True)
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsDetailAPIView(APIView):
    def get_object(self, pk):
        news_instance = get_object_or_404(News, pk=pk)
        return news_instance

    def get(self, request, pk):
        news = self.get_object(pk=pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data)

    def put(self, request, pk):
        news = self.get_object(pk=pk)
        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        news = self.get_object(pk=pk)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# function based views
# @api_view(['GET', 'POST'])
# def news_list_create_api_view(request):
#     if request.method == "GET":
#         news = News.objects.filter(is_active=True)
#         serializer = NewsSerializer(news, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = NewsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(["GET", "PUT", "DELETE"])
# def news_detail_api_view(request, pk):
#     try:
#         news_instance = News.objects.get(pk=pk)
#     except News.DoesNotExist:
#         return Response({'errors': {'status': 404, 'message': "Couldn't find any news"}}, status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = NewsSerializer(news_instance)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = NewsSerializer(news_instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         news_instance.delete()
#         return Response({'action': {'status': 204, 'message': "news deleted"}}, status=status.HTTP_204_NO_CONTENT)
