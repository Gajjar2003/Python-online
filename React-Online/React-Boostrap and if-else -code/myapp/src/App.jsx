import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import Food from './Components/Food'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Food/>
    </>
  )
}

export default App
