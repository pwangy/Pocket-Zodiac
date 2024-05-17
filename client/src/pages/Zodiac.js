import { useContext } from 'react'
import { AuthContext } from '../context/AuthContext'
import { images } from '../utils/images'

const Zodiac = () => {
	const { user } = useContext(AuthContext)

	if (!user) return <h3>Checking the stars...</h3>
	const {east, west} = user.user_zodiacs[0]

	return (
		<>
			<h3 className='em'>Here's your personal zodiac, {user.username}.</h3>
			<div className='detail-container col-nowrap'>
				<div className='wrap'>
					{east.img && <img className='ico detail' src={ images[east.img]} alt={east.name} />}
					<h3 className='exp'>Eastern Sign: {east.name}</h3>
					{Object.entries(east).map(
						([key, value], index) => {
							key = key === 'desc' ? 'description' : key
							key = key === 'western_counterpart' ? 'western counterpart' : key
							return (
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
								(<p className='text' key={index}>
									<strong>{key}:</strong> {value}
								</p>)
						)}
					)}

					{east.element.img && <img src={ images[east.element.img]} alt={east.element.name} className='ico detail next' />}
					<h3 className='exp'>Element: {east.element.name}</h3>
					{typeof east.element === 'object' ? 
						Object.entries(east.element).map(
							([key, value], index) => {
								key = key === 'desc' ? 'description' : key
								return (
									key !== 'id' && 
									key !== 'img' && 
									(<p className='text' key={index}><strong>{key}:</strong> {value}</p>)
								)}
						) : ''
					}
				</div>
				<div className='detail-container col-nowrap'>
					{west.img && <img src={ images[west.img]} alt={west.name} className='ico detail next' />}
					<h3 className='exp'>Western Sign: {west.name}</h3>
					{Object.entries(west).map(
						([key, value], index) => {
							key = key === 'desc' ? 'description' : key
							return (
								key !== 'id' && 
								key !== 'img' && 
								key !== 'symbol' &&
								key !== 'start' &&
								key !== 'end' &&
								key !== 'name' &&
								(<p className='text' key={index}><strong>{key}:</strong> {value}</p>)
						)}
					)}
				</div>
			</div>
		</>
)}

export default Zodiac
