import { useContext } from 'react'
import { AuthContext } from '../context/AuthContext'
import ElementsContainer from '../components/ElementContainer'

const Explore = () => {
    const { elements } = useContext(AuthContext)

	return (
        <>
            <p>here's the Explore page</p>
            <p>learn more about signs, elements, etc here</p>
            {/* <> */}
            <ElementsContainer elements={elements} />
            {/* </> */}
        </>
)}

export default Explore