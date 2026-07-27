import React from "react";

function Employeeinput({ setEmployees }) {

  const newEmployee = (e) => {
    if (e.key === "Enter") {

      const createnew = e.target.value.trim();  

      
      

      if (createnew === "") {
        return;
      }

      setEmployees((oldEmployees) => [
        ...oldEmployees,
        createnew,
      ]);

      e.target.value = "";
    }
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Enter Your Employee....."
        className="w-50 p-2"
        onKeyDown={newEmployee}
      />
    </div>
  );
}

export default Employeeinput;