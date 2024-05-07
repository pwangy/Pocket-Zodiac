import { useState, useContext } from 'react'
import { useNavigate } from 'react-router-dom'
import { Formik, Form, Field, ErrorMessage } from 'formik'
import * as Yup from 'yup'
import { AuthContext } from '../context/AuthContext'

const Profile = () => {
	const { user, patchUser, deleteUser } = useContext(AuthContext)
	const [editing, setEditing] = useState(false)
    const navigate = useNavigate()

	const editMode = () => {
		setEditing(!editing)
	}

	const handleDelete = () => {
		fetch(`/users/${user.id}`, {
			method: 'DELETE'
		})
			.then((res) => {
				if (res.status === 204) {
					deleteUser(user)
                    navigate('/')
				} else {
					return res.json().then((errorObj) => {
						console.error('Error deleting user:', errorObj)
					})
				}
			})
			.catch((err) => console.log(err))
	}

	const profileSchema = Yup.object({
		email: Yup.string().email().required("Email is required"),
		birthdate: Yup.date().required('Date is required.')
	})

	const initialValues = {
		email: user?.email || '',
		birthdate: user?.birthdate || ''
	}

    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
      }

	return (
		<>
			{editing ? (
				<div className='edit'>
					<h3>Now editing</h3>
					<Formik
						initialValues={initialValues}
						validationSchema={profileSchema}
						onSubmit={(formData, { setSubmitting }) => {
                            // const formatData = {
                            //     ...formData,
                            //     birthdate: new Date(formData.birthdate).toISOString().split('T')[0]
                            // }
							fetch(`/users/${user.id}`, {
								method: 'PATCH',
								headers: { 
                                    'Content-Type': 'application/json', 
                                    'X-CSRF-TOKEN': getCookie('csrf_access_token')
                                },
								body: JSON.stringify(formData)
							})
                            .then((res) => {
                                if (res.ok) {
                                    return res.json()
                                    .then((userData) => {
                                        patchUser(userData)
                                        console.log('Changes saved!')
                                        setEditing(false)
                                    })
                                } else if (res.status === 401) {
                                    fetch('/refresh', {
                                        method: 'POST',
                                        headers: {'X-CSRF-TOKEN': getCookie('csrf_refresh_token')}
                                    })
                                    .then (res => {
                                        if (res.ok) {
                                            fetch(`/users/${user.id}`, {
                                                method: 'PATCH',
                                                headers: { 
                                                    'Content-Type': 'application/json', 
                                                    'X-CSRF-TOKEN': getCookie('csrf_access_token')
                                                },
                                                body: JSON.stringify(formData)
                                            })
                                            .then((res) => {
                                                if (res.ok) {
                                                    return res.json().then((userData) => {
                                                        patchUser(userData)
                                                        console.log('Changes saved!')
                                                        setEditing(false)
                                                    })
                                                    // maybe build a check token route in be
                                                } else {
                                                    return res.json().then(errorObj => console.error(errorObj.message || errorObj.Error))
                                                }
                                                // note to make errors consistent; use message OR Error
                                            })
                                    // throw new Error('Something went wrong while saving')
                                        } else {
                                            throw new Error('Token Expired! Please login again.')
                                        }
                                    })
                                }
                            })
                            .catch((error) => {
                                console.error('Error:', error.message)
                            })
                            .finally(() => {
                                setSubmitting(false)
                            })
                        }}
                        >
						{({ touched, errors, isSubmitting }) => (
							<Form>
								<Field 
                                    name='email'
                                    type='email'
                                    autoComplete='email'
                                />
                                <ErrorMessage name='email' component='div' />
								<Field name='birthdate' type='date' />
								<ErrorMessage name='birthdate'component='div' />
								<input type='submit' disabled={isSubmitting} value={'Save Changes'} />
							</Form>
						)}
					</Formik>
				</div>
			) : (
				<div className='view'>
					<h3>Manage your details here</h3>
					<p>{user.username}'s Profile</p>
					<button onClick={editMode}>edit profile</button>
					<p>id: {user.id}</p>
					<p>email: {user.email}</p>
					<p>birthdate: {user.birthdate}</p>
					<button onClick={handleDelete}>delete profile</button>
				</div>
			)}
		</>
	)
} // add csrf token to every fetch call. fix login_req > jwt req. change birthdate to string in be


export default Profile
