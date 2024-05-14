import { useLocation } from 'react-router-dom'

const Detail = () => {
    const { state } = useLocation()
    const { id, name, gloss, desc, qualities, element, modality, planet, house, img } = state

    return (
        <>
            {/* <img src=''></img> */}
            <h3>{name}</h3>
            <p>{qualities}</p>
            <p>{desc}</p>
            <p>{planet}</p>
        </>
    )
}

export default Detail