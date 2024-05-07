import { Link } from 'react-router-dom'
import Placeholder from '../../assets/elements/solarsystem.png'

const Card = ({ id, name }) => {

    return (
        <div className='card'>
            <img src={Placeholder} alt='element icon' className='ico' />
            <Link to={`/west/${id}`}>
                <h6>{name}</h6>
            </Link>
        </div>
)}

export default Card