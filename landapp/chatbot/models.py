from django.db import models

# Create your models here.


class Category(models.Model):
    category=models.TextField(max_length=100, null=False, db_index=True)
    # 민원 분류 카테고리

    def __str__(self):
        return self.category;


# 회원이 했던 질문과 답변 저장 테이블
class Complain(models.Model):
    author=models.ForeignKey('accounts.Member', on_delete=models.CASCADE, null=True)
    # 외래키 연결
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    timestamp=models.DateTimeField(auto_now_add=True)  # 작성날짜와 시간 타임스탬프 저장(객체 생성시 자동 생성)
    contents=models.TextField()  # 민원 내용
    robot=models.TextField()   # 로봇 답변 데이터

    def __str__(self):
        return self.contents;
