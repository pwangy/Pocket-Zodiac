import { useContext, useState } from 'react'
// import { useNavigate } from 'react-router-dom'
import * as Yup from 'yup'
import YupPassword from 'yup-password'
import { object, string } from 'yup'
import { Formik, Form, Field, useFormik } from 'formik'
import { AuthContext } from '../context/AuthContext'

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

	email: string().email().required("Email is required")
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
	email: ''
}

const Auth = () => {
	const { user, login } = useContext(AuthContext)
	const [isLogin, setIsLogin] = useState(true)
	// const navigate = useNavigate()

	const requestUrl = isLogin ? '/login' : '/signup'

	const handleIsLogin = () => {
		setIsLogin(!isLogin)
	}

	const formik = useFormik({
		initialValues,
		validationSchema: isLogin ? loginSchema : signupSchema,
		onSubmit: (formData) => {
			// debugger
			const updatedValues = Object.assign({}, formData, {
				password_hash: formData.password,
			})
			delete updatedValues.password;
			fetch(requestUrl, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(updatedValues)
			}).then((res) => {
				if (res.ok) {
					res.json()
						.then((userData) => {
							login(userData)
							console.log('logged in!')
						})
						// .then(() => {
						// 	// isLogin ? navigate('/home') : navigate('/')
						// })
				} else if (res.status === 422) {
					console.error('invalid login!')
					return res.json().then((errorObj) => console.log(errorObj))
				}
			})
		}
	})

	return (
		<section className='form'>
			<p>{isLogin ? 'Login' : 'Sign up'}</p>
			<Formik onSubmit={formik.handleSubmit}>
				<Form>
					<Field
						name='username'
						type='text'
						placeholder='Username'
						onChange={formik.handleChange}
						onBlur={formik.handleBlur}
						value={formik.values.username}
						autoComplete='username'
					/>
					{formik.errors.username && formik.touched.username && (
						<div className='error-message'>{formik.errors.username}</div>
					)}
					<Field
						name='password'
						type='password'
						placeholder='Password'
						onChange={formik.handleChange}
						onBlur={formik.handleBlur}
						value={formik.values.password}
						autoComplete='current-password'
					/>
					{formik.errors.password && formik.touched._password && (
						<div className='error-message'>{formik.errors.password}</div>
					)}
					{!isLogin && (
						<>
							<Field
								type='password'
								name='confirmPassword'
								placeholder='Confirm Password'
								onChange={formik.handleChange}
								onBlur={formik.handleBlur}
								value={formik.values.confirmPassword}
								autoComplete='confirm-new-password'
							/>
							{formik.errors.confirmPassword && formik.touched.confirmPassword && (
								<div className='error-message'>{formik.errors.confirmPassword}</div>
							)}
							<Field
								type='text'
								name='email'
								placeholder='email'
								onChange={formik.handleChange}
								onBlur={formik.handleBlur}
								value={formik.values.email}
								autoComplete='email'
							/>
							{formik.errors.email && formik.touched.email && (
								<div className='error-message'>{formik.errors.email}</div>
							)}
						</>
					)}
					<input type='submit' value={isLogin ? 'Login' : 'Sign up'} />
					{isLogin ? <button type='button' className='change-form' onClick={handleIsLogin}>Create New Account</button> : ''}
				</Form>
			</Formik>
		</section>
)}

export default Auth
