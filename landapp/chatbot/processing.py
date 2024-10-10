# chatbot/processing.py
import asyncio
import hashlib
import json
import sqlite3

# DB(SQLite) 답변을 가져오는 함수
def fetch_answer_from_db(question_hash):
    # SQLite DB 연결하기
    conn = sqlite3.connect('db.sqlite3')  
    cursor = conn.cursor()

    cursor.execute("SELECT answer FROM answers WHERE question_hash=?", (question_hash,))
    result = cursor.fetchone()
    
    conn.close()
    return result[0] if result else "답변을 찾을 수 없습니다."

# 비동기 배치 처리 함수
async def batch_process_requests(questions):
    print(f"Batch processing {len(questions)} questions...")
    await asyncio.sleep(2)  # 비동기적으로 2초 대기 (모델 처리 대신)

    # 각 질문에 대한 해시 값 생성
    responses = []
    for question in questions:
        question_hash = hashlib.sha256(question.encode()).hexdigest()
        response = fetch_answer_from_db(question_hash)
        responses.append({"answer": response})

    return responses

# 비동기 챗봇 함수 (질문 분석 및 캐시)
async def chatbot(question, batch_queue):
    future = asyncio.get_event_loop().create_future()
    batch_queue.append((question, future))

    # 배치 처리 완료될 때까지 대기
    return await future

# 배치 처리 관리
async def process_batch_queue(batch_queue, batch_interval=5):
    while True:
        if batch_queue:
            questions = [q[0] for q in batch_queue]
            futures = [q[1] for q in batch_queue]

            # 모델을 통해 배치 처리
            responses = await batch_process_requests(questions)

            # 응답을 사용자에게 전달
            for i, response in enumerate(responses):
                futures[i].set_result(response)

            # 처리 후 배치 큐 비우기
            batch_queue.clear()

        # 배치 주기 대기
        await asyncio.sleep(batch_interval)
