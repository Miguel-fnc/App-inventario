if (!token) {
    window.location.href = 'index.html';
}

fetch('http://localhost:3000/api/inventario/sekuritgrasas', {
    headers: {
        'Authorization': token
    }
})
.then(res => res.json())
.then(data => {
    const tbody = document.querySelector('#TableSekuritGrasas tbody');

    data.forEach(item => {
        const tr = document.createElement('tr');

        tr.dataset.id = item.ID;

        tr.innerHTML = `
            <td>${item.COLOR}</td>
            <td>${item.TIPO}</td>
            <td>${item.PRESENTACION}</td>
            <td>
                <input 
                    type="number" 
                    class="precio-input" 
                    value="${item.PRECIO}" 
                    min="0"
                >
            </td>
            <td>
                <input 
                    type="number" 
                    class="stock-input" 
                    value="${item.STOCK}" 
                    min="0"
                >
            </td>
        `;

        tbody.appendChild(tr);
    });
})
.catch(err => {
    console.log(err);
    alert('Error al cargar sekurit grasas');
});

updateBtn.addEventListener('click', async () => {
    const rows = document.querySelectorAll('#TableSekuritGrasas tbody tr');

    const updates = [];

    rows.forEach(row => {
        const id = row.dataset.id;

        const precio = row.querySelector('.precio-input').value;
        const stock = row.querySelector('.stock-input').value;

        updates.push({
            id,
            precio,
            stock
        });
    });

    try {
        const res = await fetch('http://localhost:3000/api/inventario/sekuritgrasas', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': token
            },
            body: JSON.stringify({ updates })
        });

        const data = await res.json();

        if (res.ok) {
            console.log('Inventario sekurit grasas actualizado correctamente')
        } else {
            alert(data.message || 'Error al actualizar inventario sekurit grasas');
        }

    } catch (error) {
        console.error(error);
        alert('Error de conexión con el servidor');
    }
});
