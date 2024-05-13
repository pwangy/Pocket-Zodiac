import { useContext, useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import * as Yup from 'yup'
import YupPassword from 'yup-password'
import { object, string } from 'yup'
import { Formik, Form, Field, ErrorMessage } from 'formik'
import { AuthContext } from '../context/AuthContext'
// import OAuth from './auth/OAuth'

YupPassword(Yup)

const signupSchema = object({
	username: string()
		.min(2, 'Username must be at least 2 characters.')
		.max(20, 'Username cannot be longer than 20 characters.')
		.required('Required'),

	password: string()
		.min(8, 'Passwords must be at least 8 characters long.')
		.matches(/[a-zA-Z0-9]/, 'Password should contain letters and numbers.')
		.minLowercase(1, 'Password must contain at least 1 lowercase letter.')
		.minUppercase(1, 'Password must contain at least 1 uppercase letter.')
		.minNumbers(1, 'Password must contain at least 1 number.')
		.minSymbols(1, 'Password must contain at least 1 special character.')
		.required('Password is required.'),

	confirmPassword: string()
		.oneOf([Yup.ref('password'), null], 'Passwords must match.')
		.required('Confirm Password is required.'),

	email: string().email().required("Email is required"),
	birthdate: Yup.string().required('Date is required.')
})

const loginSchema = object({
	username: string().required('Username is required.'),
	password: string().required('A password is required to login.')
})

// Initial values
const initialValues = {
	username: '',
	password: '',
	confirmPassword: '',
	email: '',
	birthdate: ''
}

const Auth = () => {
	const { user, updateUser } = useContext(AuthContext)
	const [isLogin, setIsLogin] = useState(true)
	const clientId = process.env.REACT_APP_GOOGLE_CLIENT_ID
	const navigate = useNavigate()
	const requestUrl = isLogin ? '/login' : '/signup'

	const handleIsLogin = () => {
		setIsLogin(!isLogin)
	}

	//? OAuth
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
		<article className='form'>
			<p>{isLogin ? 'Login' : 'Sign up'}</p>
			<Formik 
				initialValues={initialValues}
				validationSchema = {isLogin ? loginSchema : signupSchema}
				onSubmit={(formData) => {
					const updatedValues = Object.assign({}, formData, {
						password_hash: formData.password
					})
					delete updatedValues.password;
					delete updatedValues.confirmPassword;
					fetch(requestUrl, {
						method: 'POST',
						headers: {
							'Content-Type': 'application/json'
						},
						body: JSON.stringify(updatedValues)
					}).then(res => {
						if (res.ok) {
							return res.json()
							.then(userData => {
								updateUser(userData)
								console.log('logged in!')
							})
						} else if (res.status === 422) {
							console.error('invalid login!')
							return res.json().then(errorObj => console.log(errorObj))
						}
					})
				}}
			> 
			{({ handleSubmit, touched, errors }) => (
				<>
					<Form onSubmit={handleSubmit}>
						<Field
							name='username'
							type='text'
							placeholder='Username'
							autoComplete='username'
						/>
						<ErrorMessage name='username' component='div' />
						<Field
							name='password'
							type='password'
							placeholder='Password'
							autoComplete='current-password'
						/>
						<ErrorMessage name='password' component='div' />
						{!isLogin && (
							<>
								<Field
									type='password'
									name='confirmPassword'
									placeholder='Confirm Password'
									autoComplete='confirm-new-password'
								/>
								<ErrorMessage name='confirmPassword' component='div' />
								<Field
									type='text'
									name='email'
									placeholder='email'
									autoComplete='email'
								/>
								<ErrorMessage name='email' component='div' />
								<Field name='birthdate' type='date' />
								<ErrorMessage name='birthdate'component='div' />
							</>
						)}
						<input type='submit' value={isLogin ? 'Login' : 'Sign up'} />
					</Form>
					{isLogin ? <button type='button' className='change-form' onClick={handleIsLogin}>Create New Account</button> : ''}
			</>
			)}
			</Formik>
			<div id='signInDiv' />
		</article>
)}

export default Auth
