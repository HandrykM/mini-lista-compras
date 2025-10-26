import { useEffect, useState } from "react";
import { useStore } from "../store/useStore";
import ItemCard from "./ItemCard";
import StatsBar from "./StatsBar";

export default function ShoppingList() {
  const { items, user, fetchItems, addItem, logout, loading, error } = useStore();
  const [nombre, setNombre] = useState("");
  const [cantidad, setCantidad] = useState(1);
  const [filter, setFilter] = useState("todos");

  useEffect(() => {
    fetchItems();
  }, []);

  const handleAdd = async (e) => {
    e.preventDefault();
    if (!nombre.trim()) return;
    
    await addItem({ 
      nombre: nombre.trim(), 
      cantidad: parseInt(cantidad)
    });
    
    setNombre("");
    setCantidad(1);
  };

  const handleLogout = () => {
    if (window.confirm("¿Estás seguro de que quieres cerrar sesión?")) {
      logout();
    }
  };

  const filteredItems = items.filter(item => {
    if (filter === "todos") return true;
    return item.estado === filter;
  });

  return (
    <div className="shopping-list-container">
      <header className="header">
        <div className="header-content">
          <div>
            <h1>🛒 Mini Lista de Compras</h1>
            <p className="subtitle">Hola, {user?.username} </p>
          </div>
          <button onClick={handleLogout} className="btn-logout">
            Cerrar sesión
          </button>
        </div>
      </header>

      <StatsBar />

      <form className="add-item-form" onSubmit={handleAdd}>
        <input 
          type="text"
          className="input-name"
          value={nombre} 
          onChange={(e) => setNombre(e.target.value)} 
          placeholder="¿Qué necesitas comprar?" 
          disabled={loading}
        />
        <input 
          type="number" 
          className="input-quantity"
          value={cantidad} 
          min="1" 
          max="999"
          onChange={(e) => setCantidad(e.target.value)}
          disabled={loading}
        />
        <button type="submit" className="btn-add" disabled={loading}>
          {loading ? "..." : "+ Agregar"}
        </button>
      </form>

      {error && (
        <div className="error-message">
          ⚠️ Error: {error}
        </div>
      )}

      <div className="filter-buttons">
        <button 
          className={filter === "todos" ? "active" : ""}
          onClick={() => setFilter("todos")}
        >
          Todos ({items.length})
        </button>
        <button 
          className={filter === "pendiente" ? "active" : ""}
          onClick={() => setFilter("pendiente")}
        >
          Pendientes ({items.filter(i => i.estado === "pendiente").length})
        </button>
        <button 
          className={filter === "comprado" ? "active" : ""}
          onClick={() => setFilter("comprado")}
        >
          Comprados ({items.filter(i => i.estado === "comprado").length})
        </button>
      </div>

      <div className="items-list">
        {loading && items.length === 0 ? (
          <p className="loading">Cargando...</p>
        ) : filteredItems.length === 0 ? (
          <p className="empty-state">
            {filter === "todos" 
              ? "📝 No hay items. ¡Agrega tu primer producto!" 
              : `No hay items ${filter}s`}
          </p>
        ) : (
          filteredItems.map((item) => (
            <ItemCard key={item.id} item={item} />
          ))
        )}
      </div>
    </div>
  );
}