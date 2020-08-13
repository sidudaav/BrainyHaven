from django.db import models

class Pattern(models.Model):
    content = models.CharField(null=True, max_length=200)
    answer = models.CharField(null=True, max_length=100)
    is_active = models.BooleanField(default=True)

class Analogy(models.Model):
    content = models.CharField(null=True, max_length=200)
    answer = models.CharField(null=True, max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Analogies"

class Riddle(models.Model):
    content = models.CharField(null=True, max_length=200)
    answer = models.CharField(null=True, max_length=100)
    is_active = models.BooleanField(default=True)