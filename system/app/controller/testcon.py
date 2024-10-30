import json
from datetime import datetime

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.controller.dependency import WSHandlerDep

router = APIRouter()

@router.websocket('/ws/{player_id}')
async def test_websocket(player_id: str, websocket: WebSocket, ws_handler: WSHandlerDep):
    await ws_handler.connect(websocket)
    now = datetime.now()
    current_time = now.strftime('%H:%M')
    try:
        while True:
            data = await websocket.receive_text()
            message = {'time': current_time, 'playerId': player_id, 'message': data}
            await ws_handler.broadcast(json.dumps(message))
    except WebSocketDisconnect as ex:
        ws_handler.disconnect(websocket)
        message = {"time":current_time,"playerId": player_id,"message":"Offline"}
        await ws_handler.broadcast(json.dumps(message))
