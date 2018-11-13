
Open Source API Specification
=============================

**Version 1.0a0**

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and
"OPTIONAL" in this document are to be interpreted as described in `RFC 2119 <http://www.ietf.org/rfc/rfc2119.txt>`_.

This specification is licensed under `The MIT License <https://opensource.org/licenses/MIT>`_.

Introduction
------------

:todo:`To be completed`

Revision History
----------------

.. list-table::
   :header-rows: 1

   * - Version
     - Date
     - Notes
   * - 1.0
     - 2018-12-xx
     - Release of version 1.0
   * - 1.0a0
     - 2018-07-31
     - First alpha version


Definitions
-----------

.. glossary::

    CR
        Civil Registry. The system in charge of the continuous, permanent, compulsory and universal recording
        of the occurrence and characteristics of vital events pertaining to the population, as provided
        through decree or regulation in accordance with the legal requirements in each country.
        
    CI
        Civil Identity. The system in charge of the recording of selected information pertaining to each member
        of the resident population of a country. :todo:`To be completed`

        
    Mime Types
        Mime type definitions are spread across several resources. The mime type definitions should be in compliance with
        `RFC 6838 <http://tools.ietf.org/html/rfc6838>`_.

        Some examples of possible mime type definitions:

        .. code-block:: guess

            text/plain; charset=utf-8
            application/json
            application/vnd.github+json
            application/vnd.github.v3+json
            application/vnd.github.v3.raw+json
            application/vnd.github.v3.text+json
            application/vnd.github.v3.html+json
            application/vnd.github.v3.full+json
            application/vnd.github.v3.diff
            application/vnd.github.v3.patch

    HTTP Status Codes
        The HTTP Status Codes are used to indicate the status of the executed operation. The available status codes are
        described by `RFC 7231 <http://tools.ietf.org/html/rfc7231#section-6>`_ and in the
        `IANA Status Code Registry <http://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml>`_.

    UIN
        Unique Identity Number.
    
:todo:`To be completed`

.. toctree::
    :maxdepth: 3

    functional-specifications
    technical-specifications

