from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from landapp.accounts.models import Member


def sign_up(request):
    # 회원가입 양식 작성했을 때
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f'name:{name}, email:{email}, password:{password}')

        member = Member(name=name, email=email, password=password)
        member.save()  # SQLite 저장

        content={
            'user_name':name,
        }
        return render(request, 'account/index.html', content)

    return render(request, 'account/signup.html')


def index(request):
    error_message = None
    user_email = request.session.get('user_email')
    user_name = request.session.get('user_name')

    if request.method == "POST":
        # 로그인 정보가 제출되었을 때
        email = request.POST.get('user_email')
        password = request.POST.get('user_passwd')

        try:
            member = Member.objects.get(email=email, password=password)
            # 사용자 정보가 있는 경우에는 세션에 저장하기
            request.session['user_email']=member.email
            request.session['user_name']=member.name
            return redirect('index')
        
        except Member.DoesNotExist:
            # 로그인 실패 시 에러 메시지 띄우기
            error_message = "이메일 또는 비밀번호가 잘못되었습니다."
            messages.error(request, error_message)

    content={
        'user_email':user_email,
        'user_name':user_name,
        'error_message':error_message,
    }

    return render(request, 'account/index.html', content);

def logout(request):
    # 세션에서 사용자 정보 삭제
    request.session.pop('user_email', None)
    request.session.pop('user_name', None)
    messages.success(request, "로그아웃되었습니다.")  # 로그아웃 메시지
    return redirect('index');
