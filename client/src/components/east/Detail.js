// import { useContext, useState, useEffect } from 'react'
import { useLocation } from 'react-router-dom'
// import { AuthContext } from '../../context/AuthContext' 

const Detail = () => {
    const { state } = useLocation()
    console.log(state)

    return (
        <>
            {/* <img src=''></img> */}
            <h3>east thing!</h3>
            {/* <p>{desc}</p> */}
        </>
    )
}

export default Detail