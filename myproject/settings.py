from __future__ import annotations

from greatapi.db.admin.user import User
from greatapi.db.admin.default import History
from myapp.models import Blog

REGISTERED_ADMINS = [
    User,
    History,
    Blog,
]