import { useContext } from 'react'
import { NavLink } from 'react-router-dom'
import { AuthContext } from '../context/AuthContext'

const Header = () => {
	const { user, logout } = useContext(AuthContext)
	
    return (
        <>
            <h1>Pocket Zodiac</h1>
            {/* {user ? ( */}
                <>
                    <NavLink id='link' to='/' className=''>home</NavLink>
                    <NavLink id='link' to='/zodiac' className=''>my zodiac</NavLink>
                    <NavLink id='link' to='/explore' className=''>explore</NavLink>
                    <NavLink id='link' to='/' className='' onClick={logout}>Logout</NavLink>
                </>
            {/* ) : ( */}
                {/* <NavLink id='link' to='/' className='link'></NavLink> */}
            {/* )} */}
        </>
)}

export default Header
