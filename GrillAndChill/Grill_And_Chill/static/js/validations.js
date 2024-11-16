document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const firstName = document.getElementById("name");
    const lastName = document.getElementById("surname");
    const password = document.getElementById("password");
    const repPassword = document.getElementById("rep_password");
    const email = document.getElementById("gmail");
    const phone = document.getElementById("tlf");
    const address = document.getElementById("direction");
  
    form.addEventListener("submit", function (event) {
      if (!validateForm()) {
        event.preventDefault();
      }
    });
  
    function validateForm() {
      let valid = true;
      let messages = [];
  
      // Validate First Name
      if (!/^[A-Za-zÀ-ÿ\s]{2,}$/.test(firstName.value)) {
        messages.push("Izena: Solo letras, mínimo 2 caracteres");
        valid = false;
      }
  
      // Validate Last Name
      if (!/^[A-Za-zÀ-ÿ\s]{2,}$/.test(lastName.value)) {
        messages.push("Abizena: Solo letras, mínimo 2 caracteres");
        valid = false;
      }
  
      // Validate Password
      if (
        !/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+={}\[\]:;<>,.?/~`\\-])[A-Za-z\d!@#$%^&*()_+={}\[\]:;<>,.?/~`\\-]{8,}$/.test(
          password.value
        )
      ) {
        messages.push(
          "Pasahitza: Mínimo 8 caracteres, al menos una mayúscula, una minúscula, un número y un carácter especial"
        );
        valid = false;
      }
  
      // Validate Password Match
      if (password.value !== repPassword.value) {
        messages.push("Las contraseñas no coinciden");
        valid = false;
      }
  
      // Validate Email
      if (!/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/.test(email.value)) {
        messages.push("Email: Formato de correo electrónico inválido");
        valid = false;
      }
  
      // Validate Phone (9 digits)
      if (!/^\d{9}$/.test(phone.value)) {
        messages.push("Telefonoa: Debe contener solo números (9 dígitos)");
        valid = false;
      }
  
      // Validate Address
      if (address.value.trim().length < 5) {
        messages.push("Helbidea: Mínimo 5 caracteres");
        valid = false;
      }
  
      if (!valid) {
        alert(messages.join("\n"));
      }
  
      return valid;
    }
  });
