const express = require('express')
const bcrypt = require('bcrypt')
const jwt = require('jsonwebtoken')
const pool = require('../db')

const router = express.Router();

router.post('/login', async (req,res) =>{
    const {email,password} = req.body;
    if(!email || !password){
        return res.status(400).json({message:"Ingrese ambos campos"});
    }

    let connection;
    try{
        connection = await pool.getConnection();

        const rows = await connection.query(
            'SELECT ID, NOMBRE as nombre, PASSWORD FROM USUARIOS WHERE EMAIL = ?',
            [email]
        );

        console.log(rows);

    if (rows.length === 0){
        return res.status(401).json({message:'Correo o contraseña incorrectos'})
    }

    const user = rows[0];

    const passwordCorrecta = user.PASSWORD

    if(!passwordCorrecta){
        return res.status(401).json({message:'Correo o Contraseña incorrecta'})
    }

    if(password !== passwordCorrecta){
        return res.status(401).json({message:'Credenciales invalidas'});
    }

    const token = jwt.sign(
        {id:user.ID},
        'CLAVE SECRETA',
        {expiresIn: '1h'}
    );

    res.json({
        message:'Login correcto',
        token,
        nombre:user.nombre
    });

    }catch(err){
        console.error(err);
        res.status(500).json({message:'error del servidor'})
    }finally{
        if (connection) connection.release();
    }
});

module.exports = router;
