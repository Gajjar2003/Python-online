import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import Todolist from './Components/Todolist'

function App() {
  const [count, setCount] = useState(0)

 const todolist = [
  {
    name: "Buy Car",
    duedate: "11/08/2026"
  },
  {
    name: "Go to Temple",
    duedate: "12/08/2026"
  },
   {
    name: "Rain For today",
    duedate: "24/07/2026"
  },
  {
    name: "Water level is high",
    duedate: "12/08/2026"
  }
]

  return (
    <>
      <Todolist itemslist={todolist}/>
    </>
  );
  }

export default App
