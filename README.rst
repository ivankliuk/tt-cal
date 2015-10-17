Installation instruction
========================

The project works on Python 2.7 only.

Clone the project:

.. code :: bash

  git clone git@github.com:ivankliuk/tt-cal.git

Create Python ``virtualenv``:

.. code :: bash

  mkvirtualenv cal

Change current directory:

.. code :: bash

  cd tt-cal

Setup project:

.. code :: bash

  python setup.py develop

Run project on all available IP interfaces:

.. code :: bash

  pserve cal.ini

Open web application in browser by entering the following URL:

.. code :: bash

  http://<ip_address>:6543/

Where ``ip_address`` is an IP address of the host with the appllication
running.
