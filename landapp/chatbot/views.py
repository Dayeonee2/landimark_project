from django.shortcuts import render
from django.http import JsonResponse
import json
import asyncio

from .processing import chatbot, process_batch_queue

# 배치 처리를 위해 다중 사용자의 질문 대기 큐
batch_queue = []

# 배치 처리 백그라운드 태스크 실행
asyncio.create_task(process_batch_queue(batch_queue))

def ask(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question = data.get('question')

        # 비동기 챗봇 처리 함수 호출
        response = asyncio.run(chatbot(question, batch_queue))
        
        return JsonResponse({"response": response})

    return render(request, 'chatbot/ask.html')
