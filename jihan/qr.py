import qrcode
import os

# 개발자 소개 페이지 URL (로컬 서버 URL)
url = 'https://drive.google.com/file/d/1o8vYavusCO2z4JbZMfkCAYIqGxEjjdof/view?usp=sharing' 

# QR 코드 생성
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Django 프로젝트의 BASE_DIR 경로 가져오기
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 이미지 저장 경로 설정
output_dir = os.path.join(BASE_DIR, 'jihan/static/image/')
os.makedirs(output_dir, exist_ok=True)  # 폴더가 없으면 생성

# QR 코드 이미지 저장
img = qr.make_image(fill='black', back_color='white')
img.save(os.path.join(output_dir, 'google_drive_qr.png'))  # 이미지 저장 경로는 jihan/static/image/qr.png

