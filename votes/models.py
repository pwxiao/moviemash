from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField()
    def __str__(self) -> str:
        return self.title 
    def total_votes(self):
        return self.vote_set.count()  # 使用反向关联计算与该电影相关的投票数

    def vote(self):
        vote = Vote.objects.create(movie=self)
        vote.save()

class Vote(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    votes = models.IntegerField(default=1)  # 将默认值设置为1

    def __str__(self) -> str:
        return f"{self.movie}{self.votes}"
