import React from "react";

function Food() {
  const Foods = ["Pizza", "Burger", "Coffee", "Tea"];
  //const Foods = []

  return (
    <div>
      <h1>Food</h1>
      {Foods.length === 0 && <h3>I am still hungry ..</h3>}
      <ul className="list-group">
        {Foods.map((item) => {
          return (
            <li className="list-group-item" key={item}>
              {item}
            </li>
          );
        })}
      </ul>
    </div>
  );
}

export default Food;
