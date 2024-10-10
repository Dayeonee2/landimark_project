import sys
import os
import django, json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  

# 1. Django 설정 파일 경로 지정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'landapp.settings')

# 2. Django 환경 초기화
django.setup()

# 3. Django 모델 import
from accounts.models import Chatbot
from chatbot.models import Category


with open('landapp/chatbot/fixtures/public_data.json', 'r', encoding='utf-8-sig') as f:
    datas=json.load(f)

# 5. 데이터베이스에 저장
for data in datas:
    question = data['question']
    answer = data['answer']
    categoryId = data['categoryId']  # categoryId 사용

    # categoryId를 통해 Category 인스턴스를 가져옴
    try:
        category_instance = Category.objects.get(category_id=categoryId)
    except Category.DoesNotExist:
        print(f"Category with id {categoryId} does not exist")
        continue  # 해당 카테고리가 없으면 넘어감

    # Chatbot 인스턴스를 생성하고 저장
    Chatbot.objects.create(
        question=question,
        answer=answer,
        category=category_instance  # ForeignKey로 category 인스턴스 전달
    )

print('데이터베이스 저장 완료')