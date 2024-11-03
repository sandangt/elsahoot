import { useAuthStore } from '@/hooks/auth-store'
import { Typography } from '@mui/material'
import { HomeLayout } from './components/layout'
import { Navigate } from 'react-router-dom'

export const HomePage = () => {
  const isLoggedIn = useAuthStore((state) => state.isLoggedIn)
  const playerId = useAuthStore((state) => state.playerId)
  const quizId = useAuthStore((state) => state.quizId)
  return (
    <HomeLayout>
      {isLoggedIn() ? (
        <>
          <Typography variant="h1">Room: {quizId}</Typography>
          <Typography variant="h2">Your player id: {playerId} </Typography>
        </>
      ) : (
        <Navigate to="/hello" />
      )}
    </HomeLayout>
  )
}
