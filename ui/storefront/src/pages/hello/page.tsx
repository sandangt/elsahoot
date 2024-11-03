import { useAuthStore } from '@/hooks/auth-store'
import { loginRequest } from '@/repositories'
import type { PlayerExtended } from '@/types'
import { Box, Button, Card, CardContent, TextField, Typography } from '@mui/material'
import { useMutation } from '@tanstack/react-query'
import { useForm } from 'react-hook-form'
import { useNavigate } from 'react-router-dom'

type FormData = {
  quizId: string
  username: string
}

export const HelloPage = () => {
  const { register, handleSubmit } = useForm<FormData>()
  const { storePlayerId, storeQuizId, storeUsername } = useAuthStore((state) => state)
  const navigate = useNavigate()
  const mutation = useMutation({
    mutationFn: loginRequest,
    onSuccess: ({ id, username, quiz }: PlayerExtended) => {
      storePlayerId(id)
      storeUsername(username)
      storeQuizId(quiz.id)
      navigate('/')
    },
  })
  return (
    <Box
      sx={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        height: '100vh',
        backgroundColor: '#f0f2f5',
      }}
    >
      <Card sx={{ maxWidth: 400, width: '100%', padding: 2 }}>
        <CardContent>
          <Typography variant="h5" align="center" gutterBottom>
            Quiz Login
          </Typography>
          <form noValidate autoComplete="off" onSubmit={handleSubmit((data: FormData) => mutation.mutate(data))}>
            <TextField label="Quiz ID" variant="outlined" fullWidth margin="normal" {...register('quizId')} />
            <TextField label="Player Username" variant="outlined" fullWidth margin="normal" {...register('username')} />
            <Button type="submit" variant="contained" color="primary" fullWidth sx={{ marginTop: 2 }}>
              Login
            </Button>
          </form>
        </CardContent>
      </Card>
    </Box>
  )
}
