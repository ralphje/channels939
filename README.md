Proof of concept for django-channels issue 939
==============================================

This package is a simple example for the issue described in issue #939 of http://github.com/django/channels.

The issue describes a bug that seems to randomly stop consumers receiving messages over channel layers if multiple
workers are present.

Steps to reproduce:

* Start two runservers:

```
manage.py runserver 8000
manage.py runserver 8001
```

* Start the producer:

```
manage.py generatestuff
```

* Open four browser tabs, two to 8000 and two to 8001.

Now, I have not been able to reproduce this issue very reliably. I have had success with letting it run for a while,
and repeatedly refreshing one of the tabs at some point. I have had let it come to a complete halt in both servers, to
the point that letting it run off a single runserver also grinds to a halt.

You may notice that I have left in a group add to ``stuff3`` but it is never removed. After introducing this
error, the problem occurred more often, but it also occurs if stuff3 is never added to.

The issue is more reproducible after lots of stuff was generated.
