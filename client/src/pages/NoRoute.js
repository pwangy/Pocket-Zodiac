import { useContext } from 'react'
import { useNavigate, useRouteError } from 'react-router-dom'
import { AuthContext } from '../context/AuthContext'

const NoRoute = () => {
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
        <article className='col-nowrap'>
            {user ?  <p>{ err.errorObj }</p> : <p>Please login to view this page.</p>}
            <button className='form-button error' onClick={handleGoBack}>Go Back</button>
            <button className='form-button error' onClick={handleGoHome}>Return Home</button>
        </article>
)}

export default NoRoute