import { create } from "zustand";
import api from "../services/api";

export const useStore = create((set, get) => ({
  // Auth state
  user: JSON.parse(localStorage.getItem("user")) || null,
  token: localStorage.getItem("token") || null,
  isAuthenticated: !!localStorage.getItem("token"),
  
  // Items state
  items: [],
  stats: {},
  loading: false,
  error: null,
  
  // ========== AUTH ACTIONS ==========
  login: async (email, password) => {
    try {
      set({ loading: true, error: null });
      const res = await api.post("/auth/login", { email, password });
      const { access_token, user } = res.data;
      
      localStorage.setItem("token", access_token);
      localStorage.setItem("user", JSON.stringify(user));
      
      set({ 
        token: access_token, 
        user, 
        isAuthenticated: true,
        loading: false 
      });
      
      return { success: true };
    } catch (error) {
      const message = error.response?.data?.detail || "Error al iniciar sesión";
      set({ error: message, loading: false });
      return { success: false, error: message };
    }
  },
  
  register: async (username, email, password) => {
    try {
      set({ loading: true, error: null });
      const res = await api.post("/auth/register", { username, email, password });
      const { access_token, user } = res.data;
      
      localStorage.setItem("token", access_token);
      localStorage.setItem("user", JSON.stringify(user));
      
      set({ 
        token: access_token, 
        user, 
        isAuthenticated: true,
        loading: false 
      });
      
      return { success: true };
    } catch (error) {
      const message = error.response?.data?.detail || "Error al registrarse";
      set({ error: message, loading: false });
      return { success: false, error: message };
    }
  },
  
  logout: () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    set({ 
      token: null, 
      user: null, 
      isAuthenticated: false,
      items: [],
      stats: {}
    });
  },
  
  // ========== ITEMS ACTIONS ==========
  fetchItems: async () => {
    try {
      set({ loading: true, error: null });
      const res = await api.get("/items/");
      const items = res.data.map(item => ({
        id: item.id,
        nombre: item.name,
        cantidad: item.quantity,
        estado: item.purchased ? "comprado" : "pendiente"
      }));
      set({ items, loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
      console.error("Error fetching items:", error);
    }
  },
  
  addItem: async (item) => {
    try {
      set({ loading: true, error: null });
      await api.post("/items/", {
        name: item.nombre,
        quantity: parseInt(item.cantidad)
      });
      await get().fetchItems();
      await get().fetchStats();
    } catch (error) {
      set({ error: error.message, loading: false });
      console.error("Error adding item:", error);
    }
  },
  
  updateItem: async (id, data) => {
    try {
      set({ loading: true, error: null });
      if (data.estado) {
        await api.patch(`/items/${id}/purchase`, {
          purchased: data.estado === "comprado"
        });
      } else {
        const updateData = {};
        if (data.nombre) updateData.name = data.nombre;
        if (data.cantidad) updateData.quantity = parseInt(data.cantidad);
        await api.put(`/items/${id}`, updateData);
      }
      await get().fetchItems();
      await get().fetchStats();
    } catch (error) {
      set({ error: error.message, loading: false });
      console.error("Error updating item:", error);
    }
  },
  
  deleteItem: async (id) => {
    try {
      set({ loading: true, error: null });
      await api.delete(`/items/${id}`);
      await get().fetchItems();
      await get().fetchStats();
    } catch (error) {
      set({ error: error.message, loading: false });
      console.error("Error deleting item:", error);
    }
  },

  fetchStats: async () => {
    try {
      const res = await api.get("/stats/");
      const total = res.data.total_items || 0;
      const comprados = res.data.items_purchased || 0;
      const porcentaje = total > 0 ? Math.round((comprados / total) * 100) : 0;
      
      set({ 
        stats: {
          total,
          comprados,
          pendientes: res.data.items_pending || 0,
          porcentaje
        }
      });
    } catch (error) {
      console.error("Error fetching stats:", error);
    }
  }
}));