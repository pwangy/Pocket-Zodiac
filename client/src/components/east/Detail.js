import { useContext, useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import { AuthContext } from '../../context/AuthContext' 

const Detail = () => {
    const { id } = useParams()
    const { elements } = useContext(AuthContext)
    const [element, setElement] = useState(null)
    const { name, qualities, desc, season, direction, planet, number, smell, taste, organ, color } = element

    useEffect(() => {
        const selectedElement = elements.find(e => e.id === id)
        setElement(selectedElement) 
    }, [id, elements])

    return (
        <>
            {/* <img src=''></img> */}
            <h3>{name}</h3>
            <p>{qualities}</p>
            <p>{desc}</p>
            <p>{season}</p>
            <p>{direction}</p>
            <p>{planet}</p>
            <p>{number}</p>
            <p>{smell}</p>
            <p>{taste}</p>
            <p>{organ}</p>
            <p>{color}</p>

        </>
    )
}

export default Detail