import { useContext } from 'react'
import { NavLink } from 'react-router-dom'
import { UserContext } from '../context/UserContext'

const Nav = () => {
	const { user, logout } = useContext(UserContext)
	
    return (
        <header>
            <h1>Pocket Astro</h1>
            <nav>
                {user ? (
                    <>
                        <NavLink id='link' to='/' className=''>link</NavLink>
                        <NavLink id='link' to='/' className='nav-link' onClick={logout}>Logout</NavLink>
                    </>
                ) : (
                    <NavLink id='link' to='/' className='link'></NavLink>
                )}
            </nav>
        </header>
)}

export default Nav
