import React from 'react'

function Calculatorbutton() {

  const buttonlist = ['C','1','2','+','3','4','-','5','6','*','7','8','/','9','0','%','.','=']
  return (
    <div>
           <div id="buttonstyle">{buttonlist.map((index)=>(
              <button className=" buttonstyle" >{index}</button>
           ))}
        
      
      </div>
    </div>
  )
}

export default Calculatorbutton
