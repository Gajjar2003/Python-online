import React from 'react'

function Product(props) {
  return (
    <div>
        <h1>Products-Items-Lits</h1>
          <ul>
            {props.product.map((abc)=>(
              <li key={abc}>{abc}</li>
            ))}
          </ul>
    </div>
  )
}

export default Product
