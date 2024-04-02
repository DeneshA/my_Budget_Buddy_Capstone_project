import React, { useState } from 'react'
import Header from './components/Header'
import Main from './components/Main'
import Footer from './components/Footer'

import './App.css'
import Signin from './components/Signin'

function App() {
  const [count, setCount] = useState(0)

  return (

    <div className='Budget-Buddy-App'>
      <Signin />     
    </div>

  )
}

export default App
