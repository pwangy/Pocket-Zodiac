import { useContext, useEffect, useState } from 'react'
import { Outlet } from 'react-router-dom'
import { AuthContext } from './context/AuthContext'
import Header from './components/Header'
import Footer from './components/Footer'

const App = () => {
	const { user } = useContext(AuthContext)

	return (
		<main>
			<Header />
			<h3>i'm the frontend!</h3>
			<Outlet context={{ user }} />
			<Footer />
		</main>
)}

export default App
