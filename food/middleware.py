import logging

logger = logging.getLogger('recipe management')
handler = logging.FileHandler("log.log")
formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s ::: %(message)s")
handler.formatter = formatter
logger.addHandler(handler)
logger.setLevel(logging.INFO)


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_data = {'user': request.user.username, 'method': request.method, 'path': request.path}

        logger.info(request_data)
        response = self.get_response(request)
        response_data = {'status_code': response.status_code}
        logger.info(response_data)

        return response

