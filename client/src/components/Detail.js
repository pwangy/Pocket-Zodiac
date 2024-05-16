import { useLocation } from 'react-router-dom'
import { toast } from 'react-toastify'
import { images } from '../utils/images'


const Detail = () => {
	const { state } = useLocation()

	if (!state) {
		return toast.loading(<h3>Checking the stars...</h3>)
	}

	const { type, id, img, name, ...props } = state

	if (type === 'east') {
		return (
			<div className='detail-container col-nowrap'>
				<img src={images[img]} alt={`${type} icon`} className='ico detail' />
				<h3 className='exp'>{props.name_12}</h3>
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
			</div>
		)
	} else if (type === 'west') {
		return (
			<div className='detail-container col-nowrap'>
				<img src={images[img]} alt={`${type} icon`} className='ico detail' />
				<h3 className='exp'>{name}</h3>
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
			</div>
		)
	} else {
        return (
			<div className='detail-container col-nowrap'>
				<img src={images[img]} alt={`${type} icon`} className='ico detail' />
				<h3 className='exp'>{name}</h3>
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
			</div>
		)
    }
}

export default Detail
