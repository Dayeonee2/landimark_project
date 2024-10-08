from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # 비밀번호는 해시 처리를 권장합니다.

    def __str__(self):
        return self.email

