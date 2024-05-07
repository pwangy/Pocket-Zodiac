import { useState, useContext } from 'react'
import { Formik, Form, Field, ErrorMessage } from 'formik'
import * as Yup from 'yup'
import { AuthContext } from '../context/AuthContext'

const Profile = () => {
    const { user, patchUser, deleteUser } = useContext(AuthContext)
    const [editing, setEditing] = useState(false)

    const editMode = () => {
        setEditing(!editing)
    }

    // const handleDelete = () => {
    //     fetch(`/users/${user.id}`, {
    //         method: 'DELETE',
    //         headers: {'Content-Type': 'application/json'}
    //     })
    //     .then(res => {
    //         if (res.ok) {
    //             const update
    //         }
    //     })
    // }

    const profileSchema = Yup.object({
        email: Yup.string().email().required("Email is required"),
        birthdate: Yup.date().required('Date is required.')
    })

    const initialValues = {
        email: user?.email || '',
        birthdate: user?.birthdate || ''
    }

    return (
        <>
            {editing ? 
                <div className='edit'>
                <h3>Now editing</h3>
                <Formik
                    initialValues={initialValues}
                    validationSchema={profileSchema}
                    onSubmit={(formData, { setSubmitting }) => {
                        fetch(`/users/${user.id}`, {
                            method: 'PATCH',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify(formData)
                        })
                        .then(res => {
                            if (res.ok) {
                                return res.json()
                            } else {
                                throw new Error('Something went wrong while saving')
                            }
                        })
                        .then(userData => {
                            patchUser(userData)
                            console.log('Changes saved!')
                        })
                        .catch(error => {
                            console.error('Error:', error.message)
                        })
                        .finally(() => {
                            setSubmitting(false)
                        })
                    }}
                >
                {({ touched, errors, isSubmitting })  => (
                    <Form>
                        <Field 
                            name='email'
                            type='email'
                            autoComplete='email'
                        />
                        <ErrorMessage name='email' component='div' />
                        <Field 
                            name='birthdate'
                            type='date'
                        />
                        <ErrorMessage name='birthdate' component='div' />
                        <input type='submit' disabled={isSubmitting} value={'Save Changes'} />
                    </Form>
                )}
                </Formik>
            </div>
            : (
                <div className='view'>
                    <h3>Manage your details here</h3>
                    <p>{user.username}'s Profile</p>
                    <button onClick={editMode}>edit profile</button>
                    <p>id: {user.id}</p>
                    <p>email: {user.email}</p>
                    <p>birthdate: {user.birthdate}</p>
                    <button onClick={deleteUser}>delete profile</button>
                </div>
            )}
        </>
)}

export default Profile