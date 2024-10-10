from django.db import models


class Member(models.Model):
    email = models.EmailField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128) 

    def __str__(self):
        return self.email;


class Chatbot(models.Model):
    question=models.TextField(db_index=True)  # 원천 질문 데이터 (학습 대상 데이터 예상)
    category=models.ForeignKey('chatbot.Category', on_delete=models.SET_NULL, null=True)
    answer=models.TextField()  # 로봇이 답변했던 데이터 (실시간 사용자 민원 분석 후 제출할 데이터)
    categoryId=models.IntegerField(null=False)  # 공공민원: 1, 건강/의료: 2

    def __str__(self):
        return self.category;