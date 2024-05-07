import { Link } from 'react-router-dom'
import Placeholder from '../../assets/elements/solarsystem.png'

const Card = ({ id, name, qualities, desc, season, direction, planet, number, smell, taste, organ, color }) => {

    return (
        <div className='card'>
            <img src={Placeholder} alt='element icon' className='ico' />
            <Link to={`/element/${id}`}>
                <h6>{name}</h6>
            </Link>
        </div>
)}

export default Card