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

    const carouselRow = document.getElementById('carouselRow');
    let isDragging = false;
    let startPos = 0;
    let currentTranslate = 0;
    let prevTranslate = 0;
    let animationID;

   
    const itemCount = items.length; 
    const itemWidth = items[0].getBoundingClientRect().width;
    const cloneFirst = items[0].cloneNode(true);
    const cloneLast = items[itemCount - 1].cloneNode(true);
    carouselRow.appendChild(cloneFirst);
    carouselRow.insertBefore(cloneLast, items[0]);

    const updatedItems = document.querySelectorAll('.carousel-item .item');
    const updatedItemCount = updatedItems.length;

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
            const speedFactor = 1.5;
            currentTranslate = prevTranslate + distanceMoved * speedFactor;
        }
    });

    carouselRow.addEventListener('mouseup', () => {
        isDragging = false;
        cancelAnimationFrame(animationID);
        prevTranslate = currentTranslate;

        if (currentTranslate < -((updatedItemCount - 1) * itemWidth)) {
            currentTranslate = -itemWidth; 
        } else if (currentTranslate > 0) {
            currentTranslate = -((updatedItemCount - 2) * itemWidth); 
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

    document.addEventListener('mouseup', () => {
        if (isDragging) {
            isDragging = false;
            cancelAnimationFrame(animationID);
            prevTranslate = currentTranslate;
            carouselRow.style.cursor = 'grab';
        }
    });
    
});
let quantity = 1;

function openModal(title, description, price, imageUrl) {
    document.getElementById("modalTitle").innerText = title;
    document.getElementById("modalDescription").innerText = description;
    document.getElementById("modalPrice").innerText = `${price}€`;
    document.getElementById("modalImg").src = imageUrl;
    document.getElementById("quantity").innerText = quantity;
    document.getElementById("productModal").style.display = "block";
}

function closeModal() {
    document.getElementById("productModal").style.display = "none";
    quantity = 1; // Reiniciar la cantidad al cerrar
}

function changeQuantity(amount) {
    quantity += amount;
    if (quantity < 1) quantity = 1; // Evita que la cantidad sea menor que 1
    document.getElementById("quantity").innerText = quantity;
}