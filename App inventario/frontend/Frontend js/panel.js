const token = localStorage.getItem('token');
const nombre = localStorage.getItem('nombre');

if(!token){
    window.location.href = 'index.html';
}

document.getElementById('username').textContent = nombre;

document.getElementById('welcome').textContent = `Bienvenido ${nombre}`;