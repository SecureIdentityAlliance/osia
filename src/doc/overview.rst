
System Overview
---------------

Components
""""""""""

The components are represented on the following diagram:

.. figure:: subsystems.*

    Components
    
The components are:

.. list-table::
    :header-rows: 1
    :widths: 30 30 30
    

    * - ID Ecosystem Component
      - Data
      - Functions
      
    * - Enrollment
      - - Alpha*
        - UIN*
        - History*
        - Supporting documents*
      - - Recording application
        - Collecting personal data 

    * - PR
      - - Alpha
        - UIN
        - History
        - Supporting documents
      - - Identity attributes storage
        - Identity Life cycle management
        
    * - UIN Gen
      - - Alpha
        - UIN
      - - UIN generation

    * - ABIS
      - - UIN
        - Biometric data (images and templates)
      - - Authentication (1:1)
        - Identification (1:N)
        - Quality control and adjudication

    * - CR
      - - Events
        - UIN
        - History
        - Supporting documents
      - - Events storage
        - Certificate production
        - Workflow

    * - ID Card
      - - Alpha
        - UIN
        - History
        - Supporting documents
      - - ID card data storage
        - ID card Life cycle management
        - ID Card Production
        - Workflow
        - SMS and email server

    * - Functional Registry
      - - Alpha
        - UIN
        - History
      - - [Card data storage]
        - Life cycle management
        - [Card production]
        - Workflow
        - SMS and email server

    * - Usage
      - ?
      - KYC/auth



Definitions
"""""""""""

.. glossary::

    **CR**
        Civil Registry. The system in charge of the continuous, permanent, compulsory and universal recording
        of the occurrence and characteristics of vital events pertaining to the population, as provided
        through decree or regulation in accordance with the legal requirements in each country.
        
    **Functional systems and registers**
        Managing data including voter rolls, land registry, vehicle registration, passport, residence registry,
        education, health and benefits.
    
    **PR**
        Population Registry. The system in charge of the recording of selected information pertaining to each member
        of the resident population of a country.

        
    **Mime Types**
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

    **HTTP Status Codes**
        The HTTP Status Codes are used to indicate the status of the executed operation. The available status codes are
        described by `RFC 7231 <http://tools.ietf.org/html/rfc7231#section-6>`_ and in the
        `IANA Status Code Registry <http://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml>`_.

    **UIN**
        Unique Identity Number.
    

