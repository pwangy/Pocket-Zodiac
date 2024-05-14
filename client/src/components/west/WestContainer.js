// import { useOutletContext } from 'react-router-dom'
import Card from './Card'

const WestContainer = ({ west }) => {
    // const { west } = useOutletContext()
    const listWestern = west?.map(e => <Card key={e.id} {...e} />)

	return (
        <>
            <p>Western Signs</p>
            <article className="row-wrap">
                {listWestern}
            </article>
        </>
)}

export default WestContainer

