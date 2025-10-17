import { create } from "zustand";
import api from "../services/api";

export const useStore = create((set, get) => ({
  items: [],
  stats: {},
  
  fetchItems: async () => {
    const res = await api.get("/items/");
    set({ items: res.data });
  },
  
  addItem: async (item) => {
    await api.post("/items/", item);
    await get().fetchItems();
  },
  
  updateItem: async (id, data) => {
    await api.put(`/items/${id}`, data);
    await get().fetchItems();
  },
  
  deleteItem: async (id) => {
    await api.delete(`/items/${id}`);
    await get().fetchItems();
  },

  fetchStats: async () => {
    const res = await api.get("/stats/");
    set({ stats: res.data });
  }
}));
