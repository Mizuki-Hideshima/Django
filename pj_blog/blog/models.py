from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self):
        return self.name

class Post(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False
    )

    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=False,
        null=False
    )
    
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    body = models.TextField(
        blank=False,
        null=False
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    title = models.ManyToManyField(
        Tag,
        blank=False,
    )

    def __str__(self):
        return self.title