Simple scraping web pages
=========================

This is a alpha version - at the moment is scraping only
**status\_code**. It is necessary to check the page status code.

How to use
~~~~~~~~~~

Scan one page and get result

.. code:: python

    from scanpages.scanpage import Scanpage

    scan = Scanpage()
    scan.set_page('https://example.com')

    res = scan.scan()

    print(res)

The list of data from json file

.. code:: python

    import os
    from scanpages.scanpage import Scanpage

    scan = Scanpage()

    res = scan.scan_from_file(os.path.abspath("import/source.json"))
    print(res)

Import data from file and results export into .txt file

.. code:: python

    import os
    from scanpages.scanpage import Scanpage

    scan = Scanpage()

    scan.set_filepath(os.path.abspath("import/source.json"))

    print(scan.scan_import('export.txt'))

