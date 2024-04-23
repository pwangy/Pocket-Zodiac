import { createRoot } from 'react-dom/client'
import { RouterProvider } from 'react-router-dom'
import router from './utils/routes'
import './styles.scss'

const container = document.getElementById('root')
const root = createRoot(container)

root.render(<RouterProvider router={ router } />)
