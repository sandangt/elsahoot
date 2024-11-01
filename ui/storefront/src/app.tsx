import { CssBaseline, ThemeProvider } from '@mui/material'
import { StrictMode, type FC, type ReactNode } from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { combineReducers, configureStore } from '@reduxjs/toolkit'
import { Provider as ReduxProvider } from 'react-redux'

import { elseHootTheme } from './components/themes'
import { HomePage } from './pages/home'

//#region Main app
const ROUTES = [
  {
    name: 'Front',
    key: 'front',
    route: '/',
    component: <HomePage />,
  },
]

const ROUTE_COMPONENTS = ROUTES.map((route) => {
  if (route.route) {
    return <Route path={route.route} element={route.component} key={route.key} />
  }
  return null
})

export const App = () => {
  return (
    <AppProvider>
      <BrowserRouter>
        <Routes>{ROUTE_COMPONENTS}</Routes>
      </BrowserRouter>
    </AppProvider>
  )
}
//#endregion

//#region App provider
type AppProviderProps = {
  children: ReactNode
}

const AppProvider: FC<AppProviderProps> = ({ children }) => (
  <StrictMode>
    <ReduxProvider store={stateStore}>
      <ThemeProvider theme={elseHootTheme}>
        <CssBaseline />
        {children}
      </ThemeProvider>
    </ReduxProvider>
  </StrictMode>
)
//#endregion

//#region Redux state store
const clientStateReducers = {}
const apiReducers = {}

const stateStore = configureStore({
  reducer: combineReducers({
    ...clientStateReducers,
    ...apiReducers,
  }),
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(),
  devTools: true,
})
//#endregion
