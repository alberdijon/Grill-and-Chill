$(document).ready(function () {
  $("a.nav-link").hover(
    function () {
      $(this).animate({ fontSize: "1.5em" }, 500);
    },
    function () {
      $(this).animate({ fontSize: "1em" }, 500);
    }
  );

  const hasierakoakSection = document.querySelector(".hasierakoak");
  const items = document.querySelectorAll(".carousel-item .item");

  const observerOptions = {
    root: hasierakoakSection,
    threshold: 1,
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) {
        entry.target.style.opacity = "0";
        entry.target.style.transition = "opacity 0.5s";
      } else {
        entry.target.style.opacity = "1";
      }
    });
  }, observerOptions);

  items.forEach((item) => {
    observer.observe(item);
  });

  const carouselRow = document.getElementById("carouselRow");
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

  const updatedItems = document.querySelectorAll(".carousel-item .item");
  const updatedItemCount = updatedItems.length;

  const setSliderPosition = () => {
    carouselRow.style.transform = `translateX(${currentTranslate}px)`;
  };

  const animation = () => {
    setSliderPosition();
    if (isDragging) requestAnimationFrame(animation);
  };

  carouselRow.addEventListener("mousedown", (event) => {
    isDragging = true;
    startPos = event.pageX;
    animationID = requestAnimationFrame(animation);
    carouselRow.style.cursor = "grabbing";
  });

  carouselRow.addEventListener("mousemove", (event) => {
    if (isDragging) {
      const currentPosition = event.pageX;
      const distanceMoved = currentPosition - startPos;
      const speedFactor = 1.5;
      currentTranslate = prevTranslate + distanceMoved * speedFactor;
    }
  });

  carouselRow.addEventListener("mouseup", () => {
    isDragging = false;
    cancelAnimationFrame(animationID);
    prevTranslate = currentTranslate;

    if (currentTranslate < -((updatedItemCount - 1) * itemWidth)) {
      currentTranslate = -itemWidth;
    } else if (currentTranslate > 0) {
      currentTranslate = -((updatedItemCount - 2) * itemWidth);
    }

    setSliderPosition();
    carouselRow.style.cursor = "grab";
  });

  carouselRow.addEventListener("mouseleave", () => {
    if (isDragging) {
      isDragging = false;
      cancelAnimationFrame(animationID);
      prevTranslate = currentTranslate;
      carouselRow.style.cursor = "grab";
    }
  });

  document.addEventListener("mouseup", () => {
    if (isDragging) {
      isDragging = false;
      cancelAnimationFrame(animationID);
      prevTranslate = currentTranslate;
      carouselRow.style.cursor = "grab";
    }
  });
});
let quantity = 1;

function changeQuantity(amount) {
  quantity += amount;
  if (quantity < 1) quantity = 1;
  document.getElementById("quantity").innerText = quantity;
  
  document.getElementById("quantity-input").innerText = quantity;
  document.getElementById("quantity-input").value = quantity;
}

function toggleHasierakoak() {
  const productContainer = document.getElementById("productContainer");
  const toggleArrow = document.getElementById("toggleArrow");

  productContainer.classList.toggle("hidden");
  productContainer.classList.toggle("visible");

  toggleArrow.classList.toggle("rotated");
}
function toggleHanburgesak() {
  const productContainer = document.getElementById("productContainer2");
  const toggleArrow = document.getElementById("toggleArrow2");

  productContainer.classList.toggle("hidden");
  productContainer.classList.toggle("visible");

  toggleArrow.classList.toggle("rotated");
}
function togglePostreak() {
  const productContainer = document.getElementById("productContainer3");
  const toggleArrow = document.getElementById("toggleArrow3");

  productContainer.classList.toggle("hidden");
  productContainer.classList.toggle("visible");

  toggleArrow.classList.toggle("rotated");
}
function toggleEdariak() {
  const productContainer = document.getElementById("productContainer4");
  const toggleArrow = document.getElementById("toggleArrow4");

  productContainer.classList.toggle("hidden");
  productContainer.classList.toggle("visible");

  toggleArrow.classList.toggle("rotated");
}

async function loadProducts() {
  try {
    const response = await fetch("/v1/products/");
    const products = await response.json();
    const carouselRow = document.getElementById("harierakoakrow");
    const burgerRow = document.getElementById("burgerrow");
    const porstreRow = document.getElementById("postrerow");
    const bebidaRow = document.getElementById("bebidarow");

    products.forEach((product) => {
      const item = document.createElement("div");
      item.className = "item text-center";
      item.onclick = () =>
        openModal(
          product.name,
          product.description,
          product.price,
          `/static/resources/products/${product.foto}`,
          product.id
        );

      const img = document.createElement("img");
      img.src = `/static/resources/products/${product.foto}`;
      img.alt = product.name;
      img.className = "carousel-img";

      const description = document.createElement("p");
      description.innerText = product.name;

      item.appendChild(img);
      item.appendChild(description);

      if (product.category.id == 1) {
        carouselRow.appendChild(item);
      } else if (product.category.id == 2) {
        burgerRow.appendChild(item);
      } else if (product.category.id == 3) {
        porstreRow.appendChild(item);
      } else if (product.category.id == 4) {
        bebidaRow.appendChild(item);
      }
    });
  } catch (error) {
    
  }
}

// Llama a la función cuando se carga la página
document.addEventListener("DOMContentLoaded", loadProducts);

// Función para abrir el modal con los detalles del producto
async function openModal(
  productName,
  productDescription,
  productPrice,
  productImage,
  productId
) {
  const response = await fetch(`/v1/product_alergens/${productId}/`);
  const allergens = await response.json();

  const allergensContainer = document.querySelector(".allergens");
  allergensContainer.innerHTML = "";
  allergensContainer.innerHTML = " </br>Alergenoak:";

  if (allergens && allergens.length > 0) {
    allergens.forEach((allergen) => {
      const img = document.createElement("img");
      img.src = `/static/resources/alergens/${allergen}.png`;
      img.title = allergen;
      allergensContainer.appendChild(img);
    });
  } else {
    const noAllergens = document.createElement("p");
    noAllergens.innerText = "Este producto no tiene alérgenos registrados.";
    allergensContainer.appendChild(noAllergens);
  }




  // Ahora rellenamos los demás campos del modal
  document.getElementById("modalTitle").innerText = productName;
  document.getElementById("modalDescription").innerText = productDescription;
  document.getElementById("modalPrice").innerText = `${productPrice} €`;
  document.getElementById("modalImg").src = productImage;
  document.getElementById("product_id").value = productId;


  // Mostrar el modal
  document.getElementById("productModal").style.display = "block";
}

function closeModal() {
  document.getElementById("productModal").style.display = "none";
}
