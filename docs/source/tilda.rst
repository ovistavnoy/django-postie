Tilda templates
===============

With 0.8 release tilda templates are now supported. To enable this feature you have to add a corresponding package to installed apps

.. code:: python

    INSTALLED_APPS += [
        ...
        'postie.integrations.tilda',
        ...
    ]


And run migrations


.. code:: python

    $ python manage.py migrate


Add urls to receive updates from tilda hooks. Relative url path is `tilda/webhook`, you should use it to fill corresponding settings in your tilda.cc dashboard.

.. code:: python

    urlpatterns += [
        path('', include('postie.integrations.tilda.urls'))
    ]


Now you have to fill settings in admin. You have to enter to public key, private key and project id(All templates you want to use must be from that project).
New field `tilda_id` in your `MailTemplate` admin page is a corresponding page id from tilda.cc, we use it to get a data from webhook.

NOTE: page html is only retrieved from webhook.


Template selection prority
--------------------------

1. Template for current activated language has a filled `tilda_id` then will use `tilda_html` with the same language.
2. Template for current activated language has a filled `tilda_id` but `tilda_html` is blank then will try to use `html`.
3. Template for current activated language has a blank `tilda_id` then will try to use `html` (old mechanic)
