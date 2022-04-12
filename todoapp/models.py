from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    priority = models.IntegerField()
    completed = models.BooleanField()

    def __str__(self):
        return self.title + "|" + str(self.completed)
    


