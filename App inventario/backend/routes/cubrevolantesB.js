const express = require('express')
const pool = require('../db');
const jwt = require('jsonwebtoken');

const router = express.Router();

//MIDDLEWARE DE AUTENTICACION
const auth = (req, res, next) => {
    const token = req.headers.authorization;

    if(!token){
        return res.status(401).json({message: 'Token requerido'});
    }

    try{
        jwt.verify(token, 'CLAVE SECRETA');
        next();
    }catch{
        res.status(401).json({message: 'Token invalido'});
    }
};

router.get('/inventario/cubrevolantes', auth, async (req, res) => {
    let connection;

    try {
        connection = await pool.getConnection();

        const rows = await connection.query(
            'SELECT ID, TIPO, PRECIO, STOCK FROM CUBREVOLANTES'
        );

        res.json(rows);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error al obtener Cubrevolantes' });
    } finally {
        if (connection) connection.release();
    }
});

router.put('/inventario/cubrevolantes', auth, async (req, res) => {
    const { updates } = req.body;
    let connection;

    try {
        connection = await pool.getConnection();

        for (const item of updates) {
            await connection.query(
                'UPDATE CUBREVOLANTES SET PRECIO = ?, STOCK = ? WHERE ID = ?',
                [item.precio, item.stock, item.id]
            );
        }

        res.json({ message: 'Inventario actualizado correctamente' });

    } catch (error) {
        console.log(error);
        res.status(500).json({ message: 'Error al actualizar inventario' });
    } finally {
        if (connection) connection.release();
    }
});


module.exports = router;