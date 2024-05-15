import { useContext } from 'react'
import { Outlet } from 'react-router-dom'
import { toast, ToastContainer, Bounce } from 'react-toastify'
import { AuthContext } from './context/AuthContext'
// import { ToastContext } from './context/ToastContext'
import Header from './components/Header'
import Footer from './components/Footer'

const App = () => {
	const { user } = useContext(AuthContext)
	// const { toastState } = useContext(ToastContext)

	return (
		<main>
			<Header />
			<ToastContainer role='alert' stacked />
			<Outlet context={{ user }} />
			<Footer />
		</main>
)}

export default App
