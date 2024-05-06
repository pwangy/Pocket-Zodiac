import { createBrowserRouter } from 'react-router-dom'
import App from '../App'
import Auth from '../components/Auth'
import Error from '../App'
import PersonalZodiac from '../pages/PersonalZodiac'
import Explore from '../pages/Explore'
import Detail from '../components/elements/Detail'

// view & edit info

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
			{
				path: '/zodiac',
				element: <PersonalZodiac />
			},
			{
				path: '/explore',
				element: <Explore />
			},
			{
				path: '/element/:id',
				element: <Detail />
			},
			{
				path: '/profile',
				element: ''
			},
    ]}
])

export default router

// /profile
// /auth
// /explore
// /user-info
// no page refreshes