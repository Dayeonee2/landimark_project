# views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import openai
import os
import time

# OpenAI API 키 설정



def chatbot(request):
    if request.method == 'POST':
        user_input = request.POST.get('message')
        
        try:
            # 2초 지연을 추가하여 요청 빈도 조절
            time.sleep(2)
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            chatbot_response = response['choices'][0]['message']['content'].strip()
        
        except openai.error.RateLimitError as e:
            print("RateLimitError:", str(e))
            return JsonResponse({'error': 'Rate limit exceeded. Please try again later.'})
        
        return JsonResponse({'response': chatbot_response})
    
    return render(request, 'chatbot.html')


def page(request):
    # 'page.html'을 렌더링
    return render(request, 'page.html')


# 회원가입 페이지 뷰
def sign(request):
    return render(request, 'sign.html')

# 회원가입 처리 뷰
def signup(request):
    if request.method == 'POST':
        # 회원 정보 처리 로직 (데이터베이스 저장 등)
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # 여기서 회원 정보를 저장하거나 처리합니다.
        
        # 회원가입 성공 메시지 띄우기
        return HttpResponse('<script>alert("회원가입에 성공하셨습니다!"); window.location.href="/chat/";</script>')
    return redirect('sign')

def chat(request):
    return render(request, 'chat.html')

def qr(request):
    return render(request, 'qr.html')

def test1(request):
    return render(request, 'test1.html') 

def test2(request):
    return render(request, 'test2.html') 