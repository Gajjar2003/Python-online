import React from 'react'

function Emplayee(props) {
  return (
    <div>
      <h1>Emplayee-List</h1>
      <ul class="list-group">
        {props.items.map((index) =>(
            <li class="list-group-item">{index}</li>
        ))}

 
</ul>
    </div>
  )
}

export default Emplayee
