import { StrictMode, type FC, type ReactNode } from 'react'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'

import { ElseHootThemeProvider, RestQuery } from './components/providers'
import HomePage from './pages/home'
import PlayPage from './pages/play'
import HelloPage from './pages/hello'

//#region Main app
const ROUTES = createBrowserRouter([
  {
    path: '/hello',
    element: <HelloPage />
  },
  {
    path: '/',
    element: <HomePage />,
  },
  {
    path: '/play',
    element: <PlayPage />,
  },
])

export const App = () => {
  return (
    <AppProvider>
      <RouterProvider router={ROUTES} />
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
    <RestQuery>
      <ElseHootThemeProvider>{children}</ElseHootThemeProvider>
    </RestQuery>
  </StrictMode>
)
//#endregion
