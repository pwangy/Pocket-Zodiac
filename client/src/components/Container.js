import Card from './Card'

const Container = ({ data, type }) => {
    const typeNames = {
        'east': 'Eastern Zodiac',
        'west': 'Western Zodiac',
        'elements': 'Elements'
    }

	let listItems
	switch (type) {
		case 'east':
            listItems = data?.slice(0, 12).map((e) => <Card key={e.id} type={type} {...e} />)
            break
        case 'west':
            listItems = data?.map((e) => <Card key={e.id} type={type} {...e} />)
            break;
        case 'elements':
            listItems = data?.map((e) => <Card key={e.id} type={type} {...e} />)
            break
        default:
            listItems = null
    }

    return (
        <>
            <p>{typeNames[type]}</p>
            <article className='row-wrap'>
                {listItems}
            </article>
        </>
)}

export default Container
