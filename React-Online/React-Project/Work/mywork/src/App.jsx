import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import LIst from './Components/LIst'
import EmployeeTodo from './Components/Employee'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      {/* <LIst/> */}
      <EmployeeTodo/>
    </>
  )
}

export default App
