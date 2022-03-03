
class TestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.users_id = None

        response = self.get_response(request)

        return response