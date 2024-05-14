import { useContext } from 'react'
import { NavLink } from 'react-router-dom'
import { AuthContext } from '../context/AuthContext'

const Header = () => {
	const { user, logout } = useContext(AuthContext)

    return (
        <header>
            <h1>Pocket Zodiac</h1>
            {user ? (
                <>
                    <NavLink id='link' to={`/edit/${user.id}`} className='nav'>profile</NavLink>
                    <NavLink id='link' to='/zodiac' className='nav'>my zodiac</NavLink>
                    <NavLink id='link' to='/explore' className='nav'>explore</NavLink>
                    <NavLink id='link' to='/' className='nav' onClick={logout}>Logout</NavLink>
                </>
            ) : (
                ''
            )}
        </header>
)}

export default Header
