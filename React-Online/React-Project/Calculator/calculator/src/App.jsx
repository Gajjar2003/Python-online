import React, { useState } from "react";
import Calculatorinput from "./Components/Calculatorinput";

function App() {
  const [addcla, setcal] = useState("");

  return (
    <>
      <Calculatorinput
        display={addcla}
        setcal={setcal}
        addcla={addcla}
      />
    </>
  );
}

export default App;