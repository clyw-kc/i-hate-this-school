from starlette.requests import Request
from starlette.responses import Response

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    request = Request(scope, receive)
    content = request.url
    response = Response(content, media_type='text/plain')
    await response(scope, receive, send)