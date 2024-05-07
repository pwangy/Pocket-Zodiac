import { useContext, useEffect, useState } from 'react'
import { Outlet } from 'react-router-dom'
import { AuthContext } from './context/AuthContext'
import Header from './components/Header'
import Footer from './components/Footer'

const App = () => {
	const { user } = useContext(AuthContext)
	const [elements, setElements] = useState([])
	const [east, setEast] = useState([])
	const [west, setWest] = useState([])

	useEffect(() => {
		fetch('/elements')
			.then((res) => {
				if (res.ok) {
					return res.json().then(setElements)
				}
				return res.json().then((errorObj) => console.log(errorObj))
			})
			.catch((err) => console.log(err))
	}, [setElements])

	useEffect(() => {
		fetch('/east')
			.then(res => {
				if (res.ok) {
					return res.json().then(setEast)
				}
				return res.json().then((errorObj) => console.log(errorObj))
			})
			.catch(err => console.log(err))
	}, [setEast])

	useEffect(() => {
		fetch('/west')
			.then(res => {
				if (res.ok) {
					return res.json().then(setWest)
				}
				return res.json().then((errorObj) => console.log(errorObj))
			})
			.catch(err => console.log(err))
	}, [setWest])


	return (
		<main>
			<Header />
			<h3>i'm the frontend!</h3>
			<Outlet context={{ user, elements, east, west }} />
			<Footer />
		</main>
)}

export default App
