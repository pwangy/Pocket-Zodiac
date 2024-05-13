import { Link } from 'react-router-dom'
import aries from '../../assets/west/128-aries.png'
import taurus from '../../assets/west/128-taurus.png'
import gemini from '../../assets/west/128-gemini.png'
import cancer from '../../assets/west/128-cancer.png'
import leo from '../../assets/west/128-leo.png'
import virgo from '../../assets/west/128-virgo.png'
import libra from '../../assets/west/128-libra.png'
import scorpio from '../../assets/west/128-scorpio.png'
import sagittarius from '../../assets/west/128-sagittarius.png'
import capricorn from '../../assets/west/128-capricorn.png'
import aquarius from '../../assets/west/128-aquarius.png'
import pisces from '../../assets/west/128-pisces.png'

const Card = ({ id, name, img }) => {
    const images = {
        '128-aries.png': aries,
        '128-taurus.png': taurus,
        '128-gemini.png': gemini,
        '128-cancer.png': cancer,
        '128-leo.png': leo,
        '128-virgo.png': virgo,
        '128-libra.png': libra,
        '128-scorpio.png': scorpio,
        '128-sagittarius.png': sagittarius,
        '128-capricorn.png': capricorn,
        '128-aquarius.png': aquarius,
        '128-pisces.png': pisces
    }

    return (
        <div className='card'>
            <img src={images[img]} alt='element icon' className='ico' />
            <Link to={`/west/${id}`}>
                <h6>{name}</h6>
            </Link>
        </div>
)}

export default Card