import { useState, useEffect } from "react";
import api from "./api";

function App() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    async function fetchItems() {
      try {
        const res = await api.get("/items/");
        setItems(res.data);
      } catch (err) {
        console.error("Error al obtener items:", err);
      }
    }
    fetchItems();
  }, []);

  return (
    <div>
      <h1>Mini Lista de Compras</h1>
      <ul>
        {items.map((item) => (
          <li key={item.id}>
            {item.name} - Cantidad: {item.quantity} - {item.purchased ? "✅ Comprado" : "❌ Pendiente"}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
