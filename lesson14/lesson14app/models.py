from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    tags = models.ManyToManyField(Tag,
                                  null=True)

    def __str__(self):
        return f"{self.name} - {self.text}"



