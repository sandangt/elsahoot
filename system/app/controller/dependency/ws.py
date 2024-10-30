from app.resource.wshandler import WSHandler, ws_handler


async def get_ws_handler() -> WSHandler:
    return ws_handler
