Strict Timeout
==============

Allows an inactivity timeout differing from the global session to be set
on a view, after which re-authentication is required, even if a user is
still logged in.

This is provided as a view decorator. The last activity in a restricted
view is tracked through the user's session.


Example Usage
-------------

Setting the timeout for a view to the default of 20 minutes::

    @strict_timeout
    def my_view(request):
        return HttpResponse("")

Specifying a custom login url to redirect to and a custom timeout::

    @strict_timeout(login_url="/login/", timeout=600)
    def my_view(request):
        return HttpResponse("")

Specifying a custom timeout and a custom session key to track last activity::

    @strict_timeout(timeout=600, session_key="__custom_timeout_key")
    def my_view(request):
        return HttpResponse("")


Installation
------------

This can be installed from source with pip using this command::

    pip install -e git+git://github.com/prestontimmons/django-strict-timeout.git#egg=StrictTimeout
