import React from 'react'

function Color(props) {
  return (
    <div>
        <h1>Welcome to colot list</h1>

         <ul>
            {props.jenil.map((color)=>(
              <li key={color}>{color}</li>
            ))}  
          </ul> 

    </div>
  )
}

export default Color

