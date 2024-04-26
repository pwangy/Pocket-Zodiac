import { useContext } from 'react'
import { useNavigate, useRouteError } from 'react-router-dom'
import { AuthContext } from '../context/AuthContext'

const Error = () => {
    const { user } = useContext(AuthContext)
    const err = useRouteError()
    const navigate = useNavigate()

    const handleGoBack = () => {
        navigate(-1)
    }

    const handleGoHome = () => {
        navigate('/')
    }

    return (
        <article className=''>
            {user ?  <p className=''>{ err.message }</p> : <p className=''>Please login to view this page.</p>}
            <button className='' onClick={handleGoBack}>Go Back</button>
            <button className='' onClick={handleGoHome}>Return Home</button>
        </article>
)}

export default Error