from django.db import models
from django.contrib.auth.models import User
# Create your models here.
prior = [
        ('low','LOW'),
        ('medium',"MEDIUM"),
        ('high','HIGH')
    ]
class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField(null=True,blank=True)

    priority = models.CharField(choices=prior,max_length=10)
    status = models.CharField(choices=[('pending','PENDING'),('in progress','IN PROGRESS'),('completed','COMPLETED')],max_length=20)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title