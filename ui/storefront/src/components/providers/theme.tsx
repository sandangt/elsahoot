import { CssBaseline, ThemeProvider } from '@mui/material'
import { type FC, type ReactNode } from 'react'
import { elseHootTheme } from '@/components//themes'

type Props = {
  children: ReactNode
}

export const ElseHootThemeProvider: FC<Props> = ({ children }) => (
  <ThemeProvider theme={elseHootTheme}>
    <CssBaseline />
    {children}
  </ThemeProvider>
)
