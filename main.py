import os
from pathlib import Path

# Django modules 
from django.core.wsgi import get_wsgi_application
from django.conf import settings
from fastapi import FastAPI

# INITIALIZE DJANGO APP HERE
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fastdj.settings')
django_app = get_wsgi_application()

# FastAPI modules
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html, get_swagger_ui_oauth2_redirect_html
from starlette.middleware.cors import CORSMiddleware


from restapi.core import conf, version
from restapi.api.v1.api import api_router


app = FastAPI(
    title=conf.PROJECT_TITLE,
    description=conf.PROJECT_DESC,
    version=version.VERSION,
    docs_url=None,
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)


app.include_router(api_router, prefix=conf.API_PREFIX)

# Self host swagger static files
base_dir = Path(__file__).resolve().parent
app.mount('/static', StaticFiles(directory=base_dir / 'static'), name='static')

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


app.mount('', WSGIMiddleware(django_app))

# app.mount('/static', StaticFiles(
#     directory=os.path.normpath(
#         os.path.join(find_spec('django.contrib.admin').origin, "..", "static")
#     )
# ), name='static')
