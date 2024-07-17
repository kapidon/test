from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=10)

class Test(models.Model):
    name = models.CharField(max_length=10)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag, blank=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
