import { useContext } from 'react'
import { Outlet } from 'react-router-dom'
import { ToastContainer } from 'react-toastify'
import { AuthContext } from './context/AuthContext'
import Header from './components/Header'
import Footer from './components/Footer'

const App = () => {
	const { user } = useContext(AuthContext)
	return (
		<main>
			<Header />
			<ToastContainer role='alert' stacked />
			<Outlet context={{ user }} />
			<Footer />
		</main>
)}

export default App
