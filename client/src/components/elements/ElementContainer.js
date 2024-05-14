import { useOutletContext } from 'react-router-dom'
import Card from '../Card'

const ElementsContainer = () => {
    const { elements } = useOutletContext()
    const listElements = elements?.map(e => <Card key={e.id} {...e} />)

	return (
        <>
            <p>Elements</p>
            <article className="row-wrap">
                {listElements}
            </article>
        </>
)}

export default ElementsContainer

