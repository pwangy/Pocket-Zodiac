import { createContext, useState } from 'react'

export const AuthContext = createContext()

const AuthProvider = ({ children }) => {
	const [user, setUser] = useState(null)

	const login = (user) => {
		setUser(user)
		console.log('user logged in!')
	}

	const logout = (user) => {
		setUser(null)
		console.log('user logged out!')
	}

	return (
		<AuthContext.Provider value={{ user, login, logout }}>
			{ children }
		</AuthContext.Provider>
)}

export default AuthProvider
