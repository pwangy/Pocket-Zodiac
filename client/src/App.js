import { useContext } from 'react'
import { Outlet } from 'react-router-dom'
import { ToastContainer, Bounce } from 'react-toastify'
import { AuthContext } from './context/AuthContext'
import Header from './components/Header'
import Footer from './components/Footer'

const App = () => {
	const { user } = useContext(AuthContext)
	const options = {
        position: 'top-left',
        autoClose: 5000,
        hideProgressBar: true,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: 'dark',
        transition: Bounce,
        role: 'alert',
        isLoading: false, 
        data: null,
        icon: false,
    }

	return (
		<main>
			<Header />
			<ToastContainer role='alert' stacked options />
			<Outlet context={{ user }} />
			<Footer />
		</main>
)}

export default App
