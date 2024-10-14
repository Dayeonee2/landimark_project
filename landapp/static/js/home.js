document.addEventListener('DOMContentLoaded', () => {
    const header = document.querySelector('.header');
    const navLinks = document.querySelectorAll('.nav-link');
    const menuToggle = document.querySelector('.menu-toggle');
    const navbar = document.querySelector('.navbar');
    const video = document.querySelector('.background-video');
    const talkBtn = document.querySelector('.talk-btn');
    
    
    window.addEventListener('scroll', () => {
        // Toggle header background on scroll
        header.classList.toggle('scrolled', window.scrollY > 50);

        // Highlight active link based on scroll position
        navLinks.forEach(link => {
            const section = document.querySelector(link.getAttribute('href'));
            const sectionTop = section.offsetTop - 100;
            const sectionHeight = section.offsetHeight;

            // Adjusted condition to include the last section more robustly
            if (window.scrollY >= sectionTop && window.scrollY < (sectionTop + sectionHeight + 10) ||
                (window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });
    });

    // Toggle mobile menu
    menuToggle.addEventListener('click', () => {
        navbar.classList.toggle('open');
    });
    
    
    // 비디오 종료 시 랜디랑 대화하기 버튼 표시
    // 영상이 끝나기 1초 전에 마지막 프레임에서 멈추기
    video.addEventListener('timeupdate', () => {
        if (video.duration - video.currentTime <= 16) { // 마지막 1초 남았을 때
            video.pause();
            talkBtn.style.visibility = 'visible';
            talkBtn.style.opacity = '1';
            talkBtn.style.transform = 'translate(-50%, -50%) scale(1)'; // 애니메이션 시작
            
        }
});

    // Smooth scroll and close mobile menu on link click
    navLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault();
            const section = document.querySelector(link.getAttribute('href'));
            const offset = 60;
            const sectionPosition = section.offsetTop - offset;
            window.scrollTo({ top: sectionPosition, behavior: 'smooth' });

            if (navbar.classList.contains('open')) {
                navbar.classList.remove('open');
            }
        });
    });
});
