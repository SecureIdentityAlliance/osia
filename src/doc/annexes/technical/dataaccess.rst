
.. _annex-interface-dataaccess:

Data Access
-----------

Download the OpenAPI file for this interface :openapi:`dataaccess.yaml`.

Services
""""""""

.. http:get:: /v1/persons
    :synopsis: null

    Retrieve a UIN based on a set of attributes.
    This service is used when the UIN is unknown.

    :query object attributes:
        The attributes used to retrieve the UIN
        (Required)
    :status 200:
        All UIN found (a list of at least one UIN)
    :status 400:
        Invalid parameter
    :status 401:
        Client must be authenticated
    :status 403:
        Service forbidden
    :status 404:
        No UIN found
    :status 500:
        Unexpected error (See :ref:`error`)

    **Example request:**

    .. sourcecode:: http

        GET /v1/persons?firstName=John&lastName=Do HTTP/1.1
        Host: example.com



    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            "1235567890"
        ]


    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 500 Internal Server Error
        Content-Type: application/json

        {
            "code": 1,
            "message": "string"
        }

.. http:get:: /v1/persons/{uin}
    :synopsis: null

    Retrieve attributes for a person.

    :param string uin:
        Unique Identity Number
    :query array attributeNames:
        The names of the attributes requested for this person
        (Required)
    :status 200:
        Requested attributes values or :ref:`error` description.
    :status 401:
        Client must be authenticated
    :status 403:
        Service forbidden
    :status 404:
        Unknown uin
    :status 500:
        Unexpected error (See :ref:`error`)

    **Example request:**

    .. sourcecode:: http

        GET /v1/persons/{uin}?attributeNames=firstName&attributeNames=lastName&attributeNames=dob HTTP/1.1
        Host: example.com



    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "firstName": "John",
            "lastName": "Doo",
            "dob": {
                "code": 1023,
                "message": "Unknown attribute name"
            }
        }


    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 500 Internal Server Error
        Content-Type: application/json

        {
            "code": 1,
            "message": "string"
        }


.. http:post:: /v1/persons/{uin}/match
    :synopsis: null

    Match person attributes.
    This service is used to check the value of attributes without exposing private data.
    
    The request body should contain a list of attributes and their value, formatted as a json dictionary.

    :param string uin:
        Unique Identity Number
    :status 200:
        Information about non matching attributes. Returns a list of matching result (See :ref:`matching-error`)
        An empty list indicates all attributes were matching.
    :status 401:
        Client must be authenticated
    :status 403:
        Service forbidden
    :status 404:
        Unknown uin
    :status 500:
        Unexpected error (See :ref:`error`)

    **Example request:**

    .. sourcecode:: http

        POST /v1/persons/{uin}/match HTTP/1.1
        Host: example.com
        Content-Type: application/json

        {
            "firstName": "John",
            "lastName": "Doo",
            "dateOfBirth": "1984-11-19"
        }


    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "attributeName": "firstName",
                "errorCode": 1
            }
        ]


    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 500 Internal Server Error
        Content-Type: application/json

        {
            "code": 1,
            "message": "string"
        }


.. http:post:: /v1/persons/{uin}/verify
    :synopsis: null

    Evaluate expressions (See :ref:`expression`) on person attributes.
    This service is used to evaluate simple expressions on
    person's attributes without exposing private data
    
    The request body should contain a list of :ref:`expression`.

    :param string uin:
        Unique Identity Number
    :status 200:
        The expressions are all true (true is returned) or one is false (false is returned)
    :status 401:
        Client must be authenticated
    :status 403:
        Forbidden access. The service is forbidden or one of the attributes is forbidden.
    :status 404:
        Unknown uin
    :status 500:
        Unexpected error (See :ref:`error`)

    **Example request:**

    .. sourcecode:: http

        POST /v1/persons/{uin}/verify HTTP/1.1
        Host: example.com
        Content-Type: application/json

        [
            {
                "attributeName": "firstName",
                "operator": "=",
                "value": "John"
            },
            {
                "attributeName": "dateOfBirth",
                "operator": "<",
                "value": "1990-12-31"
            }
        ]


    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        true


    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 500 Internal Server Error
        Content-Type: application/json

        {
            "code": 1,
            "message": "string"
        }


.. http:get:: /v1/persons/{uin}/document
    :synopsis: null

    Retrieve in an unstructured format (PDF, image) a document such as a marriage certificate.

    :param string uin:
        Unique Identity Number
    :query string secondaryUin:
        Unique Identity Number of a second person linked to the requested document.
        Example: wife, husband
    :query string doctype:
        The type of document
        (Required)
    :query string format:
        The expected format of the document.
        If the document is not available at this format, it must be converted.
        TBD: one format for certificate data.
        (Required)
    :status 200:
        The document(s) is/are found and returned, as binary data in a MIME multipart structure.
    :status 401:
        Client must be authenticated
    :status 403:
        Service forbidden
    :status 404:
        Unknown uin
    :status 415:
        Unsupported format
    :status 500:
        Unexpected error (See :ref:`error`)

    **Example request:**

    .. sourcecode:: http

        GET /v1/persons/{uin}/document?doctype=marriage&secondaryUin=234567890&format=pdf HTTP/1.1
        Host: example.com



    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 500 Internal Server Error
        Content-Type: application/json

        {
            "code": 1,
            "message": "string"
        }


Data Model
""""""""""

.. _person-attributes:

Person Attributes
'''''''''''''''''

When exchanged in the services described in this document, the persons attributes
will apply the following rules:

.. list-table:: Person Attributes
    :header-rows: 1
    :widths: 20 30 50
    
    * - Attribute Name
      - Description
      - Format
      
    * - ``uin``
      - Unique Identity Number
      - Text
    * - ``firstName``
      - First name
      - Text
    * - ``lastName``
      - Last name
      - Text
    * - ``spouseName``
      - Spouse name
      - Text
    * - ``dateOfBirth``
      - Date of birth
      - Date (iso8601). Example: ``1987-11-17``
    * - ``placeOfBirth``
      - Place of birth
      - Text
    * - ``gender``
      - Gender
      - Number (iso5218). One of 0 (Not known), 1 (Male), 2 (Female), 9 (Not applicable)
    * - ``dateOfDeath``
      - Date of death
      - Date (iso8601). Example: ``2018-11-17``
    * - ``placeOfDeath``
      - Place of death
      - Text
    * - ``reasonOfDeath``
      - Reason of death
      - Text
    * - ``status``
      - Status. Example: missing, wanted, dead, etc.
      - Text

    
.. _matching-error:

Matching Error
''''''''''''''

A list of:

.. list-table:: Matching Error Object
    :header-rows: 1
    :widths: 25 20 35 10
    
    * - Attribute
      - Type
      - Description
      - Mandatory

    * - ``attributeName``
      - String
      - Attribute name (See :ref:`person-attributes`)
      - Yes

    * - ``errorCode``
      - 32 bits integer
      - Error code. Possible values: ``0`` (attribute does not exist); ``1`` (attribute exists but does not match)
      - Yes

.. _expression:

Expression
''''''''''

.. list-table:: Expression Object
    :header-rows: 1
    :widths: 25 20 35 10
    
    * - Attribute
      - Type
      - Description
      - Mandatory

    * - ``attributeName``
      - String
      - Attribute name (See :ref:`person-attributes`)
      - Yes

    * - ``operator``
      - String
      - Operator to apply. Possible values: ``<``, ``>``, ``=``, ``>=``, ``<=``
      - Yes

    * - ``value``
      - string, or integer, or boolean
      - The value to be evaluated
      - Yes

.. _error:

Error
'''''

.. list-table:: Error Object
    :header-rows: 1
    :widths: 25 20 35 10
    
    * - Attribute
      - Type
      - Description
      - Mandatory

    * - ``code``
      - 32 bits integer
      - Error code
      - Yes

    * - ``message``
      - String
      - Error message
      - Yes

