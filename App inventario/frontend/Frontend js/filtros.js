const token = localStorage.getItem('token');

if (!token) {
    window.location.href = 'index.html';
}

fetch('http://localhost:3000/api/inventario/filtros', {
    headers: {
        'Authorization': token
    }
})
.then(res => res.json())
.then(data => {
    const tbody = document.querySelector('#TableFiltros tbody');
    tbody.innerHTML = '';

    data.forEach(item => {
        const tr = document.createElement('tr');

        tr.dataset.id = item.ID;

        tr.innerHTML = `
            <td>${item.CODIGO}</td>
            <td>${item.TIPO}</td>
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
    alert('Error al cargar filtros');
});

updateBtn = document.getElementById('updateAllFiltros');

updateBtn.addEventListener('click', async () => {
    const rows = document.querySelectorAll('#TableFiltros tbody tr');

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
        const res = await fetch('http://localhost:3000/api/inventario/filtros', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': token
            },
            body: JSON.stringify({ updates })
        });

        const data = await res.json();

        if (res.ok) {
            alert('Inventario actualizado correctamente');
            console.log('Inventario de filtros actualizado correctamente')
        } else {
            alert(data.message || 'Error al actualizar inventario de filtros');
        }

    } catch (error) {
        console.error(error);
        alert('Error de conexión con el servidor');
    }
});
