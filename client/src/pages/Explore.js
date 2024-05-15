import { useState, useEffect } from 'react'
import { toast } from 'react-toastify'
import Container from '../components/Container'

const Explore = () => {
    const [elements, setElements] = useState([])
	const [east, setEast] = useState([])
	const [west, setWest] = useState([])

	useEffect(() => {
		fetch('/elements')
			.then(res => {
				if (res.ok) {
					return res.json().then(setElements)
				}
				return res.json().then(errorObj => toast.error(errorObj))
			})
			.catch((err) => toast.error(err))
	}, [])

	useEffect(() => {
		fetch('/east')
			.then(res => {
				if (res.ok) {
					return res.json().then(setEast)
				}
				return res.json().then(errorObj => toast.error(errorObj))
			})
			.catch(err => toast.error(err))
	}, [])

	useEffect(() => {
		fetch('/west')
			.then(res => {
				if (res.ok) {
					return res.json().then(setWest)
				}
				return res.json().then(errorObj => toast.error(errorObj))
			})
			.catch(err => toast.error(err))
	}, [])

// ! include logic to check if user is logged in , redirect to signup page if not (explore and profile) - app or auth should handle this
// ! fixup calc_w.. doesn't populate patch and signup.
// confirm mvp once west calc works
// try sign up user for each west sign.


	return (
        <>
            <p>here's the Explore page</p>
            <p>learn more about signs, elements, etc here</p>
            {/* <> */}
            <Container data={east} type='east' />
            <Container data={west} type='west' />
            <Container data={elements} type='elements' />
            {/* </> */}
        </>
)}

export default Explore