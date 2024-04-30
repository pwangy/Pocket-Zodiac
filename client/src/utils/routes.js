import { createBrowserRouter } from 'react-router-dom'
import App from '../components/App'
import Auth from '../components/Auth'
import Error from '../components/App'

const router = createBrowserRouter([
    {
        path: '/',
		element: <App />,
		errorElement: <Error />,
		children: [
			{
				path: '/',
				element: <Auth />,
				index: true
			},
			{
				path: '/auth',
				element: <Auth />
			},
			// {
			// 	path: '',
			// 	element: ''
			// },
    ]}
])

export default router