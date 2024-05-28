from rest_framework.response import Response

class CustomResponse:
    def __init__(self):
        self.status = 200
        self.data = None
        self.message = None
        self.errors = None

    def success_response(self, status, data, message):
        self.status = status
        self.data = data
        self.message = message
        return Response({"success": True, "message": message, "data": data}, status=status)

    def error_response(self, status, message, errors):
        self.status = status
        self.errors = errors
        self.message = message
        return Response({"success": False, "message": message, "errors": errors}, status=status)
