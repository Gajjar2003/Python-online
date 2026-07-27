import React from "react";

function Employeebutton() {

  const clickhandl = (e) => {
    console.log(e.target.value);
  };

  return (
    <div className="text-end">
      <button
        className="btn btn-success"
        onClick={clickhandl} value="Click me"
      >
        Add
      </button>
    </div>
  );
}

export default Employeebutton;