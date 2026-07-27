import { useState } from "react";
import "./App.css";
import Employeelist from "./Components/Employeelist";

function App() {
  const [employees, setEmployees] = useState([]);

  return (
    <>
      <Employeelist
        item={employees}
        setEmployees={setEmployees}
      />
    </>
  );
}

export default App;