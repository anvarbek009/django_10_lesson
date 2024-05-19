from django.db import models
from users.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class CategoryBlog(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'category_blog'

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(CategoryBlog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'blog'

class Review(models.Model):
    comment=models.CharField(max_length=100)
    rating=models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    class Meta:
        db_table ='review'

    def __str__(self):
        return f'{self.rating} - {self.blog.title} review by {self.user.username}'