import React from "react";
import "./style.css";
import Calculatorbutton from "./Calculatorbutton";

function Calculatorinput() {
  return (
    <div id="calculator">
      <h1 className="mt-3">Calculator-App</h1>

      <input type="text" id="display" />
      

      <Calculatorbutton/>
    </div>
  );
}

export default Calculatorinput;
