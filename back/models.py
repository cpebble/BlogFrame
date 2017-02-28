from django.db import models
import datetime
#Reference: https://docs.djangoproject.com/en/1.10/ref/models/fields/

# Create your models here.
class Post(models.Model):
    postId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    shortTitle = models.CharField(max_length=20)

    created = models.DateTimeField(editable=False)
    published=models.DateTimeField()

    body = models.TextField()
    author=models.ForeignKey('Author', on_delete=models.CASCADE, blank=True, default=1)

    def save(self):
        if not self.postId:
            self.created = datetime.datetime.now()
        if not self.published:
            self.published = self.created
        if not self.shortTitle:
            self.shortTitle = self.title[0:20]
        super(Post, self).save()
    def __str__(self):
        return "%02d / %s - %s" % (self.created.day, self.created.month, self.shortTitle)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-published']

class Author(models.Model):
    name = models.CharField(max_length=100) #Fulde navn
    description = models.TextField(blank=True) #En personlig beskrivelse

    latest = models.IntegerField(blank=True, null=True) #Postid af den seneste indlæg

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name


class Dame:
    erModel = models.BooleanField(default=True)
    vilPåHotel = models.BooleanField(default=True)
    hotelPreference= models.CharField(default="D'angleterre")
    drinkPreference = models.CharField(default="Belvedere")
    siger = models.TextField(default=("Uhh ja"*3))
