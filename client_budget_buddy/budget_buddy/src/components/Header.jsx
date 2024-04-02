import { useNavigate } from "react-router-dom"
import {Link} from 'react-router-dom'
import Nav from './Nav'

export default function Header(){
    const navigate = useNavigate()
    return(
        <div className="header-container">
            <div className="nav-container">
                <Nav />
            </div>
        </div>
    )
}