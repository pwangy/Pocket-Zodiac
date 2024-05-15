import React from 'react'
import { createRoot } from 'react-dom/client'
import { RouterProvider } from 'react-router-dom'
import { GoogleOAuthProvider } from '@react-oauth/google'
import AuthProvider from './context/AuthContext'
import ToastProvider from './context/ToastContext'
import router from './utils/routes'
import './styles.scss'

const rootElement = document.getElementById('root')
const root = createRoot(rootElement)

root.render(
    <ToastProvider>
        <GoogleOAuthProvider clientID='process.env.REACT_GOAUTH_CID'>
            <AuthProvider>
                <RouterProvider router={ router } />
            </AuthProvider>
        </GoogleOAuthProvider>
    </ToastProvider>
)