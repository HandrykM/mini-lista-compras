export default function Landing({ onLogin, onRegister }) {
  return (
    <div className="landing-container">
      <div className="landing-content">
        <div className="landing-hero">
          <h1 className="landing-title">
            🛒 Mini Lista de Compras
          </h1>
          <p className="landing-subtitle">
            Organiza tus compras de manera simple y eficiente
          </p>
          <div className="landing-features">
            <div className="feature">
              <span className="feature-icon">✓</span>
              <span>Crea y gestiona tus listas</span>
            </div>
            <div className="feature">
              <span className="feature-icon">✓</span>
              <span>Marca productos comprados</span>
            </div>
            <div className="feature">
              <span className="feature-icon">✓</span>
              <span>Ve tu progreso en tiempo real</span>
            </div>
          </div>
        </div>

        <div className="landing-actions">
          <button onClick={onLogin} className="btn-landing btn-primary">
            Iniciar sesión
          </button>
          <button onClick={onRegister} className="btn-landing btn-secondary">
            Crear cuenta
          </button>
        </div>

        <div className="landing-footer">
          <p>Simple. Rápido. Efectivo.</p>
        </div>
      </div>
    </div>
  );
}