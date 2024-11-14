function toggleCart() {
  const cart = document.getElementById("cart");
  cart.classList.toggle("open");
}



document.addEventListener("DOMContentLoaded", loadCartProducts);

async function loadCartProducts() {
  try {
    const userId = document.getElementById("user-id").getAttribute("data-user-id");

    if (!userId) {
      return;
    }

    const cartItemsContainer = document.querySelector(".cart-items");
    const totalPriceElement = document.querySelector("#total-price");

    const response = await fetch(`/api/cart/${userId}`);
    const data = await response.json();

    if (data.order && data.order.ended !== false) {

      totalPriceElement.innerText = `${data.price.toFixed(2)}€`;

      data.products.forEach(product => {
        const productId = product.products_Id.id;
        const existingCartItem = document.getElementById(`product-${productId}`);

        if (existingCartItem) {
          // Si el producto ya está en el carrito, actualizar la cantidad
          const quantityText = existingCartItem.querySelector(`#quantity-text-${productId}`);
          const currentQuantity = parseInt(quantityText.innerText.split(": ")[1]);
          quantityText.innerText = `Cantidad: ${currentQuantity + 1}`;
        } else {
          // Si el producto no está en el carrito, crear una nueva tarjeta
          const cartItem = document.createElement("div");
          cartItem.className = "cart-item";
          cartItem.id = `product-${productId}`;

          // Columna izquierda: Imagen del producto
          const imgContainer = document.createElement("div");
          imgContainer.className = "cart-item-img";
          const img = document.createElement("img");
          img.src = `/static/resources/products/${product.products_Id.foto}`;
          img.alt = product.products_Id.name;
          img.style.width = "50px";
          img.style.height = "50px";
          imgContainer.appendChild(img);

          // Columna derecha: Nombre y botones de cantidad
          const rightColumn = document.createElement("div");
          rightColumn.className = "cart-item-details";

          // Fila superior: Nombre del producto
          const productName = document.createElement("div");
          productName.className = "product-name";
          productName.innerText = product.products_Id.name;
          rightColumn.appendChild(productName);

          // Fila inferior: Control de cantidad
          const quantityControl = document.createElement("div");
          quantityControl.className = "quantity-control";

          // Botón de restar cantidad
          const decreaseButton = document.createElement("button");
          decreaseButton.innerText = "-";
          decreaseButton.onclick = () => changeQuantityCart(productId, -1);

          // Texto con la cantidad actual, inicializada en 1
          const quantityText = document.createElement("span");
          quantityText.innerText = `Cantidad: 1`;
          quantityText.id = `quantity-text-${productId}`;

          // Botón de sumar cantidad
          const increaseButton = document.createElement("button");
          increaseButton.innerText = "+";
          increaseButton.onclick = () => changeQuantityCart(productId, 1);

          // Icono de eliminar producto
          const deleteIcon = document.createElement("img");
          deleteIcon.src = "{% static 'resources/delete-icon.png' %}";
          deleteIcon.alt = "Eliminar producto";
          deleteIcon.className = "delete-icon";
          deleteIcon.onclick = () => deleteProductFromCart(productId);

          quantityControl.appendChild(decreaseButton);
          quantityControl.appendChild(quantityText);
          quantityControl.appendChild(increaseButton);
          quantityControl.appendChild(deleteIcon);

          rightColumn.appendChild(quantityControl);

          // Añadir columnas al item del carrito
          cartItem.appendChild(imgContainer);
          cartItem.appendChild(rightColumn);

          cartItemsContainer.appendChild(cartItem);
        }
      });
    } else {
      // Si no hay orden activa, mostrar mensaje vacío
      cartItemsContainer.innerHTML = "<p>Tu carrito está vacío</p>";
    }
  } catch (error) {
    console.error("Error loading cart products:", error);
  }
}

function changeQuantityCart(productId, quantityChange) {
  const userId = document.getElementById("user-id").getAttribute("data-user-id");
  const action = quantityChange > 0 ? 'update' : 'update'; 

  fetch('/api/update_cart/', {
      method: 'POST',
      body: new URLSearchParams({
          'user_id': userId,
          'product_id': productId,
          'quantity_change': quantityChange,
          'action': action
      }),
      headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
      }
  })
  .then(response => response.json())
  .then(data => {
      if (data.message) {
          console.log(data.message); // Muestra el mensaje de éxito
          loadCartProducts();  // Recargar los productos del carrito
      } else {
          alert(data.error); // Mostrar error si ocurre algo
      }
  });
}




// Función para eliminar un producto del carrito
async function deleteProductFromCart(productId) {
  try {
    const userId = "{{ request.session.user_id }}";
    const response = await fetch(`/api/remove-product/${userId}/${productId}`, { method: 'POST' });
    const data = await response.json();

    if (data.success) {
      // Eliminar el producto del carrito en la UI
      const cartItem = document.getElementById(`product-${productId}`);
      cartItem.remove();

      // Actualizar el precio total
      const totalPriceElement = document.querySelector("#total-price");
      totalPriceElement.innerText = `${data.newTotalPrice.toFixed(2)}€`;
    } else {
      console.log("Error al eliminar el producto.");
    }
  } catch (error) {
    console.error("Error removing product:", error);
  }
}