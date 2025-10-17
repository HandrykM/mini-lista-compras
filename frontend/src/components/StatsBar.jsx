import { useEffect } from "react";
import { useStore } from "../store/useStore";

export default function StatsBar() {
  const { stats, fetchStats } = useStore();

  useEffect(() => { fetchStats(); }, []);

  return (
    <div className="stats">
      <p>Total: {stats.total || 0}</p>
      <p>Comprados: {stats.comprados || 0}</p>
      <p>Progreso: {stats.porcentaje || 0}%</p>
    </div>
  );
}
