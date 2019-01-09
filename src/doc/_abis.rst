.. http:post:: /v1/subjects/{subjectId}/{encounterId}
    :synopsis: Insert

    **Insert**

    :param string subjectId:
        the id of the subject
    :param string encounterId:
        the id of the encounter
    :query string transactionId:
        The id of the transaction
    :query integer priority:
        the request priority

    :status 201:
        Insertion successful
    :status 400:
        Bad request
    :status 403:
        Insertion not allowed
    :status 500:
        Unexpected error

    **Example request:**

    .. sourcecode:: http

        POST /v1/subjects/00001/22 HTTP/1.1
        Host: example.com
        Content-Type: application/json

        {
            "data": [
                {
                    "biometricType": "FACE",
                    "biometricSubType": "UNKNOWN",
                    "image": "byte",
                    "imageRef": "https://example.com"
                }
            ],
            "filters": {
                "galleries": [
                    "string"
                ],
                "lastName": "string",
                "firstName": "string",
                "dateOfBirth": "2019-01-09"
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


.. http:get:: /v1/subjects/{subjectId}/{encounterId}
    :synopsis: Read

    **Read**

    :param string subjectId:
        the id of the subject
    :param string encounterId:
        the id of the encounter
    :query string transactionId:
        The id of the transaction
    :query integer priority:
        the request priority
    :status 200:
        Read successful


    :status 400:
        Bad request
    :status 403:
        Read not allowed
    :status 404:
        Unknown record
    :status 500:
        Unexpected error

    **Example request:**

    .. sourcecode:: http

        GET /v1/subjects/00001/22?transactionId=tid01&priority=2 HTTP/1.1
        Host: example.com

    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": [
                {
                    "biometricType": "FACE",
                    "biometricSubType": "UNKNOWN",
                    "image": "byte",
                    "imageRef": "https://example.com"
                }
            ],
            "filters": {
                "galleries": [
                    "string"
                ],
                "lastName": "string",
                "firstName": "string",
                "dateOfBirth": "2019-01-09"
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


.. http:put:: /v1/subjects/{subjectId}/{encounterId}
    :synopsis: Update

    **Update**

    :param string subjectId:
        the id of the subject
    :param string encounterId:
        the id of the encounter
    :query string transactionId:
        The id of the transaction
    :query integer priority:
        the request priority

    :status 204:
        Update successful
    :status 400:
        Bad request
    :status 403:
        Update not allowed
    :status 404:
        Unknown record
    :status 500:
        Unexpected error

    **Example request:**

    .. sourcecode:: http

        PUT /v1/subjects/{subjectId}/{encounterId} HTTP/1.1
        Host: example.com
        Content-Type: application/json

        {
            "data": [
                {
                    "biometricType": "FACE",
                    "biometricSubType": "UNKNOWN",
                    "image": "byte",
                    "imageRef": "https://example.com"
                }
            ],
            "filters": {
                "galleries": [
                    "string"
                ],
                "lastName": "string",
                "firstName": "string",
                "dateOfBirth": "2019-01-09"
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


.. http:delete:: /v1/subjects/{subjectId}/{encounterId}
    :synopsis: Delete one encounter

    **Delete one encounter**

    :param string subjectId:
        the id of the subject
    :param string encounterId:
        the id of the encounter
    :query string transactionId:
        The id of the transaction
    :query integer priority:
        the request priority
    :status 204:
        Delete successful
    :status 400:
        Bad request
    :status 403:
        Delete not allowed
    :status 404:
        Unknown record
    :status 500:
        Unexpected error

    **Example request:**

    .. sourcecode:: http

        DELETE /v1/subjects/00001/22?transactionId=tid01&priority=4 HTTP/1.1
        Host: example.com

    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 500 Internal Server Error
        Content-Type: application/json

        {
            "code": 1,
            "message": "string"
        }


.. http:delete:: /v1/subjects/{subjectId}
    :synopsis: Delete all encounter

    **Delete all encounter**

    :param string subjectId:
        the id of the subject
    :query string transactionId:
        The id of the transaction
    :query integer priority:
        the request priority
    :status 204:
        Delete successful
    :status 400:
        Bad request
    :status 403:
        Delete not allowed
    :status 404:
        Unknown record
    :status 500:
        Unexpected error

    **Example request:**

    .. sourcecode:: http

        DELETE /v1/subjects/00001?transactionId=tid01&priority=4 HTTP/1.1
        Host: example.com

    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 500 Internal Server Error
        Content-Type: application/json

        {
            "code": 1,
            "message": "string"
        }


.. http:post:: /v1/identify/{galleryId}
    :synopsis: Identification based on biometric data from one gallery

    **Identification based on biometric data from one gallery**

    :param string galleryId:
        the id of the gallery
    :query string callback:
        the callback address, where the identification result will be sent when available
    :query string transactionId:
        The id of the transaction
    :query integer priority:
        the request priority
    :query integer maxNbCand:
        the maximum number of candidates
    :query number threshold:
        the algorithm threshold
    :query string algorithm:
        the algorithm to use for this request
    :status 202:
        Identification request received successfully and correct
    :status 400:
        Bad request
    :status 403:
        Identification not allowed
    :status 500:
        Unexpected error

    **Example request:**

    .. sourcecode:: http

        POST /v1/identify/G01?callback=http%3A%2F%2Fclient.com%2Fcallback&transactionId=tid01&maxNbCand=10 HTTP/1.1
        Host: example.com
        Content-Type: application/json

        {
            "data": [
                {
                    "biometricType": "FACE",
                    "biometricSubType": "UNKNOWN",
                    "image": "byte",
                    "imageRef": "https://example.com"
                }
            ]
        }

    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 500 Internal Server Error
        Content-Type: application/json

        {
            "code": 1,
            "message": "string"
        }

.. admonition:: Callback

    .. http:post:: /callback
        :synopsis: null

        Callback called when the result of the identification is available.

        The request body will contain the list of candidates.

        :query string transactionId:
            The id of the transaction
        :status 204: Response is received and accepted.
        :status 403: Forbidden access to the service
        :status 500: Unexpected error

    **Example request:**

    .. sourcecode:: http

        POST http://client.com/callback?transactionId=tid01 HTTP/1.1
        Host: client.com
        Content-Type: application/json

        [
        {
            "subjectId": "00001",
            "rank": 1,
            "score": 1234,
            "scoreList": [
            {
                "score": 1234,
                "biometricType": "FACE",
                "biometricSubType": "PORTRAIT"
            }
            ]
        },
        {
            "subjectId": "30107",
            "rank": 2,
            "score": 234,
            "scoreList": [
            {
                "score": 234,
                "biometricType": "FACE",
                "biometricSubType": "PORTRAIT"
            }
            ]
        }
        ]


.. http:post:: /v1/verify/{subjectId}
    :synopsis: Verification of one set of biometric data and a record in the system

    **Verification of one set of biometric data and a record in the system**

    :param string subjectId:
        the id of the subject
    :query string transactionId:
        The id of the transaction
    :query integer priority:
        the request priority
    :query number threshold:
        the algorithm threshold
    :query string algorithm:
        the algorithm to use for this request

    :status 200:
        Verification execution successful

    :status 400:
        Bad request
    :status 404:
        Unknown record
    :status 403:
        Verification not allowed
    :status 500:
        Unexpected error

    **Example request:**

    .. sourcecode:: http

        POST /v1/verify/{subjectId} HTTP/1.1
        Host: example.com
        Content-Type: application/json

        {
            "data": [
                {
                    "biometricType": "FACE",
                    "biometricSubType": "UNKNOWN",
                    "image": "byte",
                    "imageRef": "https://example.com"
                }
            ]
        }

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


.. http:post:: /v1/verify
    :synopsis: Verification of two sets of biometric data

    **Verification of two sets of biometric data**

    :query string transactionId:
        The id of the transaction
    :query integer priority:
        the request priority
    :query number threshold:
        the algorithm threshold
    :query string algorithm:
        the algorithm to use for this request
    :status 200:
        Verification execution successful
    :status 400:
        Bad request
    :status 403:
        Verification not allowed
    :status 500:
        Unexpected error

    **Example request:**

    .. sourcecode:: http

        POST /v1/verify HTTP/1.1
        Host: example.com
        Content-Type: application/json

        {
            "data1": [
                {
                    "biometricType": "FACE",
                    "biometricSubType": "UNKNOWN",
                    "image": "byte",
                    "imageRef": "https://example.com"
                }
            ],
            "data2": [
                {
                    "biometricType": "FACE",
                    "biometricSubType": "UNKNOWN",
                    "image": "byte",
                    "imageRef": "https://example.com"
                }
            ]
        }

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


