$(document).ready(function(){
    $('a.nav-link').hover(
        function() {
            $(this).animate({ fontSize: '1.4em' }, 500);
        }, 
        function() {
            $(this).animate({ fontSize: '1em' }, 500);
        }
    );
    const gif = $('.products img');

    $(window).on('scroll', function() {
        const scrollPosition = $(window).scrollTop();
        
        const moveAmount = scrollPosition * 0.3; 
        gif.css({
            transform: `translateX(${moveAmount}px)` 
        });
    });
})