import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import Clockhedding from './Components/Clockhedding'
import Clocktext from './Components/Clocktext'
import Clocktime from './Components/Clocktime'
import "bootstrap/dist/css/bootstrap.min.css"



function App() {
  const [count, setCount] = useState(0)

  return (
    <center>  
     <Clockhedding/>
     <Clocktext/>
     <Clocktime/>
    </center>
  )
}

export default App
