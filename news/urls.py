from django.urls import path
from . import views


app_name='news'
urlpatterns = [
    path('create/', views.create_news, name='create'),
    path('category/<str:category>/', views.news_by_category, name ='category'),
    path('detail/<int:news_id>/', views.news_detail, name='detail')
]