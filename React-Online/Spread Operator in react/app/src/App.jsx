import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import List from './Components/List'
import Input from './Components/Input'
import Product from './Components/Product'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    {/* <List/> */}
    {/* <Input/> */}
    <Product/>
    </>
  )
}

export default App
