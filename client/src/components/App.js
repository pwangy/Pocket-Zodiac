import { useContext } from 'react'
import { Outlet } from 'react-router-dom'
import { AuthContext } from '../context/AuthContext'
import Header from './Header'
import Footer from './Footer'

const App = () => {
	const { user } = useContext(AuthContext)
	
	return (
		<>
			<Header />
			<h1>i'm the frontend!</h1>
			<Outlet context={{ user }} />
			<Footer />
		</>
)}

export default App
