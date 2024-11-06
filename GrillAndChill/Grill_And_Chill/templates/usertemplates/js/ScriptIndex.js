$(document).ready(function(){
    $('a.nav-link').hover(
        function() {
            $(this).animate({ fontSize: '1.5em' }, 500);
        }, 
        function() {
            $(this).animate({ fontSize: '1em' }, 500);
        }
    );
    const scrollText = document.querySelector(".scroll-text");

    function handleScroll() {
        const textPosition = scrollText.getBoundingClientRect().top;
        const screenPosition = window.innerHeight / 1.3;

        // Verifica si el elemento está en la pantalla
        if (textPosition < screenPosition) {
            scrollText.classList.add("show");
            window.removeEventListener("scroll", handleScroll); // Remueve el event listener después de mostrar el texto
        }
    }

    window.addEventListener("scroll", handleScroll);
})