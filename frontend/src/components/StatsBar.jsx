import { useStore } from "../store/useStore";

export default function StatsBar() {
  const { stats } = useStore();

  return (
    <div className="stats-bar">
      <div className="stat-item">
        <span className="stat-label">Total</span>
        <span className="stat-value">{stats.total || 0}</span>
      </div>
      <div className="stat-item">
        <span className="stat-label">Comprados</span>
        <span className="stat-value comprados">{stats.comprados || 0}</span>
      </div>
      <div className="stat-item">
        <span className="stat-label">Pendientes</span>
        <span className="stat-value pendientes">{stats.pendientes || 0}</span>
      </div>
      <div className="stat-item progress">
        <span className="stat-label">Progreso</span>
        <div className="progress-bar">
          <div 
            className="progress-fill" 
            style={{ width: `${stats.porcentaje || 0}%` }}
          />
          <span className="progress-text">{stats.porcentaje || 0}%</span>
        </div>
      </div>
    </div>
  );
}