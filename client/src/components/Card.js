import { Link } from 'react-router-dom'
import { images } from '../utils/images'

const Card = ({ id, img, name, type, ...props }) => {
    return (
        <div className='card'>
            <img src={ images[img] } alt={`${type} icon`} className='ico' />
            <Link to={{
                pathname: `/${type}/${id}`,
                state: { id, img, name, type, ...props }
            }}>
                <h6>{ props.name_12 || props.name }</h6>
            </Link>
        </div>
)}

export default Card