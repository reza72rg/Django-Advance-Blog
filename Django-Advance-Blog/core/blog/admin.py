from django.contrib import admin
from blog.models import Post,Category
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    def get_fields(self, request, obj=None):
        return ["image", "author", "title", "content", "category", "status", "published_date"]

    def get_list_display(self, request):
        return ["author", "title", "status"]

    def get_search_fields(self, request):
        return ["author", "title", "status"]

    def get_list_filter(self, request, filters=None):
        return ["author", "title", "status"]


admin.site.register(Category)
