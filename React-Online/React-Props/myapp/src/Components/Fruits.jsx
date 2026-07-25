import React from 'react'

function Fruits(props) {
  return (
    <div>
      <h1>Fruits</h1>

      <ul>
        {props.items.map((fruit) => (
          <li key={fruit}>{fruit}</li>
        ))}
      </ul>
    </div>
  )
}

export default Fruits