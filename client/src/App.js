import { useContext, useEffect, useState } from 'react'
import { Outlet } from 'react-router-dom'
import { ToastContainer, toast, Bounce } from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'
import { AuthContext } from './context/AuthContext'
import Header from './components/Header'
import Footer from './components/Footer'

const App = () => {
	const { user } = useContext(AuthContext)
	const notify = () => {
		toast('Welcome to the frontend!', { 
			autoClose: 2000,
			position: "top-left",
			hideProgressBar: false,
			closeOnClick: true,
			pauseOnHover: true,
			draggable: true,
			progress: undefined,
			theme: "dark",
			transition: Bounce,
			role: 'alert'
		})
	}

	return (
		<main>
			<Header />
			<ToastContainer role='alert' />
			<h3>i'm the frontend!</h3>
			<Outlet context={{ user }} />
			<Footer />
		</main>
)}

export default App
