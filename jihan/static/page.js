document.addEventListener('DOMContentLoaded', function () {
    // "챗봇 시작하기" 버튼 클릭 시 챗봇 페이지로 이동
    document.querySelector('.start-chatbot').addEventListener('click', function () {
        window.location.href = '/chatbot/';
    });
});
