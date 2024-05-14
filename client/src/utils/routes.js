import { createBrowserRouter } from 'react-router-dom'
import App from '../App'
import Auth from '../components/Auth'
import Error from '../pages/Error'
import PersonalZodiac from '../pages/PersonalZodiac'
import Explore from '../pages/Explore'
import Detail from '../components/Detail'
import Profile from '../pages//Profile'

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
				path: '/east/:id',
				element: <Detail />
			},
			{
				path: '/west/:id',
				element: <Detail />
			},
			{
				path: '/edit/:id',
				element: <Profile />
			}
    ]}
])

export default router

// /user-info
// no page refreshes