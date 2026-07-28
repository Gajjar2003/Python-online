import React, { useState } from "react";

function Employeelist() {
  const [textshow, settext] = useState("Wel Come To Add Employees");

  const [newemp, setemp] = useState([]);

  const clickbutton = (e) => {
    console.log(e);
        console.log(e.target.value);
  };

  const textchange = (e) => {
    if (e.key === "Enter") {
      let newEmployee = e.target.value;
        console.log(newEmployee);
        
      if (newEmployee === "") {
        return;
      }

      setemp([...newemp, newEmployee]);
      settext("New Employees Add "+ newEmployee);
      //console.log("New Employee add: " + newEmployee);
   
      e.target.value = "";
    }
  };

  return (
    <div>
      <h1 className="m-2">Welcome To Employees-List</h1>

      <input
        type="text"
        placeholder="Enter Your Employees Name....."
        className="p-2 w-50 m-2"
        onKeyDown={textchange}
      />

      <p className="m-3">{textshow}</p>

      <ul className="list-group">
        {newemp.map((index) => (
          <li className="list-group-item" key={index}>
            {index}

            <div className="text-end">
              <button
                className="btn btn-success"
                onClick={clickbutton}
                value="Add Employees"
              >
                Add
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Employeelist;
