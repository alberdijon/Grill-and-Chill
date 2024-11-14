$(document).ready(function(){
    $('a.nav-link').hover(
        function() {
            $(this).animate({ fontSize: '1.5em' }, 500);
        }, 
        function() {
            $(this).animate({ fontSize: '1em' }, 500);
        }
    );
    const gif = $('.products img');

    // Cuando se haga scroll en la página
    $(window).on('scroll', function() {
        // Obtener el desplazamiento vertical de la página
        const scrollPosition = $(window).scrollTop();
        
        // Calcular el movimiento del GIF basándonos en el desplazamiento
        // A medida que se baja, el GIF se moverá hacia la izquierda.
        const moveAmount = scrollPosition * 0.3; // Ajusta el factor para mayor o menor movimiento

        // Aplicar el movimiento al GIF en el eje X (horizontal)
        gif.css({
            transform: `translateX(${moveAmount}px)` // Mueve el GIF en el eje X
        });
    });
})