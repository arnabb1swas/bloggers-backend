from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.urls import reverse


# Create your models here.
from .utils import slugifyInstanceTitle

User = settings.AUTH_USER_MODEL


class QuerySet(models.QuerySet):

    def search(self, query=None):
        if query is None:
            return self.all()
        elif query == "":
            return self.none()  # [] empty query list

        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups)


class BlogManager(models.Manager):
    def get_queryset(self):  # query search funtion has been called
        # searching the query through default queary search funtion
        return QuerySet(self.model, using=self._db)

    def search(self, query=None):  # searching the query user gave
        return self.get_queryset().search(query=query)  # calling the query search funtion


class blog(models.Model):
    author = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=80,
                            blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateField(
        auto_now_add=False, auto_now=False, blank=True, null=True)

    objects = BlogManager()

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.slug is None:
            slugifyInstanceTitle(self, save=False)
        super().save(*args, **kwargs)


def blogPostSave(sender, instance, created, *args, **kwargs):
    print(post_save)
    if created:
        slugifyInstanceTitle(instance, save=True)


# to connect the articlepostsave with the post_save ||  post_save.connect(def_name that has to be connected, sender=classname trough which it will connect)
post_save.connect(blogPostSave, sender=blog)
