from django.db import models
from django.contrib.auth.models import User
import uuid
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

ROLE_STATUS = (
    (0,"Active"),
    (1,"Resigned")
)

PROJECT_STATUS = (
    (0,"Active"),
    (1,"Completed")
)

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Role(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    organisation = models.CharField(max_length=100, unique=True)
    body = RichTextUploadingField(null = True, blank=True)
    status = models.IntegerField(choices=ROLE_STATUS, default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.title)
            has_slug = Role.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count)
                has_slug = Role.objects.filter(slug=slug).exists()
                self.slug = slug

        super().save(*args, **kwargs)



class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.ImageField(null=True)
    body = RichTextUploadingField()
    project_url = models.URLField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)
    tags = models.ManyToManyField(Tag, blank=True)                      

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.title)
            has_slug = Project.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count)
                has_slug = Project.objects.filter(slug=slug).exists()
                self.slug = slug

        super().save(*args, **kwargs)
        		

class Skill(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    logo = models.ImageField(null=True, default="skill.png")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title



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