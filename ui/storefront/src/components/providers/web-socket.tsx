import { useEffect, type FC, type ReactNode } from 'react'

import { WS_URL } from '@/settings'

type Props = {
  children: ReactNode
}

export const SocketProvider: FC<Props> = ({ children }) => {
  useEffect(() => {
    const url = WS_URL['test']
    const ws = new WebSocket(url)
    ws.onopen = () => {
      ws.send('CONNECT')
    }
    return () => ws.close()
  })
  return <>{children}</>
}
