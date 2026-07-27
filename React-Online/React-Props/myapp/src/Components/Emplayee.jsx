import React, { useState } from "react";
import Employeeinput from "./Employeeinput";
import EmployeeText from "./EmployeeText";

function Emplayee(props) {

  const [addtext, settext] = useState("Welcome to Employee");

  return (
    <div>
      <h1>Employee-List</h1>

      <Employeeinput settext={settext} />

      <br />

      <EmployeeText addtext={addtext} />

      <ul className="list-group">
        {props.items.map((index) => (
          <li className="list-group-item" key={index}>
            {index}

            <div className="text-end">
              <button className="btn btn-success">
                Add
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Emplayee;