// import { useContext } from 'react'
// import { AuthContext } from '../context/AuthContext'
import { useOutletContext } from 'react-router-dom'
import ElementsContainer from '../components/ElementContainer'

const Explore = () => {
    const { elements } = useOutletContext()

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