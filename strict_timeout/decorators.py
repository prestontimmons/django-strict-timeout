from datetime import datetime, timedelta

from django.conf import settings
from django.shortcuts import redirect


SESSION_KEY = "__strict_timeout_value"


def strict_timeout(function=None, login_url=settings.LOGIN_URL,
         timeout=1200, session_key=SESSION_KEY):
    """
    Decorator for views that have re-authentication timeouts that differ
    from the global session.

    Optional Arguments::

        ``login_url``
            The url to redirect to for login. The default value is
            settings.LOGIN_URL.

        ``timeout``
            The timeout before requiring re-authentication in seconds.
            The default value is 1200.

        ``session_key``
            The session key to use for storing the time of the user's
            last activity in restricted views.

    Example Usage::

        @strict_timeout
        def my_view(request):
            return HttpResponse("")

        @strict_timeout(login_url="/login/", timeout=600)
        def my_view(request):
            return HttpResponse("")
    """

    def _dec(view_func):
        def _view(request, *args, **kwargs):

            if not request.user.is_authenticated():
                return redirect("%s?next=%s" % (login_url,
                    request.get_full_path()))

            request_time = datetime.now()
            last_activity = max(request.session.get(session_key, request_time),
                request.user.last_login)

            if last_activity < request_time - timedelta(seconds=timeout):
                return redirect("%s?next=%s" % (login_url,
                    request.get_full_path()))

            request.session[session_key] = request_time

            return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)
