from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from .models import Member  # Member 모델을 import
# 이 부분은 나중에 추가할 수 있습니다. 
# models.py에 Member 모델을 정의하고, 필요한 필드를 추가합니다.

def sign_up(request):
    # 회원가입 양식 작성했을 때
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # MySQL 연결 및 데이터 삽입
        with connection.cursor() as cursor:
            query = "INSERT INTO member (name, email, password) VALUES (%s, %s, %s);"
            cursor.execute(query, (name, email, password))
            connection.commit()  # 변경사항 커밋

        messages.success(request, "회원가입이 완료되었습니다!")  # 성공 메시지
        return redirect('index')  # 가입 후 인덱스 페이지로 리다이렉트

    return render(request, 'signup.html')

def index(request):
    error_message = None
    user_email = request.session.get('user_email')
    user_name = request.session.get('user_name')

    if request.method == "POST":
        # 로그인 정보가 제출되었을 때
        email = request.POST.get('user_email')
        password = request.POST.get('user_passwd')

        # MySQL에서 사용자 정보 조회
        with connection.cursor() as cursor:
            query = "SELECT name, email FROM member WHERE email = %s AND password = %s;"
            cursor.execute(query, (email, password))
            member = cursor.fetchone()

        if member:
            request.session['user_email'] = member[1]  # 세션에 email 저장
            request.session['user_name'] = member[0]  # 세션에 name 저장
            return redirect('index')
        else:
            error_message = "이메일 또는 비밀번호가 잘못되었습니다."
            messages.error(request, error_message)  # 에러 메시지 표시

    print('email:', user_email)
    print('error_msg:', error_message)
    return render(request, 'index.html', {
        'user_email': user_email,
        'user_name': user_name,
        'error_message': error_message,
    })

def logout(request):
    # 세션에서 사용자 정보 삭제
    request.session.pop('user_email', None)
    request.session.pop('user_name', None)
    messages.success(request, "로그아웃되었습니다.")  # 로그아웃 메시지
    return redirect('index')
