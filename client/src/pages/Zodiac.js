import { useContext, useState, useEffect } from 'react'
import { AuthContext } from '../context/AuthContext'

const Zodiac = () => {
	const { user } = useContext(AuthContext)
	const [userZodiac, setUserZodiac] = useState(null)

	useEffect(() => {
		fetch(`/userzodiacbyid/${user.id}`)
			.then(res => {
				if (!res.ok) {
					return res.json().then(errorObj => console.log(errorObj))
				}
				return res.json()
			.then(data => setUserZodiac(data))
			.then(console.log(userZodiac))
			})
			.catch(err => console.log(err))
		}, [])

	if (!user) return <h3>Checking the stars...</h3>

	return (
		<>
			<p>Hello, {user.username}.</p>
			<p>these are your signs</p>
			{/* <p>{userZodiac.west_id}</p> */}
			{/* <p>{userZodiac.east_id}</p> */}
			{/* <p>{userZodiac.west_id}</p> */}
		</>
)}

export default Zodiac
