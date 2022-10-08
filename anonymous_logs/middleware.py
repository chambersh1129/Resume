from django.utils.deprecation import MiddlewareMixin

from .models import AnonymousLogs


class LogAnonymousRequestsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        path = request.get_full_path()

        # don't log anything related to admin or images
        ignore_paths = ["admin", ".jpg", ".ico"]
        if any(ignore for ignore in ignore_paths if ignore in path):
            return

        # ignore authenticated users (aka, me)
        if request.user.is_authenticated:
            return

        user_agent = request.headers.get("User-Agent", "")

        # ignore UptimeRobot health checks
        ignore_agents = ["uptimerobot"]
        if any(ignore for ignore in ignore_agents if ignore in user_agent):
            return

        try:
            log = AnonymousLogs(path=path, user_agent=user_agent)

        except Exception:
            log = AnonymousLogs(path="I BROKE", user_agent="BEATS ME")

        finally:
            log.save()
