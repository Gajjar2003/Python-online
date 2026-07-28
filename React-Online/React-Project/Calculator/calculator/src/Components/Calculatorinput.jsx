import React from "react";
import Calculatorbutton from "./Calculatorbutton";
import "./style.css";

function Calculatorinput(props) {
  return (
    <div id="calculator">
      <h1>Calculator-App</h1>

      <input
        type="text"
        value={props.display || ""}
        readOnly
        className="p-3 w-100 bg-dark text-white rounded"
      />

      <Calculatorbutton
        setcal={props.setcal}
        addcla={props.addcla}
      />
    </div>
  );
}

export default Calculatorinput;