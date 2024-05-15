import { createContext, useContext, useState, useRef, useCallback } from 'react'
import { ToastContainer, toast, Bounce, toastId } from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'

export const ToastContext = createContext()

export const useToast = () => useContext(ToastContext)

const ToastProvider = ({ children }) => {
    const [t, setT] = useState({ type: '', message: null })

    const options = {
        position: "top-left",
        autoClose: 5000,
        hideProgressBar: true,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
        transition: Bounce,
        role: 'alert',
        isLoading: false, 
        data: null,
        icon: false,
    }

    // shortcuts to types
    // toast.success('Success', options)
    // toast.info('Info', options)
    // toast.warn('Warn', options)
    // toast.error('Error', options)

    const showToast = useCallback((type, message) => {
        setT({ type, message })
    })

    // const ToastInfo = ( t ) => {
    //     type: INFO
    //     toast.success( t, {
    //         type: toast.TYPE.INFO,
    //         data: {text: {t}}
    //     }, options)}
    //     return (<div></div>)

    // const ToastSuccess = ( t ) => {
    //     toast.success( t, {
    //         type: toast.TYPE.SUCCESS,
    //         data: {text: {t}}
    //     }, options)}

    // const ToastError = ( t ) => {
    //     toast.error( t, {
    //         type: toast.TYPE.ERROR,
    //         data: {text: {t}}
    //     }, options)}


    // const ToastLoading = ( t ) => {
    //     toast.loading( t, {
    //         type: toast.TYPE.LOADING,
    //         data: {text: {t}}
    //     }, options)}

    return(
        <ToastContext.Provider value={{ showToast }}>
            {children}
        </ToastContext.Provider>
    )
}

export default ToastProvider





