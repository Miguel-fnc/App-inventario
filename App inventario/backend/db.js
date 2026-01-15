const mariadb = require("mariadb")

const pool = mariadb.createPool({
    host: 'localhost', 
    port: 3306,
    user: 'miguelfnco',
    password: 'Miguel_421',
    database: 'inventario',
    connectionLimit: 3
});


module.exports = pool;