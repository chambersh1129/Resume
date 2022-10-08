from django.utils.deprecation import MiddlewareMixin

from .models import AnonymousLogs


class LogAnonymousRequestsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # don't log anything related to admin or images
        ignore_paths = ["admin", ".jpg", ".ico"]

        # only log anonymous user to cut down on logs from myself when I'm logged in
        if not request.user.is_authenticated and not any(path for path in ignore_paths if path in request.path):
            try:
                log = AnonymousLogs(path=request.get_full_path(), user_agent=request.headers.get("User-Agent", ""))

            except Exception:
                log = AnonymousLogs(path="I BROKE")

            finally:
                log.save()
