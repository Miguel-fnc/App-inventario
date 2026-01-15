const express = require('express');
const cors = require('cors');

//RUTAS MOBIL
const authRoutes = require('./routes/auth');
const blendRoute = require('./routes/BlendB');
const multiRoute = require('./routes/MultiB');
const trcproRoute = require('./routes/trcproB');
const monogradosMobilRoute = require('./routes/monogradosMobilB');
const mobilFullRoute = require('./routes/mobilFullB');
const mobil1Route = require('./routes/mobil1B');
const mobilDelvacRoute = require('./routes/mobilDelvacB');

//RUTAS CASTROL
const castrolEdgeRoute = require('./routes/castrolEdgeB');
const castrolMineralRoute = require('./routes/castrolMineralB');
const castrolFullRoute = require('./routes/castrolFullB');

//RUTAS ROSHFRAN
const roshfranRoute = require('./routes/roshfranB');

//RUTAS SEKURIT
const sekuritCajasRoute = require('./routes/sekuritCajasB');
const sekuritCubetasRoute = require('./routes/sekuritCubetasB');
const sekuritGrasasRoute = require('./routes/sekuritGrasasB');
const sekuritQuimicosRoute = require('./routes/sekuritQuimicosB');

//RUTAS BUJIAS
const bujiasRoute = require('./routes/bujiasB');

//RUTA CUBREVOLANTES
const cubrevolantesRoute = require('./routes/cubrevolantesB');

//RUTAS TAPETES
const tapetesRoute = require('./routes/tapetesB');

//RUTA BARDAHL
const bardahlRoute = require('./routes/bardahlB');

//RUTA PARABRISAS
const parabrisasRoute = require('./routes/parabrisasB');

//RUTA FILTROS
const filtrosRoute = require('./routes/filtrosB');

const app = express();

app.use(cors());
app.use(express.json());

//RUTAS GET  PUT
app.use('/api', authRoutes);
app.use('/api', blendRoute);
app.use('/api', multiRoute);
app.use('/api', trcproRoute);
app.use('/api', monogradosMobilRoute);
app.use('/api', mobilFullRoute);
app.use('/api', mobil1Route);
app.use('/api', mobilDelvacRoute);
app.use('/api', castrolEdgeRoute);
app.use('/api',castrolMineralRoute);
app.use('/api',castrolFullRoute);
app.use('/api', roshfranRoute);
app.use('/api', sekuritCajasRoute);
app.use('/api', sekuritCubetasRoute);
app.use('/api', sekuritGrasasRoute);
app.use('/api', sekuritQuimicosRoute);
app.use('/api', bujiasRoute);
app.use('/api', cubrevolantesRoute);
app.use('/api', tapetesRoute);
app.use('/api', bardahlRoute);
app.use('/api', parabrisasRoute);
app.use('/api', filtrosRoute);

//SERVIDOR
const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`Servidor escuchando en el puerto ${PORT}`)
});