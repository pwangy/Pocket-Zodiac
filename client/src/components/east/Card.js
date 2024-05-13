import { Link } from 'react-router-dom'
import rat from '../../assets/east/128-rat.png'
import ox from '../../assets/east/128-ox.png'
import tiger from '../../assets/east/128-tiger.png'
import rabbit from '../../assets/east/128-rabbit.png'
import dragon from '../../assets/east/128-dragon.png'
import snake from '../../assets/east/128-snake.png'
import horse from '../../assets/east/128-horse.png'
import goat from '../../assets/east/128-goat.png'
import monkey from '../../assets/east/128-monkey.png'
import rooster from '../../assets/east/128-rooster.png'
import dog from '../../assets/east/128-dog.png'
import pig from '../../assets/east/128-pig.png'

const Card = ({ id, name_12, img }) => {
    const images = {
        '128-rat.png': rat,
        '128-ox.png': ox,
        '128-tiger.png': tiger,
        '128-rabbit.png': rabbit,
        '128-dragon.png': dragon,
        '128-snake.png': snake,
        '128-horse.png': horse,
        '128-goat.png': goat,
        '128-monkey.png': monkey,
        '128-rooster.png': rooster,
        '128-dog.png': dog,
        '128-pig.png': pig
    }

    return (
        <div className='card'>
            <img src={images[img]} alt='element icon' className='ico' />
            <Link to={`/west/${id}`}>
                <h6>{name_12}</h6>
            </Link>
        </div>
)}

export default Card