import React, { useState } from "react";

function Input() {
  const [newadd, setadd] = useState([]);

  const changeitems = (e) => {
    if (e.key === "Enter") {
      let additems = e.target.value;

      let addnewitems = [...newadd, additems];

      setadd(addnewitems);

      console.log(addnewitems);

      e.target.value = "";
    }
  };

  return (
    <div>
      <h1>Input-list</h1>

      <input
        type="text"
        placeholder="Enter Your input ..."
        onKeyDown={changeitems}
      />

      <ul>
        {newadd.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

export default Input;