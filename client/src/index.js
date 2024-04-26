import React from 'react'
import { createRoot } from 'react-dom/client'
import { RouterProvider } from 'react-router-dom'
import AuthProvider from './context/AuthContext'
import router from './utils/routes'
import './styles.scss'

const rootElement = document.getElementById('root')
const root = createRoot(rootElement)

root.render(
    <AuthProvider>
        <RouterProvider router={ router } />
    </AuthProvider>
)