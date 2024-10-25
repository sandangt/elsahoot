import { Box, CssBaseline, ThemeProvider } from '@mui/material'
import { StrictMode, type FC, type ReactNode } from 'react'
import { elseHootTheme } from './components/themes'

export const App = () => (
  <AppProvider>
    <Box>Hello World</Box>
  </AppProvider>
)

type AppProviderProps = {
  children: ReactNode
}

const AppProvider: FC<AppProviderProps> = ({ children }) => (
  <StrictMode>
    <ThemeProvider theme={elseHootTheme}>
      <CssBaseline />
      {children}
    </ThemeProvider>
  </StrictMode>
)
