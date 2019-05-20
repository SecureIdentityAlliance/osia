
.. _annex-interface-uin:

UIN Management
--------------

Download the OpenAPI file for this interface :todo:`here`.

Services
""""""""

.. http:post:: /v1/uin

   Request the generation of a new UIN.

   The request body should contain a list of attributes and their value, formatted as a json dictionary.

   :status 200: UIN is generated
   :status 401: Client must be authenticated
   :status 403: Service forbidden
   :status 500: Unexpected error (See :ref:`error`)

**Example request:**

.. sourcecode:: http

   POST http://server.com/v1/uin HTTP/1.1
   Host: server.com
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

   1235567890

**Example response:**

.. sourcecode:: http

   HTTP/1.1 500 Internal Server Error
   Content-Type: application/json

   {
         "code": 1,
         "message": "string"
   }
