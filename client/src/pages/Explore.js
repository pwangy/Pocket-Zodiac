import { useState, useEffect } from 'react'
import ElementsContainer from '../components/elements/ElementContainer'
import WestContainer from '../components/west/WestContainer'
import EastContainer from '../components/east/EastContainer'

const Explore = () => {
    const [elements, setElements] = useState([])
	const [east, setEast] = useState([])
	const [west, setWest] = useState([])

	useEffect(() => {
		fetch('/elements')
			.then((res) => {
				if (res.ok) {
					return res.json().then(setElements)
				}
				return res.json().then((errorObj) => console.log(errorObj))
			})
			.catch((err) => console.log(err))
	}, [])

	useEffect(() => {
		fetch('/east')
			.then(res => {
				if (res.ok) {
					return res.json().then(setEast)
				}
				return res.json().then((errorObj) => console.log(errorObj))
			})
			.catch(err => console.log(err))
	}, [])

	useEffect(() => {
		fetch('/west')
			.then(res => {
				if (res.ok) {
					return res.json().then(setWest)
				}
				return res.json().then((errorObj) => console.log(errorObj))
			})
			.catch(err => console.log(err))
	}, [])


	return (
        <>
            <p>here's the Explore page</p>
            <p>learn more about signs, elements, etc here</p>
            {/* <> */}
            <EastContainer east={east} />
            <WestContainer west={west} />
            <ElementsContainer elements={elements} />
            {/* </> */}
        </>
)}

export default Explore