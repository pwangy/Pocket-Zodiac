import { useOutletContext } from 'react-router-dom'
import ElementsContainer from '../components/elements/ElementContainer'
import WestContainer from '../components/west/WestContainer'

const Explore = () => {
    const { elements, east, west } = useOutletContext()

	return (
        <>
            <p>here's the Explore page</p>
            <p>learn more about signs, elements, etc here</p>
            {/* <> */}
            <WestContainer west={west} />
            <ElementsContainer elements={elements} />
            {/* </> */}
        </>
)}

export default Explore