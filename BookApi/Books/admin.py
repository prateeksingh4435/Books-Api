from django.contrib import admin
from .models import BookRecommendation , Comment
# Register your models here.


# booksapi/admin.py



class BookRecommendationAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'user', 'created_at')
    search_fields = ('title', 'author', 'user__username')
    list_filter = ('created_at', 'author')
    date_hierarchy = 'created_at'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('recommendation', 'user', 'text', 'created_at')
    search_fields = ('recommendation__title', 'user__username', 'text')
    list_filter = ('created_at', 'user')
    date_hierarchy = 'created_at'

admin.site.register(BookRecommendation, BookRecommendationAdmin)
admin.site.register(Comment, CommentAdmin)
