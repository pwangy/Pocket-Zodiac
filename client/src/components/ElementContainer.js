import { useContext } from 'react'
import { AuthContext } from '../context/AuthContext'
import Card from './Card'

const ElementsContainer = () => {
    const { elements } = useContext(AuthContext)
    const listElements = elements?.map(e => <Card key={e.id} {...e} />)

	return (
        <>
            <p>Elements</p>
            <p>{listElements}</p>
        </>
)}

export default ElementsContainer