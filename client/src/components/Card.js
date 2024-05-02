import { Link } from 'react-router-dom'

const Card = ({ id, name, qualities, desc, season, direction, planet, number, smell, taste, organ, color }) => {
    
    return (
        <article>
            <Link to={`/element/${id}`}>
                <img src=''></img>
                <h3>{name}</h3>
            </Link>
        </article>
    )
}

export default Card