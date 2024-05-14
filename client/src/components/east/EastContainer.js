// import { useOutletContext } from 'react-router-dom'
import Card from './Card'

const EastContainer = ({ east }) => {
    // const { east } = useOutletContext()
    const listEastern = east?.slice(0, 12).map(e => <Card key={e.id} {...e} />)

	return (
        <>
            <p>Eastern Signs</p>
            <article className="row-wrap">
                {listEastern}
            </article>
        </>
)}

export default EastContainer
