import { createBrowserRouter } from 'react-router-dom'
import App from '../App'
import Auth from '../components/Auth'
import Error from '../App'
import PersonalZodiac from '../pages/PersonalZodiac'
import Explore from '../pages/Explore'
import SingleEle from '../components/elements/Detail'
import WestSign from '../components/west/Detail'
import EastSign from '../components/east/Detail'
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
				element: <SingleEle />
			},
			{
				path: '/east/:id',
				element: <EastSign />
			},
			{
				path: '/west/:id',
				element: <WestSign />
			},
			{
				path: '/profile/:id',
				element: <Profile />
			},
			// {
			// 	path: '/profile',
			// 	element: <Profile />
			// },
    ]}
])

export default router

// /user-info
// no page refreshes