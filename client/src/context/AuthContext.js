import { createContext, useState, useEffect } from 'react'
// import { useNavigate } from 'react-router-dom'

export const AuthContext = createContext()

const AuthProvider = ({ children }) => {
	const [user, setUser] = useState(null)
	const updateUser = (user) => setUser(user)
	const [elements, setElements] = useState([])
	// const [somethingtoedit, setsomethingtoedit] = useSttate(false)
	// const navigate = useNavigate()

	const getCookie = (name) => {
		const value = `; ${document.cookie}`
		const parts = value.split(`; ${name}=`)
		if (parts.length === 2) return parts.pop().split(';').shift()
	}

	useEffect(() => {
		fetch('/elements')
			.then((res) => {
				if (res.ok) {
					return res.json().then(setElements)
				}
				return res.json().then((errorObj) => console.log(errorObj))
			})
			.catch((err) => console.log(err))
	}, [setElements])

	useEffect(() => {
		fetch('/me', {
			headers: {
				'X-CSRF-TOKEN': getCookie('csrf_access_token')
			},
		})
		.then((res) => {
			if (res.ok) {
				res.json().then(updateUser)
			} else {
				fetch('/refresh', {
					method: 'POST',
					headers: {
						'X-CSRF-TOKEN': getCookie('csrf_refresh_token'),
					}
				})
				.then((res) => {
					if (res.ok) {
						res.json().then(updateUser)
					} else {
						// navigate('/auth')
						console.error('Please log in.')
					}
				})
			}
		})
	}, [])

	const login = (user) => {
		setUser(user)
		console.log('user logged in!')
	}

	const logout = (user) => {
		fetch('/logout', { method: 'DELETE' })
			.then((res) => {
				if (res.status === 204) {
					setUser(null)
					console.log('logged out!')
				}
			})
			.catch((err) => console.log(err))
	}

	return (
		<AuthContext.Provider value={{ user, login, logout, elements }}>
			{children}
		</AuthContext.Provider>
	)
}

export default AuthProvider
