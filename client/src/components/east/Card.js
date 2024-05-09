import { Link } from 'react-router-dom'
import Placeholder from '../../assets/elements/solarsystem.png'

const Card = ({ id, name_12, }) => {

    return (
        <div className='card'>
            <img src={Placeholder} alt='element icon' className='ico' />
            <Link to={`/west/${id}`}>
                <h6>{name_12}</h6>
            </Link>
        </div>
)}

export default Card