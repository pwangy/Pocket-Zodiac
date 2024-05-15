import { useNavigate } from 'react-router-dom'
import { images } from '../utils/images'

const Card = ({ type, id, img, name, ...props }) => {
    const navigate = useNavigate()

    if (type === 'east') {
        return (
            <div onClick={() => navigate(`/${type}/${id}`, {state: { type, id, img, name, ...props }})}>
                <img src={ images[img] } alt={`${name} icon`} className='ico' />
                <h6>{props.name_12}</h6>
        </div>
        )
    } else {
        return (
            <div onClick={() => navigate(`/${type}/${id}`, {state: { type, id, img, name, ...props }})} className='card'>
                <img src={ images[img] } alt={`${name} icon`} className='ico' />
                <h6>{name}</h6>
            </div>
    )}
}

export default Card