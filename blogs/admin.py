from django.contrib import admin
from .models import Blog,CategoryBlog,Review
# Register your models here.

admin.site.register(Blog)
admin.site.register(CategoryBlog)
admin.site.register(Review)
