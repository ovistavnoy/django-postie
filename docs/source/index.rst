Welcome to Django Postie documentation!
=======================================

Application to send emails and managing mailing through admin.

Fully support and tested on django >= 2.0 and python >= 3.7

Why this project
----------------

I've tried other projects but all of them didn't satisfy all of my needs in one, such as:

* Editing email templates in the admin panel with code editor (WYSIWYG often mess with template tags).
* Translated templates.
* Celery backend with no extra actions on configuring (such as cron, management commands etc).
* Error logging.
* Management command to create missing templates.
* List of available variables inside template editing form.

This project requires:

    * `django-parler <https://github.com/django-parler/django-parler>`_
    * `django-codemirror2 <https://github.com/sk1p/django-codemirror2>`_
    * `django-ckeditor <https://github.com/django-ckeditor/django-ckeditor>`_

Also you also may investigate such great projects as:

    * `django-des <https://github.com/jamiecounsell/django-des>`_
    * `django-mailbox <https://github.com/coddingtonbear/django-mailbox>`_

Installation
------------

Installing from pypi. ::

    pip install django-postie

Add application and its required packages to your INSTALLED_APPS.

Run migrations.

.. code:: python

    INSTALLED_APPS = [
        ...
        'postie',
        'parler',
        'codemirror2',
        'ckeditor',
        ...
    ]


Usage
-----

For more details check the correspoding documentation.


.. code:: python

   # your_module.py

   from postie.shortcuts import send_mail

   file_content = open('path-to-the-file')

   send_mail(
       event='MAIL_EVENT',
       recipients=['email@email.com', 'email1@email1.com'],
       context={
           'var1': 'variable context',
           'var2': 'another value'
       },
       from_email='noreply@email.com',
       attachments=[{
           'file_name': file_content
       }],
       language='en'
   )
   # Also you can pass backend class directly to send method

   file_content.close()


Advanced usage
--------------

.. code:: python

   # your_module.py

   from postie.entities import Template

   file_content = open('path-to-the-file')
   another_file_content = open('path-to-the-another-file')

   template = Template.from_event('MAIL_EVENT')
   letter = template.new_letter(
      event='MAIL_EVENT',
      recipients=['email@email.com', 'email1@email1.com'],
      context={
          'var1': 'variable context',
          'var2': 'another value'
      },
      from_email='noreply@email.com',
      attachments=[{
          'file_name': file_content
      }],
      language='en'
   )

   # You can add attachment directly to the letter like this
   letter.add_attachment('file_name', another_file_content)

   # Sending letter
   # Also you can pass backend class directly to send method
   letter.send()

   file_content.close()
   another_file_content.close()


Current state
-------------

This package is already used on multiple projects and is fully tested, but API in future releases may change as package is under development to support new features and new releases of django.

If you have any troubles with package feel free to submit an issue or even better - create pull request

Contents
--------


.. toctree::
    :maxdepth: 2

    changelog

    shortcuts
    entities
    forms
    backends
    utils
    tilda
