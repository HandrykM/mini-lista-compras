import { create } from "zustand";
import api from "../services/api";

export const useStore = create((set, get) => ({
  items: [],
  stats: {},
  
  // Obtener todos los items
  fetchItems: async () => {
    try {
      const res = await api.get("/items/");
      set({ items: res.data });
    } catch (err) {
      console.error("Error al obtener items:", err);
    }
  },

  // Agregar un item
  addItem: async (item) => {
    try {
      const res = await api.post("/items/", item);
      set({ items: [...get().items, res.data] });
    } catch (err) {
      console.error("Error al agregar item:", err);
    }
  },

  // Actualizar un item
  updateItem: async (id, item) => {
    try {
      const res = await api.put(`/items/${id}`, item);
      set({
        items: get().items.map((i) => (i.id === id ? res.data : i))
      });
    } catch (err) {
      console.error("Error al actualizar item:", err);
    }
  },

  // Eliminar un item
  deleteItem: async (id) => {
    try {
      await api.delete(`/items/${id}`);
      set({ items: get().items.filter((i) => i.id !== id) });
    } catch (err) {
      console.error("Error al eliminar item:", err);
    }
  },

  // Estadísticas
  fetchStats: () => {
    const items = get().items;
    const total = items.length;
    const comprados = items.filter((i) => i.estado === "comprado").length;
    const porcentaje = total ? Math.round((comprados / total) * 100) : 0;
    set({ stats: { total, comprados, porcentaje } });
  }
}));
