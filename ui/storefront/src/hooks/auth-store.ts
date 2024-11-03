import { create } from 'zustand'

type State = {
  quizId: string | null
  playerId: string | null
  username: string | null
}

type Action = {
  storePlayerId: (playerId: State['playerId']) => void
  storeUsername: (username: State['username']) => void
  storeQuizId: (quizId: State['quizId']) => void
  isLoggedIn: () => boolean
}

export const useAuthStore = create<State & Action>((set, get) => ({
  playerId: null,
  username: null,
  quizId: null,
  storePlayerId: (playerId) => set(() => ({ playerId })),
  storeUsername: (username) => set(() => ({ username })),
  storeQuizId: (quizId) => set(() => ({ quizId})),
  isLoggedIn: () => !!get().quizId && !!get().playerId
}))
