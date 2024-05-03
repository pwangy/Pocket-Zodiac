import { createContext, useState, useEffect } from 'react'

export const AuthContext = createContext()

const AuthProvider = ({ children }) => {
	const [user, setUser] = useState(null)
	const updateUser = (user) => setUser(user)
	// const [username, setUsername] = useState('')
	// const updateUsername = (user) => setUsername(user.username)
	// const [somethingtoedit, setsomethingtoedit] = useSttate(false)

	const getCookie = (name) => {
		const value = `; ${document.cookie}`
		const parts = value.split(`; ${name}=`)
		if (parts.length === 2) return parts.pop().split(';').shift()
	}

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
						res.json()
							console.log('Logged in!')
							.then(updateUser)
							// .then(updateUsername)
					} else {
						console.error('Please log in.')
					}
				})
			}
		})
	}, [])

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
		<AuthContext.Provider value={{ user, updateUser, logout }}>
			{children}
		</AuthContext.Provider>
	)
}

export default AuthProvider
