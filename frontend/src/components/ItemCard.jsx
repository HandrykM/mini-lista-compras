import { useStore } from "../store/useStore";

export default function ItemCard({ item }) {
  const { updateItem, deleteItem } = useStore();

  const toggleEstado = async () => {
    const nuevoEstado = item.estado === "pendiente" ? "comprado" : "pendiente";
    await updateItem(item.id, { estado: nuevoEstado });
  };

  const handleDelete = async () => {
    if (window.confirm(`¿Eliminar "${item.nombre}"?`)) {
      await deleteItem(item.id);
    }
  };

  return (
    <div className={`item-card ${item.estado}`}>
      <div className="item-info">
        <span className="item-name">{item.nombre}</span>
        <span className="item-quantity">x{item.cantidad}</span>
      </div>
      <div className="item-actions">
        <button 
          className={`btn-toggle ${item.estado}`}
          onClick={toggleEstado}
        >
          {item.estado === "pendiente" ? "✓ Comprado" : "↻ Pendiente"}
        </button>
        <button className="btn-delete" onClick={handleDelete}>
          🗑️
        </button>
      </div>
    </div>
  );
}