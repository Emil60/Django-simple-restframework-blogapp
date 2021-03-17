from django.urls import path
from . import views
# function based urls
# urlpatterns = [
#     path('news/', views.news_list_create_api_view, name='news_list'),
#     path('news/<int:pk>', views.news_detail_api_view, name='news_actions'),
# ]

# class based urls
urlpatterns = [
    path('authors/', views.AuthorListCreateAPIView.as_view(), name='author_list'),
    path('news/', views.NewsListCreateAPIView.as_view(), name='news_list'),
    path('news/<int:pk>', views.NewsDetailAPIView.as_view(), name='news_actions'),
]
