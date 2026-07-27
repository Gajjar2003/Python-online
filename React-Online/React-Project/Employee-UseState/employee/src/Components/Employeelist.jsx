import React from "react";
import Employeebutton from "./Employeebutton";
import Employeeinput from "./Employeeinput";

function Employeelist(props) {
  return (
    <div>
      <h1>Employee List</h1>

      <Employeeinput setEmployees={props.setEmployees} />

      <br />

      <ul className="list-group">
        {props.item.map((employee) => (
          <li className="list-group-item" key={employee}>
            {employee}

            <Employeebutton />
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Employeelist;