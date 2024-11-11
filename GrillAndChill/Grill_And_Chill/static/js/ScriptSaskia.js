function toggleCart() {
  const cart = document.getElementById("cart");
  cart.classList.toggle("open");
}

function addToCartFromModal() {
    console.log("La función addToCartFromModal ha sido llamada");
    const productTitle = document.getElementById("modalTitle").innerText;
    const productPrice = document.getElementById("modalPrice").innerText;
    const productImage = document.getElementById("modalImg").src;
    const quantity = parseInt(document.getElementById("quantity").innerText);

    if (isNaN(quantity) || quantity < 1) {
        alert("Por favor, selecciona una cantidad válida.");
        return;
    }

    const product = {
        title: productTitle,
        price: productPrice,
        image: productImage,
        quantity: quantity,
    };

    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    cart.push(product);
    localStorage.setItem("cart", JSON.stringify(cart));

    updateCartView();
    closeModal();
}

 


function removeFromCart(index) {
  cartItems.splice(index, 1);
  updateCartDisplay();
}
function changeQuantity(change) {
  let quantityElement = document.getElementById("quantity");
  let currentQuantity = parseInt(quantityElement.textContent);
  currentQuantity = Math.max(1, currentQuantity + change);
  quantityElement.textContent = currentQuantity;
}