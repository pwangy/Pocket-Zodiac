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
		pauseOnFocusLoss: true,
		newestOnTop: true,
        draggable: true,
        progress: undefined,
        transition: Bounce,
        role: 'alert'
    }

	return (
		<main>
			<Header />
			<ToastContainer role='alert' stacked options={options} />
			<Outlet context={{ user }} />
			<Footer />
		</main>
)}

export default App
