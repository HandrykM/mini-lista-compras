import { useEffect, useState } from "react";
import { useStore } from "../store/useStore";
import ItemCard from "./ItemCard";
import StatsBar from "./StatsBar";

export default function ShoppingList() {
  const { items, fetchItems, addItem, fetchStats } = useStore();
  const [nombre, setNombre] = useState("");
  const [cantidad, setCantidad] = useState(1);

  useEffect(() => {
    fetchItems();
    fetchStats();
  }, []);

  const handleAdd = async (e) => {
    e.preventDefault();
    if (!nombre) return;
    await addItem({ nombre, cantidad, estado: "pendiente" });
    setNombre("");
    setCantidad(1);
    fetchStats();
  };

  return (
    <div className="container">
      <h1>🛒 Mini Lista de Compras</h1>
      <form onSubmit={handleAdd}>
        <input value={nombre} onChange={(e) => setNombre(e.target.value)} placeholder="Producto" />
        <input type="number" value={cantidad} min="1" onChange={(e) => setCantidad(e.target.value)} />
        <button>Agregar</button>
      </form>
      <StatsBar />
      <div>
        {items.map((i) => <ItemCard key={i.id} item={i} />)}
      </div>
    </div>
  );
}
