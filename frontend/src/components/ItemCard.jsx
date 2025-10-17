import { useStore } from "../store/useStore";

export default function ItemCard({ item }) {
  const { updateItem, deleteItem, fetchStats } = useStore();

  const toggleEstado = async () => {
    const nuevoEstado = item.estado === "pendiente" ? "comprado" : "pendiente";
    await updateItem(item.id, { ...item, estado: nuevoEstado });
    fetchStats();
  };

  return (
    <div className="card">
      <span>{item.nombre} ({item.cantidad})</span>
      <button onClick={toggleEstado}>
        {item.estado === "pendiente" ? "✅ Marcar comprado" : "↩️ Desmarcar"}
      </button>
      <button onClick={() => deleteItem(item.id)}>🗑 Eliminar</button>
    </div>
  );
}
