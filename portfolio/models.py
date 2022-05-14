from django.db import models
from django.contrib.auth.models import User
import uuid
from ckeditor_uploader.fields import RichTextUploadingField

ROLE_STATUS = (
    (0,"Active"),
    (1,"Resigned")
)

PROJECT_STATUS = (
    (0,"Active"),
    (1,"Completed")
)

class Role(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    Organisation = models.CharField(max_length=100, unique=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=ROLE_STATUS, default=0)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True)
    body = RichTextUploadingField()
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title        

class Skill(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    logo = models.ImageField(null=True, default="skill.png")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


# class Project(models.Model):
#     title = models.CharField(max_length=300, unique=True)
#     description = models.CharField(max_length=1000)
#     slug = models.SlugField(max_length=300, unique=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolio_Projects')
#     details = models.TextField()
#     status = models.IntegerField(choices=PROJECT_STATUS, default=0)    
#     period = models.DateField()
 
#     class Meta:
#         ordering = ['period']

#     def __str__(self):
#         return self.title