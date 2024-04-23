import { createBrowserRouter } from 'react-router-dom'
import App from '../components/App'
// import Error from '../components/App'

const router = createBrowserRouter([
    {
        path: '/',
		element: <App />,
		// errorElement: <Error />,
		children: [
			{
				path: '/',
				element: <App />,
				index: true
			},
			{
				path: '',
				element: ''
			},
    ]}
])

export default router