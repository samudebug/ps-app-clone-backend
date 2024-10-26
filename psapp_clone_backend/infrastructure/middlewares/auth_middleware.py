from typing import Awaitable, Callable
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response

from psapp_clone_backend.adapters.clients.psn_awp_client import PSNAPIClient
class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
        headers = request.headers
        token = headers.get("Authorization")
        if token is None and request.url == '/docs':
            return JSONResponse({"error": "Unauthorized"}, status_code=401)
        request.state.context_data = {"sso_code": token}
        return await call_next(request)