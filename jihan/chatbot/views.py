from django.shortcuts import render

# Create your views here.

def chatbot(request):
    return render(request, 'chatbot.html')  # chatbot.html 템플릿을 렌더링

def page(request):
    # 'page.html'을 렌더링
    return render(request, 'page.html')