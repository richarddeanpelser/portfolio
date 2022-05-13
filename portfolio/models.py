from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Active"),
    (1,"Resigned")
)
class Company(models.Model):
    name: models.CharField(max_length=200,unique=True)
    country: models.CharField(max_length=100)
    city: models.CharField(max_length=100)
    slug: models.SlugField(max_length=200, unique=True)

class Role(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

class Project(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolio_Projects')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)    
    period = models.DateField()

    # class Meta:
    #     ordering = ['-created_at']

    def __str__(self):
        return self.title