from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .serializers import BookRecommendationSerializer ,CommentSerializer
from .models import BookRecommendation , Comment
from django.http import JsonResponse
from .utils import search_books
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


def book_search(request):
    query = request.GET.get('query', '')
    context = {}
    if query:
        data = search_books(query)
        if 'error' not in data:
            context['books'] = data
        else:
            context['error'] = data['error']
    return render(request, 'search.html', context)
    



class BookRecommendationListCreate(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = BookRecommendation.objects.all()
    serializer_class = BookRecommendationSerializer
    
class BookRecommendationDetail(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = BookRecommendation.objects.all()
    serializer_class = BookRecommendationSerializer
    
    
class CommentListCreate(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class CommentDetail(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    
    




