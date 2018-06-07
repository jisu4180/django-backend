from django.db import models
from django.utils import timezone


class Post(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # 타 모델에 대한 링크
    title = models.CharField(max_length=200) # 글자수가 제한된 텍스
    text = models.TextField() # 글자수 제한없는 텍스트
    created_date = models.DateTimeField(
            default=timezone.now)  #날짜 및 시간
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
