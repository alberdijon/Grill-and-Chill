$(document).ready(function () {
  const hanburgesakSection = document.querySelector(".hanburgesak");
  const hanburgesakItems = document.querySelectorAll(".carousel-item .item");

  const hanburgesakObserverOptions = {
    root: hanburgesakSection,
    threshold: 1,
  };

  const hanburgesakObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) {
        entry.target.style.opacity = "0";
        entry.target.style.transition = "opacity 0.5s";
      } else {
        entry.target.style.opacity = "1";
      }
    });
  }, hanburgesakObserverOptions);

  hanburgesakItems.forEach((item) => {
    hanburgesakObserver.observe(item);
  });

  const carouselRowHanburgesak = document.getElementById("burgerrow");
  let isDraggingHanburgesak = false;
  let startPosHanburgesak = 0;
  let currentTranslateHanburgesak = 0;
  let prevTranslateHanburgesak = 0;
  let animationIDHanburgesak;

  const itemCountHanburgesak = hanburgesakItems.length;
  const itemWidthHanburgesak = hanburgesakItems[0].getBoundingClientRect().width;
  const cloneFirstHanburgesak = hanburgesakItems[0].cloneNode(true);
  const cloneLastHanburgesak = hanburgesakItems[itemCountHanburgesak - 1].cloneNode(true);
  carouselRowHanburgesak.appendChild(cloneFirstHanburgesak);
  carouselRowHanburgesak.insertBefore(cloneLastHanburgesak, hanburgesakItems[0]);

  const updatedItemsHanburgesak = document.querySelectorAll(".carousel-item .item");
  const updatedItemCountHanburgesak = updatedItemsHanburgesak.length;

  const setSliderPositionHanburgesak = () => {
    carouselRowHanburgesak.style.transform = `translateX(${currentTranslateHanburgesak}px)`;
  };

  const animationHanburgesak = () => {
    setSliderPositionHanburgesak();
    if (isDraggingHanburgesak) requestAnimationFrame(animationHanburgesak);
  };

  carouselRowHanburgesak.addEventListener("mousedown", (event) => {
    isDraggingHanburgesak = true;
    startPosHanburgesak = event.pageX;
    animationIDHanburgesak = requestAnimationFrame(animationHanburgesak);
    carouselRowHanburgesak.style.cursor = "grabbing";
  });

  carouselRowHanburgesak.addEventListener("mousemove", (event) => {
    if (isDraggingHanburgesak) {
      const currentPositionHanburgesak = event.pageX;
      const distanceMovedHanburgesak = currentPositionHanburgesak - startPosHanburgesak;
      const speedFactorHanburgesak = 1;
      currentTranslateHanburgesak = prevTranslateHanburgesak + distanceMovedHanburgesak * speedFactorHanburgesak;
    }
  });

  carouselRowHanburgesak.addEventListener("mouseup", () => {
    isDraggingHanburgesak = false;
    cancelAnimationFrame(animationIDHanburgesak);
    prevTranslateHanburgesak = currentTranslateHanburgesak;

    if (currentTranslateHanburgesak < -((updatedItemCountHanburgesak - 1) * itemWidthHanburgesak)) {
      currentTranslateHanburgesak = -itemWidthHanburgesak; 
    } else if (currentTranslateHanburgesak > 0) {
      currentTranslateHanburgesak = -((updatedItemCountHanburgesak - 2) * itemWidthHanburgesak);
    }

    setSliderPositionHanburgesak();
    carouselRowHanburgesak.style.cursor = "grab";
  });

  carouselRowHanburgesak.addEventListener("mouseleave", () => {
    if (isDraggingHanburgesak) {
      isDraggingHanburgesak = false;
      cancelAnimationFrame(animationIDHanburgesak);
      prevTranslateHanburgesak = currentTranslateHanburgesak;
      carouselRowHanburgesak.style.cursor = "grab";
    }
  });

  document.addEventListener("mouseup", () => {
    if (isDraggingHanburgesak) {
      isDraggingHanburgesak = false;
      cancelAnimationFrame(animationIDHanburgesak);
      prevTranslateHanburgesak = currentTranslateHanburgesak;
      carouselRowHanburgesak.style.cursor = "grab";
    }
  });

  const edariakSection = document.querySelector(".edariak");
  const edariakItems = document.querySelectorAll("#bebidarow .item");

const edariakObserverOptions = {
  root: edariakSection,
  threshold: 1,
};

const edariakObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) {
      entry.target.style.opacity = "0";
      entry.target.style.transition = "opacity 0.5s";
    } else {
      entry.target.style.opacity = "1";
    }
  });
}, edariakObserverOptions);

edariakItems.forEach((item) => {
  edariakObserver.observe(item);
});

const carouselRowEdariak = document.getElementById("bebidarow");
let isDraggingEdariak = false;
let startPosEdariak = 0;
let currentTranslateEdariak = 0;
let prevTranslateEdariak = 0;
let animationIDEdariak;

const itemCountEdariak = edariakItems.length;
const itemWidthEdariak = edariakItems[0].getBoundingClientRect().width;

const cloneFirstEdariak = edariakItems[0].cloneNode(true);
const cloneLastEdariak = edariakItems[itemCountEdariak - 1].cloneNode(true);
carouselRowEdariak.appendChild(cloneFirstEdariak);
carouselRowEdariak.insertBefore(cloneLastEdariak, edariakItems[0]);

const updatedItemsEdariak = document.querySelectorAll(".carousel-item .item");
const updatedItemCountEdariak = updatedItemsEdariak.length;

const setSliderPositionEdariak = () => {
  carouselRowEdariak.style.transform = `translateX(${currentTranslateEdariak}px)`;
};

const animationEdariak = () => {
  setSliderPositionEdariak();
  if (isDraggingEdariak) requestAnimationFrame(animationEdariak);
};

carouselRowEdariak.addEventListener("mousedown", (event) => {
  isDraggingEdariak = true;
  startPosEdariak = event.pageX;
  animationIDEdariak = requestAnimationFrame(animationEdariak);
  carouselRowEdariak.style.cursor = "grabbing";
});

carouselRowEdariak.addEventListener("mousemove", (event) => {
  if (isDraggingEdariak) {
    const currentPositionEdariak = event.pageX;
    const distanceMovedEdariak = currentPositionEdariak - startPosEdariak;
    const speedFactorEdariak = 1;
    currentTranslateEdariak = prevTranslateEdariak + distanceMovedEdariak * speedFactorEdariak;
  }
});

carouselRowEdariak.addEventListener("mouseup", () => {
  isDraggingEdariak = false;
  cancelAnimationFrame(animationIDEdariak);
  prevTranslateEdariak = currentTranslateEdariak;

  if (currentTranslateEdariak < -((updatedItemCountEdariak - 1) * itemWidthEdariak)) {
    currentTranslateEdariak = -itemWidthEdariak;
  } else if (currentTranslateEdariak > 0) {
    currentTranslateEdariak = -((updatedItemCountEdariak - 2) * itemWidthEdariak);
  }

  setSliderPositionEdariak();
  carouselRowEdariak.style.cursor = "grab";
});

carouselRowEdariak.addEventListener("mouseleave", () => {
  if (isDraggingEdariak) {
    isDraggingEdariak = false;
    cancelAnimationFrame(animationIDEdariak);
    prevTranslateEdariak = currentTranslateEdariak;
    carouselRowEdariak.style.cursor = "grab";
  }
});

document.addEventListener("mouseup", () => {
  if (isDraggingEdariak) {
    isDraggingEdariak = false;
    cancelAnimationFrame(animationIDEdariak);
    prevTranslateEdariak = currentTranslateEdariak;
    carouselRowEdariak.style.cursor = "grab";
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
document.addEventListener("DOMContentLoaded", loadProducts);

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

  document.getElementById("modalTitle").innerText = productName;
  document.getElementById("modalDescription").innerText = productDescription;
  document.getElementById("modalPrice").innerText = `${productPrice} €`;
  document.getElementById("modalImg").src = productImage;

  document.getElementById("product_id").value = productId;
  document.getElementById("productModal").style.display = "block";
}

function closeModal() {
  document.getElementById("productModal").style.display = "none";
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
    const carouselRow = document.getElementById("hasierakoakrow");
    const burgerRow = document.getElementById("burgerrow");
    const postrerow = document.getElementById("postrerow");
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
        postrerow.appendChild(item);
      } else if (product.category.id == 4) {
        bebidaRow.appendChild(item);
      }
    });
  } catch (error) {
    console.error("Error fetching products:", error);
  }
}
