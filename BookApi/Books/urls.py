from django.urls import path
from .views import book_search
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    path('search/', book_search, name='book_search'),
    path('recommendations/', views.BookRecommendationListCreate.as_view(), name='recommendation_list_create'),
    path('recommendations/<int:pk>/', views.BookRecommendationDetail.as_view(), name='recommendation_detail'),
    path('comments/', views.CommentListCreate.as_view(), name='comment_list_create'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment_detail'),
    
]