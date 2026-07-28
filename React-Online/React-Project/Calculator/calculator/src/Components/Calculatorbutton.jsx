import React from "react";

function Calculatorbutton({ setcal, addcla }) {
  const onclickbutton = (buttontaxt) => {
    if (buttontaxt === "C") {
      setcal("");
    } else if (buttontaxt === "=") {
      try {
        const result = eval(addcla);
        setcal(String(result));
      } catch (error) {
        setcal("Error");
      }
    } else {
      setcal((oldValue) => oldValue + buttontaxt);
    }
  };

  const buttonlist = [
    "C",
    "1",
    "2",
    "3",
    "+",
    "4",
    "5",
    "6",
    "-",
    "7",
    "8",
    "9",
    "*",
    "0",
    "00",
    "000",
    "/",
    ".",
    "%",
    "=",
  ];

  return (
    <div id="buttonstyle">
      {buttonlist.map((index) => (
        <button
          className="buttonstyle"
          key={index}
          onClick={() => onclickbutton(index)}
        >
          {index}
        </button>
      ))}
    </div>
  );
}

export default Calculatorbutton;
