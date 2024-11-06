$(document).ready(function () {
    $('a.nav-link').hover(
        function () {
            $(this).animate({ fontSize: '1.5em' }, 500);
        },
        function () {
            $(this).animate({ fontSize: '1em' }, 500);
        }
    );

    const hasierakoakSection = document.querySelector('.hasierakoak');
    const items = document.querySelectorAll('.carousel-item .item');

    const observerOptions = {
        root: hasierakoakSection,
        threshold: 1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                entry.target.style.opacity = '0';
                entry.target.style.transition = 'opacity 0.5s';
            } else {
                entry.target.style.opacity = '1';
            }
        });
    }, observerOptions);

    items.forEach(item => {
        observer.observe(item);
    });

    // Carrusel con soporte para arrastrar
    const carouselRow = document.getElementById('carouselRow');
    let isDragging = false;
    let startPos = 0;
    let currentTranslate = 0;
    let prevTranslate = 0;
    let animationID;

    // Ajustes para bucle
    const itemCount = items.length; // Número total de elementos
    const itemWidth = items[0].getBoundingClientRect().width; // Ancho de un elemento

    // Duplicar los elementos para crear un efecto de bucle
    const cloneFirst = items[0].cloneNode(true);
    const cloneLast = items[itemCount - 1].cloneNode(true);
    carouselRow.appendChild(cloneFirst);
    carouselRow.insertBefore(cloneLast, items[0]);

    // Actualiza el número de elementos después de duplicar
    const updatedItems = document.querySelectorAll('.carousel-item .item');
    const updatedItemCount = updatedItems.length; // Total de elementos después de la duplicación

    const setSliderPosition = () => {
        carouselRow.style.transform = `translateX(${currentTranslate}px)`;
    };

    const animation = () => {
        setSliderPosition();
        if (isDragging) requestAnimationFrame(animation);
    };

    carouselRow.addEventListener('mousedown', (event) => {
        isDragging = true;
        startPos = event.pageX;
        animationID = requestAnimationFrame(animation);
        carouselRow.style.cursor = 'grabbing';
    });

    carouselRow.addEventListener('mousemove', (event) => {
        if (isDragging) {
            const currentPosition = event.pageX;
            const distanceMoved = currentPosition - startPos;
            const speedFactor = 1.5; // Factor de velocidad
            currentTranslate = prevTranslate + distanceMoved * speedFactor;
        }
    });

    carouselRow.addEventListener('mouseup', () => {
        isDragging = false;
        cancelAnimationFrame(animationID);
        prevTranslate = currentTranslate;

        // Lógica para hacer que el carrusel sea cíclico
        if (currentTranslate < -((updatedItemCount - 1) * itemWidth)) {
            currentTranslate = -itemWidth; // Mueve a la segunda imagen (primer clon)
        } else if (currentTranslate > 0) {
            currentTranslate = -((updatedItemCount - 2) * itemWidth); // Mueve al último elemento antes del clon
        }

        setSliderPosition();
        carouselRow.style.cursor = 'grab';
    });

    carouselRow.addEventListener('mouseleave', () => {
        if (isDragging) {
            isDragging = false;
            cancelAnimationFrame(animationID);
            prevTranslate = currentTranslate;
            carouselRow.style.cursor = 'grab';
        }
    });

    // Para el caso de que el usuario suelte el ratón fuera del área del carrusel
    document.addEventListener('mouseup', () => {
        if (isDragging) {
            isDragging = false;
            cancelAnimationFrame(animationID);
            prevTranslate = currentTranslate;
            carouselRow.style.cursor = 'grab';
        }
    });
});
