const token = localStorage.getItem('token');
if(!token){
  window.location.href = 'index.html';
}

document.getElementById('loginForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  const errorEl = document.getElementById('error');

  errorEl.textContent = '';

  try {
    const response = await fetch('http://localhost:3000/api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email, password })
    });

    const data = await response.json();


    if (!response.ok) {
      errorEl.textContent = data.message;
      return;
    }

    localStorage.setItem('token', data.token);
    localStorage.setItem('nombre', data.nombre);

    window.location.href = 'panel.html';

  } catch (err) {
    errorEl.textContent = 'No se pudo conectar al servidor';
  }
});
