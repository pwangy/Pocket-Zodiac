import { useNavigate } from 'react-router-dom'
import { images } from '../utils/images'

const Card = ({ type, id, img, name, ...props }) => {
    const navigate = useNavigate()
    // console.log(type)

    if (type === 'east') {
        return (
            <div onClick={() => navigate(`/${type}/${id}`, {state: { type, id, img, name, ...props }})}>
                <img src={ images[img] } alt={`${name} icon`} className='ico' />
                {/* <Link to={{ pathname: `/${type}/${id}`, state: { type, id, img, name, ...props }}}> */}
                <h6>{props.name_12}</h6>
                {/* </Link> */}
        </div>
        )
    } else {
        return (
            <div onClick={() => navigate(`/${type}/${id}`, {state: { type, id, img, name, ...props }})} className='card'>
                <img src={ images[img] } alt={`${name} icon`} className='ico' />
                {/* <Link to={{ pathname: `/${type}/${id}`, state: { type, id, img, name, ...props }}}> */}
                <h6>{name}</h6>
                {/* </Link> */}
            </div>
    )}
}

export default Card