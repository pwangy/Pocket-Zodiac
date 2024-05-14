import { useLocation } from 'react-router-dom'
import { images } from '../utils/images'

const Detail = () => {
    const { state } = useLocation()
    const { type, id, img, ...props } = state

    return (
        <>
            <img src={ images[img] } alt={`${type} icon`} className='ico' />
            <h3>{type} thing!</h3>
            {Object.entries(props).map(([key, value]) => 
                key !== 'name' && <p key={key}><strong>{key.charAt(0).toUpperCase() + key.slice(1)}:</strong> {value}</p>)}
        </>
    )}

export default Detail