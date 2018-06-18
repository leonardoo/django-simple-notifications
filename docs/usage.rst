=====
Usage
=====

To use django-notifications in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_notifications.apps.DjNotificationsConfig',
        ...
    )

Add django-notifications's URL patterns:

.. code-block:: python

    from dj_notifications import urls as dj_notifications_urls


    urlpatterns = [
        ...
        url(r'^', include(dj_notifications_urls)),
        ...
    ]
