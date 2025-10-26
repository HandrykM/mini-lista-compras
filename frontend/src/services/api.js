import axios from "axios";
const api = axios.create({ baseURL: "https://mini-lista-compras.onrender.com" }); //Aqui Upamecano pone la URL base de la API
export default api;
