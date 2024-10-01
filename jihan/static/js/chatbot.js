$(document).ready(function() {
    $('#chat-form').on('submit', function(e) {
        e.preventDefault();
        let userMessage = $('#user-input').val();
        
        $('#messages').append('<p><strong>You:</strong> ' + userMessage + '</p>');
        
        $.ajax({
            type: 'POST',
            url: '/chatbot/',  // URL을 명시적으로 정의
            data: {
                'message': userMessage,
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function(response) {
                console.log(response);  // 응답 내용을 콘솔에 출력하여 확인
                $('#messages').append('<p><strong>Bot:</strong> ' + response.response + '</p>');
                $('#user-input').val('');  // 입력창 초기화
            },
            error: function(error) {
                console.log("Error: ", error);  // 오류 내용 확인
            }
        });
    });
});
