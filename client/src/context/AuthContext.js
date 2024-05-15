import { createContext, useContext, useState, useEffect } from 'react'
import { toast } from 'react-toastify'
import ToastContext from './ToastContext'

export const AuthContext = createContext()

const AuthProvider = ({ children }) => {
	const [user, setUser] = useState(null)
	const updateUser = (user) => setUser(user)
	// const { showToast } = useContext(ToastContext)

	const getCookie = ( name ) => {
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
		.then(res => {
			if (res.ok) {
				res.json().then(updateUser)
			} else {
				fetch('/refresh', {
					method: 'POST',
					headers: {
						'X-CSRF-TOKEN': getCookie('csrf_refresh_token'),
					}
				})
				.then(res => {
					if (res.ok) {
						res.json()
							toast.success('Logged in!')
							.then(updateUser)
					} else {
						toast.info('Please log in.')
						// toasty.error(({ closeToast }) => 'Please log in.')
						// showToast('info', 'Please log in.')


					}
				})
			}
		})
	}, [])

	const patchUser = (patched_user) => setUser(patched_user)


	const deleteUser = (deleted_user) => setUser(null)

	const logout = (user) => {
		fetch('/logout', { method: 'DELETE' })
			.then((res) => {
				if (res.status === 204) {
					setUser(null)
					toast.success('Logged out!')
				}
			})
			.catch((err) => toast.error(err))
	}

	return (
		<AuthContext.Provider value={{ user, updateUser, logout, patchUser, deleteUser, getCookie }}>
			{children}
		</AuthContext.Provider>
	)
}

export default AuthProvider
