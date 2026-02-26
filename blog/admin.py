from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date','published_date', 'updated_date', 'views',)
    list_filter = ('created_date','published_date','updated_date')
    search_fields = ('title', 'content',)
    readonly_fields = ('views', 'updated_date')
    prepopulated_fields = {'slug': ('title',)}
