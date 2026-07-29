import React, { useState } from 'react'

function List() {

 const [newadd,setnew] =useState(['a','b','c'])

 const additems = (e)=>{
    console.log(e);
    console.log(e.target.value);

    const newarray = e.target.value;
    const newitems = [...newadd,newarray]
    setnew(newitems)
    console.log(newitems);
    
    
    
 }
  
 

  return (
    <div>
      <h1>List-app</h1>

      <button onClick={additems}>Add</button>

      {newadd.map((index)=>(
        <li key={index}>{index}</li>
      ))}
    </div>
  )
}

export default List
