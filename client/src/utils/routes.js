import { createBrowserRouter } from 'react-router-dom'
import App from '../App'
import Auth from '../components/Auth'
import Detail from '../components/Detail'
import Error from '../pages/Error'
import Explore from '../pages/Explore'
import Profile from '../pages//Profile'
import Zodiac from '../pages/Zodiac'

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
				element: <Zodiac />
			},
			{
				path: '/explore',
				element: <Explore />
			},
			{
				path: '/elements/:id',
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