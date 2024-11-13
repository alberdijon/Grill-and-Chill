const userId = document.getElementById('user-data').getAttribute('data-user-id');

// Hacer la solicitud GET para obtener los detalles del usuario
fetch(`/v1/users/${userId}/`)
    .then(response => response.json())
    .then(data => {
        // Actualizar los elementos HTML con los datos del usuario
        document.getElementById('email').textContent = data.gmail;
        document.getElementById('phone').textContent = data.tlf;
        document.getElementById('address').textContent = data.direction;
        document.getElementById('password').textContent = '********';  // Mostrar un texto oculto o permitir cambiar la contraseña
    })
    .catch(error => {
        console.error('Error al cargar los datos del usuario:', error);
    });