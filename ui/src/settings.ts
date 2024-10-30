export const SYSTEM_PORT = import.meta.env.VITE_SYSTEM_PORT
export const SYSTEM_HOST = import.meta.env.VITE_SYSTEM_HOST
export const WS_URL = {
  'test': `ws://${SYSTEM_HOST}:${SYSTEM_PORT}/test/ws`
}
