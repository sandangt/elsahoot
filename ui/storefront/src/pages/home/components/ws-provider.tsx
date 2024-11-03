import { useEffect, type FC, type ReactNode } from 'react'

type Props = {
  children: ReactNode
}

export const WebSocketProvider: FC<Props> = ({ children }) => {
  useEffect(() => {

  }, [])
  return <>{children}</>
}
