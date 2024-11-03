import { type FC, type ReactNode } from 'react'

type Props = {
  children: ReactNode
}

export const HomeLayout: FC<Props> = ({ children }) => <>{children}</>
