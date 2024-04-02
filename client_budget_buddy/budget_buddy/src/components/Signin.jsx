import '../styles/Signin.css'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
export default function Signin() {

  const navigation = useNavigate()

  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  const HandleNavigation = () => {
    navigation('/signup')
  }

  const HandleSubmit = async (e) => {
    e.preventDefault()

    const response = await fetch('http://localhost:8000/signin', {
      method: 'POST',
      headers: {
        'ContentType': 'application/json'
      },
      credentials: 'include',
      body: JSON.stringify({
        email, password

      })
    })
  }

  return (
    <div className="main-signin">
      <div className="header-container">
        <p className='title'>Budget Buddy</p>
        <p className='slogon'> Chart Your Finances with Budget Buddy</p>
      </div>
      {/* <main className="form-signin w-100 m-auto"> */}
      <form onSubmit={HandleSubmit}>

        <h1 className="h3 mb-3 fw-normal">Please sign in</h1>

        <div className="form-floating">
          <input type="email" className="form-control" id="floatingInput" placeholder="name@example.com" onChange={e => setEmail(e.target.value)} />
          <label htmlFor="floatingInput">Email address</label>
        </div>
        <div className="form-floating">
          <input type="password" className="form-control" id="floatingPassword" placeholder="Password" onChange={e => setPassword(e.target.value)} />
          <label htmlFor="floatingPassword">Password</label>
        </div>

        <button className="btn btn-primary w-100 py-2" type="submit">Sign in</button><br></br><br />
        <button className="btn btn-primary sign-up w-100 py-2" type="button" onClick={HandleNavigation}>Sign Up</button>

      </form>
      {/* </main> */}
      <div className="footer-container">
        <p className="mt-5 mb-3 text-body-secondary">&copy; 2024</p>
      </div>
    </div>
  )
}