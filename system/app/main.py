from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controller import router
from app.exception.adviser import exception_map
from app.init import init_app
from app.settings import CORS_ALLOWED_ORIGINS, CORS_ALLOWED_METHODS
from app.settings import APP_TITLE, APP_SWAGGER_URL, APP_REDOC_URL, APP_METADATA, APP_VERSION

app = FastAPI(title=APP_TITLE,
              docs_url=APP_SWAGGER_URL,
              redoc_url=APP_REDOC_URL,
              openapi_tags=APP_METADATA,
              version=APP_VERSION,
              lifespan=init_app)
app.include_router(router, prefix='/console')
for exc_tuple in exception_map:
    app.add_exception_handler(*exc_tuple)
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOWED_ORIGINS,
    allow_methods=CORS_ALLOWED_METHODS
)
