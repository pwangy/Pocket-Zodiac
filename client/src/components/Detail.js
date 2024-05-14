import { useLocation } from 'react-router-dom'
import { images } from '../utils/images'

const Detail = () => {
	const { state } = useLocation()

	if (!state) {
		return <h3>Checking the stars...</h3>
	}

	const { type, id, img, name, ...props } = state

	if (type === 'east') {
		return (
			<>
				<img src={images[img]} alt={`${type} icon`} className='ico' />
				<h3>{props.name_12} thing!</h3>
				{Object.entries(props).map(
					([key, value]) =>
						key !== 'name' &&
						key !== 'start' &&
						key !== 'end' &&
						key !== 'start1' &&
						key !== 'end1' &&
						key !== 'id' &&
                        key !== 'element_id' &&
                        key !== 'element' &&
                        key !== 'order_12' &&
                        key !== 'order_60' &&
                        key !== 'name_12' &&
                        (<p key={key}>
                            <strong>
                                {key.charAt(0).toUpperCase() + key.slice(1)}
                                :
                            </strong>{' '}
								{value instanceof Object ? JSON.stringify(value) : value}
						</p>)
				)}
			</>
		)
	} else if (type === 'west') {
		return (
			<>
				<img src={images[img]} alt={`${type} icon`} className='ico' />
				<h3>{name} thing!</h3>
				{Object.entries(props).map(
					([key, value]) =>
						key !== 'name' &&
						key !== 'start' &&
						key !== 'end' &&
						key !== 'id' &&
						key !== 'symbol' &&
                        (<p key={key}>
                            <strong>
                                {key.charAt(0).toUpperCase() + key.slice(1)}
                                :
                            </strong>{' '}
								{value instanceof Object ? JSON.stringify(value) : value}
						</p>)
				)}
			</>
		)
	} else {
        return (
			<>
				<img src={images[img]} alt={`${type} icon`} className='ico' />
				<h3>{name} thing!</h3>
				{Object.entries(props).map(
					([key, value]) =>
						key !== 'name' && (
							<p key={key}>
								<strong>
									{key.charAt(0).toUpperCase() + key.slice(1)}
									:
								</strong>{' '}
								{value instanceof Object
									? JSON.stringify(value)
									: value}
							</p>
						)
				)}
			</>
		)
    }
}

export default Detail
