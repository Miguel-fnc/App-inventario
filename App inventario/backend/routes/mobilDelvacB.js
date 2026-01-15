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

router.get('/inventario/mobildelvac', auth, async(req, res) => {

    let connection;

    try{
        connection = await pool.getConnection();

        const rows = await connection.query(
            'SELECT ID, VISCOSIDAD, PRESENTACION, PRECIO, STOCK FROM MOBIL_DELVAC'
        );

        res.json(rows);

    }catch(err){
        console.log(err);
        res.status(500).json({message: 'Error al obtener el inventario'});
    }finally{
        if (connection) connection.release();
    }
});

router.put('/inventario/mobildelvac', auth, async (req, res) => {
    const { updates } = req.body;
    let connection;

    try {
        connection = await pool.getConnection();

        for (const item of updates) {
            await connection.query(
                'UPDATE MOBIL_DELVAC SET PRECIO = ?, STOCK = ? WHERE ID = ?',
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