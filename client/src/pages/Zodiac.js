import { useContext, useState, useEffect } from 'react'
import { toast } from 'react-toastify'
import { AuthContext } from '../context/AuthContext'
import { images } from '../utils/images'

const Zodiac = () => {
	const { user, getCookie } = useContext(AuthContext)
	// const [east, setEast] = useState(null)
	// const [element, setElement] = useState(null)
	// const [west, setWest] = useState(null)

	// useEffect(() => {
	// 	const fetchUserZodiac = async () => {
	// 		if (user) {
	// 			const token = getCookie('csrf_access_token')
	// 			const url = `/userzodiacbyid/${user.id}`
	// 			try {
	// 				const res = await fetch(url, {
	// 					method: 'GET',
	// 					headers: {
	// 						'Content-Type': 'application/json',
	// 						'X-CSRF-TOKEN': token
	// 					}
	// 				})
	// 				.then(res => {
	// 						if (!res.ok) {
	// 							return res.json().then(errorObj => toast.error(errorObj))
	// 						}
	// 						return res.json()
	// 					})
	// 				.then(data => {
	// 					setEast(data.east)
	// 					setWest(data.west)
	// 					setElement(data.east.element)
	// 					})
	// 				.catch(err => toast.error(err))
	// 			} catch (err) {
	// 				toast.error(err)
	// 			}
	// 	}}
	// 	fetchUserZodiac()
	// }, [user])

	// useEffect(() => {
	// 	console.log('east:', east)
	// 	console.log('west:', west)
	// 	console.log('element:', element)
	// }, [east, west, element])

	if (!user) return <h3>Checking the stars...</h3>
	const {east, west} = user.user_zodiacs[0]

	return (
		<>
			<p>Here's your personal zodiac, {user.username}.</p>
			<div>
				{east.img && <img src={ images[east.img]} alt={east.name} className='ico' />}
				<h3>Eastern Sign: {east.name}</h3>
				{Object.entries(east).map(
					([key, value], index) =>
						key !== 'id' && 
						key !== 'img' && 
						key !== 'element' &&
						key !== 'element_id' &&
						key !== 'order_12' &&
						key !== 'order_60' &&
						key !== 'name_12' &&
						key !== 'start' &&
						key !== 'end' &&
						key !== 'start1' &&
						key !== 'end1' &&
						(<p key={index}>{key}: {value}</p>)
				)}
				{east.element.img && <img src={ images[east.element.img]} alt={east.element.name} className='ico' />}
				<p>Element: {typeof east.element === 'object' ? 
					Object.entries(east.element).map(
						([key, value], index) =>
							key !== 'id' && 
							key !== 'img' && 
						(<p key={index}>{key}: {value}</p>)
						) : ''}</p>
			</div>
			<div>
				{west.img && <img src={ images[west.img]} alt={west.name} className='ico' />}
				<h3>Western Sign: {west.name}</h3>
				{Object.entries(west).map(
					([key, value], index) =>
						key !== 'id' && 
						key !== 'img' && 
						key !== 'symbol' &&
						key !== 'start' &&
						key !== 'end' &&
						key !== 'name' &&
						(<p key={index}>{key}: {value}</p>)
				)}
			</div>
		</>
)}

export default Zodiac
