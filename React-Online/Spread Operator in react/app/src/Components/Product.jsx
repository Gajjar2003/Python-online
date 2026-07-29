import React, { useState } from 'react'

function Product() {

  const [newproduct,setproduct] = useState([])

  const changeitems = (e) =>{
    if(e.key === 'Enter'){
      let newadd = e.target.value;
      let itemsadd = [...newproduct,newadd]
      setproduct(itemsadd)
      console.log(e);
      console.log(itemsadd);

      e.target.value ="";
      
    }
    
    
    
  }


  return (
    <div>
      <h2>Product-application</h2>
      <input type="text" placeholder='Enter Your Product ....' onKeyDown={changeitems}/>

      <ul>
        {newproduct.map((index)=>(
        <li key={index}>{index}</li>

        ))}
      </ul>
    </div>
  )
}

export default Product
