import React from "react";

function Employeeinput({ settext }) {

  const changeEmploye = (e) => {
    settext(e.target.value);
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Enter Your Employee...."
        className="p-2 w-50"
        onChange={changeEmploye}
      />
    </div>
  );
}

export default Employeeinput;