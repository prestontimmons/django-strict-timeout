Strict Timeout
==============

Allows an inactivity timeout differing from the global session to be set
on a view, after which re-authentication is required, even if a user is
still logged in.

This is provided as a view decorator. The last activity in a restricted
view is tracked through the user's session.

Example Usage::

    @strict_timeout
    def my_view(request):
        return HttpResponse("")

    @strict_timeout(login_url="/login/", timeout=600)
    def my_view(request):
        return HttpResponse("")

    @strict_timeout(timeout=600, session_key="__custom_timeout_key")
    def my_view(request):
        return HttpResponse("")
