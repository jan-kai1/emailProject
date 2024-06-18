import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
// import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import DisplayEmail from "./displayEmail"
import Navbar from "./Navbar"

function App() {
  const [count, setCount] = useState(0)
  
 
  const [emailData, setEmailData] = useState([])
  const [isLoading, setLoading] = useState(false)
  document.title = "email Project"
  
  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/data")
    .then(response => response.json())
    .then(data => {
      console.log(data)
      
      setEmailData(data)
    })
  
    .catch(error => {
      console.error("error fetching", error)
      setTimeout(getData, 500)
    })
      
  }, [])
  
  const getData = () => {
    fetch("http://127.0.0.1:5000/api/data")
    .then(response => response.json())
    .then(data => {
      console.log(data)
      setEmailData(data)
    } )
  }
  return (
    <div className ="d-flex flex-column vh-100 bg-dark text-white"> 
      <Navbar />
      <div className="d-flex flex-column  justify-content-center align-items-center" >
          
          <div>
            {emailData ? <DisplayEmail emails = {emailData}/> : <p></p>}
            
            
            {isLoading ? <p>Loading</p> : <p>not loading</p>}
            <button class = "btn btn-primary" onClick = {getData}>getData</button>
            <button class ="btn btn-primary" onClick = {() => setLoading(!isLoading)}>Display Email</button>
          </div>
          
        </div >
    </div>
  
  )
}

export default App
