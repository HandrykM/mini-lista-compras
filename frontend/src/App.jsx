import { useState } from "react";
import { useStore } from "./store/useStore";
import Landing from "./components/Landing";
import Login from "./components/Login";
import Register from "./components/Register";
import ShoppingList from "./components/ShoppingList";
import "./App.css";

function App() {
  const { isAuthenticated } = useStore();
  const [currentView, setCurrentView] = useState("landing"); // landing, login, register

  // Si está autenticado, mostrar la lista
  if (isAuthenticated) {
    return (
      <div className="app">
        <ShoppingList />
      </div>
    );
  }

  // Si no está autenticado, mostrar landing/login/register
  return (
    <div className="app">
      {currentView === "landing" && (
        <Landing
          onLogin={() => setCurrentView("login")}
          onRegister={() => setCurrentView("register")}
        />
      )}
      {currentView === "login" && (
        <Login onToggle={() => setCurrentView("register")} />
      )}
      {currentView === "register" && (
        <Register onToggle={() => setCurrentView("login")} />
      )}
    </div>
  );
}

export default App;