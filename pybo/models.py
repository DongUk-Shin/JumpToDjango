from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200) #최대 200 문자열 저장 필드
    content = models.TextField()    #텍스트 필드
    create_date = models.DateTimeField() #질문이 생성된 날짜, 시간 저장
    
    def __str__(self): #id 값 대신 제목
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    #question 모델과의 관계를 나타내는 외래 키
    content = models.TextField()
    create_date = models.DateTimeField()