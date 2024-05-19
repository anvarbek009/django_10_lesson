from django.urls import path
from .views import ListView, BlogListView,BlogDetailView,BlogCreateView,BlogDeleteView,AddReviewView,ReviewDeleteView,ReviewUpdateView

app_name = 'blogs'
urlpatterns = [
    path('blogs/',BlogListView.as_view(),name='blog_list'),
    path('deatail/<int:pk>',BlogDetailView.as_view(),name='blog_detail'),
    path('create/',BlogCreateView.as_view(),name='blog_create'),
    path('delete/<int:pk>',BlogDeleteView.as_view(),name='blog_delete'),
    path('add_review/<int:pk>', AddReviewView.as_view(), name='add_review'),  
    path('review_delete/<int:pk>', ReviewDeleteView.as_view(), name='review_delete'),
    path('review_update/<int:pk>', ReviewUpdateView.as_view(), name='review_update'),
]