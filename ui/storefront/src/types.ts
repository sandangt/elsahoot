export interface Player {
  id: string
  username: string
  score: number
  riddlePassed: number
  createdAt: number
  modifiedAt: number
}

export interface Quiz {
  id: string
  topic: string
  totalScore: number
  createdAt: number
  modifiedAt: number
}

export interface PlayerExtended extends Player {
  quiz: Quiz
}
