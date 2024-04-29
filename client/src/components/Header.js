import { useContext } from 'react'
import { NavLink } from 'react-router-dom'
import { AuthContext } from '../context/AuthContext'

const Header = () => {
	const { user, logout } = useContext(AuthContext)
	
    return (
        <>
            <h1>Pocket Chinese Astrology</h1>
            {/* {user ? ( */}
                <>
                    <NavLink id='link' to='/' className=''>link</NavLink>
                    <NavLink id='link' to='/' className='' onClick={logout}>Logout</NavLink>
                </>
            {/* ) : ( */}
                <NavLink id='link' to='/' className='link'></NavLink>
            {/* )} */}
        </>
)}

export default Header
