import { LoginFailedException } from '@/exceptions'
import { type PlayerExtended } from '@/types'

type LoginRequestParams = {
  quizId: string
  username: string
}

type LoginRequestResult = PlayerExtended

export const loginRequest = async ({ quizId, username }: LoginRequestParams): Promise<LoginRequestResult> => {
  const resp = await fetch('http://localhost:38000/console/hello', {
    headers: {
      'Content-Type': 'application/json',
    },
    method: 'POST',
    body: JSON.stringify({ quizId, username }),
  })
  if (!resp.ok) {
    throw LoginFailedException.default()
  }
  return await resp.json()
}
