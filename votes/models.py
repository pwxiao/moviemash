from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField()
    votes = models.IntegerField(default=1) 
    def __str__(self) -> str:
        return self.title 
    def total_votes(self):
        return self.votes  # 使用反向关联计算与该电影相关的投票数

    def vote(self):
        self.votes += 1
        self.save()

