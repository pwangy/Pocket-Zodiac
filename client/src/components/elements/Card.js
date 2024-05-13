import { Link } from 'react-router-dom'
import earth from '../../assets/elements/128-earth.png'
import fire from '../../assets/elements/128-fire.png'
import water from '../../assets/elements/128-water.png'
import wood from '../../assets/elements/128-wood.png'
import metal from '../../assets/elements/128-metal.png'

const Card = ({ id, name, img }) => {
    const images = {
        '128-earth.png': earth,
        '128-fire.png': fire,
        '128-water.png': water,
        '128-wood.png': wood,
        '128-metal.png': metal,
    }

    return (
        <div className='card'>
            <img src={images[img]} alt='element icon' className='ico' />
            <Link to={`/element/${id}`}>
                <h6>{name}</h6>
            </Link>
        </div>
)}

export default Card