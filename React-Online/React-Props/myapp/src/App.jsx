import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import User from './Components/User'

import Fruits from './Components/Fruits'
import Color from './Components/Color'
import Product from './Components/Product'
import Emplayee from './Components/Emplayee'


function App() {
  const [count, setCount] = useState(0)

  //  const fruits = ["Apple", "Banana", "Mango", "Orange"];

  // const colos = ['red','blue','yellow','balck','white'] 

  // const products = ['Pc','Laptop','mouse','cpu','keyboard']

    const Emplyees = ['jenil','meet','vraj','Aniket','kram','yug','Darshan','jay','Ravi','Dhruv','prem']

  return (
    <>
      {/* <User name="jenil" age="21"/>
      
      <Fruits items={fruits}/>

      <Color jenil={colos}/>

      <Product product={products}/> */}
      <Emplayee  items = {Emplyees}/>


    </>
  )
}

export default App
