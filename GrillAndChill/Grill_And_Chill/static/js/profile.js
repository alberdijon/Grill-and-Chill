const userId = document.getElementById('user-data').getAttribute('data-user-id');

fetch(`/v1/users/${userId}/`)
    .then(response => response.json())
    .then(data => {
        document.getElementById('email').textContent = data.gmail;
        document.getElementById('phone').textContent = data.tlf;
        document.getElementById('address').textContent = data.direction;
        document.getElementById('password').textContent = '********'; 
    })
    .catch(error => {
        console.error('Error al cargar los datos del usuario:', error);
    });