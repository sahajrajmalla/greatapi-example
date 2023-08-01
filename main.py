from __future__ import annotations

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from greatapi.config import GREATAPI_ADMIN_STATIC_PATH
from greatapi.db.database import engine
from greatapi.db import admin
from greatapi.admin.sites import admin_router
from greatapi.admin.sites import AdminSite
from greatapi.utils.cbv import _cbv
from greatapi.core import auth_router, user_router, test_auth_router, history_router
from myapp.router import meroapp_router

from myproject import REGISTERED_ADMINS

from greatapi.utils.urls import get_route_dict

from myapp.models import Base as MeroAppBase


app = FastAPI()

app.mount('/static', StaticFiles(directory=GREATAPI_ADMIN_STATIC_PATH), name='static')

admin.AdminBase.metadata.create_all(engine)
admin.UserBase.metadata.create_all(engine)
MeroAppBase.metadata.create_all(engine)

registered_admins = get_route_dict(REGISTERED_ADMINS)

admin_site = _cbv(admin_router, AdminSite, registered_admins)


app.include_router(admin_router)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(test_auth_router)
app.include_router(history_router)
app.include_router(meroapp_router)