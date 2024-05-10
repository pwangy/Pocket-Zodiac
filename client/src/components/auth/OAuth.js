import { useContext, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { AuthContext } from '../../context/AuthContext'

const OAuth = () => {
	const { updateUser } = useContext(AuthContext)
	const clientId = process.env.REACT_APP_GOOGLE_CLIENT_ID
	const navigate = useNavigate()

	useEffect(() => {
		const script = document.createElement('script')
		script.src = 'https://apis.google.com/js/platform.js'
		script.async = true
		script.defer = true
		// script.onload = resolve
		script.onload = () => {
			if (window.google && window.google.accounts) {
				window.google.accounts.id.initialize({
					client_id: clientId,
					callback: handleCallbackResponse
				})
				window.google.accounts.id.renderButton(
					document.getElementById('signInDiv'),
					{ theme: 'outline', size: 'medium', text: 'continue_with' })
			} else {
			console.error('Google API failed to load')
			}
		}
		document.head.appendChild(script)
		return () => {
			document.head.removeChild(script)
		}
	}, [])

	const handleCallbackResponse = (response) => {
		fetch('/goauth', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
                'Accept': 'application/json'
			},
			body: JSON.stringify({ id_token: response.credential })
		})
			.then(res => res.json())
			.then(user => {
				updateUser(user)
				navigate(`/`)
                console.log('logged in!')
			})
			.catch(error => console.error(error))
	}

	return (
		<>
			<div id='signInDiv'></div>
		</>
	)
}

export default OAuth
