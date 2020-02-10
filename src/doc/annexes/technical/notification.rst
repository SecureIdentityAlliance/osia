
.. _annex-interface-notification:

Notification
------------

.. only:: html

    Get the OpenAPI file for this interface: `notification.yaml <../../notification.yaml>`_

.. raw:: latex

    Get the OpenAPI file for this interface: \textattachfile[]{../html/notification.yaml}{notification.yaml}

Services
""""""""

Publisher
'''''''''

.. http:post:: /v1/topics
    :synopsis: Create a topic

    **Create a topic**

    Create a new topic. This service is idempotent.

    :query string name:
        The topic name
        (Required)
    :status 200:
        Topic was created.
    :status 500:
        Unexpected error

    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "uuid": "string",
            "name": "string"
        }


    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 500 Internal Server Error
        Content-Type: application/json

        {
            "code": 1,
            "message": "string"
        }


.. http:get:: /v1/topics
    :synopsis: Get all topics

    **Get all topics**

    :status 200:
        Get all topics
    :status 500:
        Unexpected error

    **Example request:**

    .. sourcecode:: http

        GET /v1/topics HTTP/1.1
        Host: example.com



    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "uuid": "string",
                "name": "string"
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


.. http:delete:: /v1/topics/{uuid}
    :synopsis: Delete a topic

    **Delete a topic**

    Delete a topic

    :param string uuid:
        the unique ID returned when the topic was created
    :status 204:
        Topic successfully removed
    :status 404:
        Topic not found
    :status 500:
        Unexpected error

    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 500 Internal Server Error
        Content-Type: application/json

        {
            "code": 1,
            "message": "string"
        }


.. http:post:: /v1/topics/{uuid}/publish
    :synopsis: Post a notification to a topic.

    **Post a notification to a topic.**

    :param string uuid:
        the unique ID of the topic
    :query string subject:
        the subject of the message.
    :status 200:
        Notification published
    :status 500:
        Unexpected error

    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 500 Internal Server Error
        Content-Type: application/json

        {
            "code": 1,
            "message": "string"
        }


Subscriber
''''''''''

.. http:post:: /v1/subscriptions
    :synopsis: Subscribe to a topic

    **Subscribe to a topic**

    Subscribes a client to receive event notification.
    
    Subscriptions are idempotent. Subscribing twice for the same topic and
    endpoint (protocol, address) will return the same subscription ID and the
    subscriber will receive only once the notifications.

    :query string topic:
        The name of the topic for which notifications will be sent
        (Required)
    :query string protocol:
        The protocol used to send the notification
    :query string address:
        the endpoint address, where the notifications will be sent.
        (Required)
    :query string policy:
        The delivery policy, expressing what happens when the message cannot be delivered.
        
        If not specified, retry will be done every hour for 7 days.
        
        The value is a set of integer separated by comma:
        
        - countdown: the number of seconds to wait before retrying. Default: 3600.
        - max: the maximum max number of retry. -1 indicates infinite retry. Default: 168
    :status 200:
        Subscription successfully created. Waiting for confirmation message.
    :status 500:
        Unexpected error

    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "uuid": "string",
            "topic": "string",
            "protocol": "http",
            "address": "string",
            "policy": "string",
            "active": true
        }


    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 500 Internal Server Error
        Content-Type: application/json

        {
            "code": 1,
            "message": "string"
        }


.. admonition:: Callback: onEvent

    .. http:post:: {$request.query.address}
        :synopsis: null

        :status 200:
            Message received and processed.
        :status 500:
            Unexpected error
        :reqheader message-type:
            the type of the message
            (Required)
        :reqheader subscription-id:
            the unique ID of the subscription
        :reqheader message-id:
            the unique ID of the message
            (Required)
        :reqheader topic-id:
            the unique ID of the topic
            (Required)

        **Example request:**

        .. sourcecode:: http

            POST {$request.query.address} HTTP/1.1
            Host: example.com
            Content-Type: application/json

            {
                "type": "SubscriptionConfirmation",
                "token": "string",
                "topic": "string",
                "message": "string",
                "messageId": "string",
                "subject": "string",
                "subscribeURL": "https://example.com",
                "timestamp": "string"
            }


        **Example response:**

        .. sourcecode:: http

            HTTP/1.1 500 Internal Server Error
            Content-Type: application/json

            {
                "code": 1,
                "message": "string"
            }



.. http:get:: /v1/subscriptions
    :synopsis: Get all subscriptions

    **Get all subscriptions**

    :status 200:
        Get all subscriptions
    :status 500:
        Unexpected error

    **Example request:**

    .. sourcecode:: http

        GET /v1/subscriptions HTTP/1.1
        Host: example.com



    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "uuid": "string",
                "topic": "string",
                "protocol": "http",
                "address": "string",
                "policy": "string",
                "active": true
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


.. http:delete:: /v1/subscriptions/{uuid}
    :synopsis: Unsubscribe from a topic

    **Unsubscribe from a topic**

    Unsubscribes a client from receiving notifications for a topic

    :param string uuid:
        the unique ID returned when the subscription was done
    :status 204:
        Subscription successfully removed
    :status 404:
        Subscription not found
    :status 500:
        Unexpected error

    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 500 Internal Server Error
        Content-Type: application/json

        {
            "code": 1,
            "message": "string"
        }


.. http:get:: /v1/subscriptions/confirm
    :synopsis: Confirm the subscription

    **Confirm the subscription**

    Confirm a subscription

    :query string token:
        the token sent to the endpoint
        (Required)
    :status 200:
        Subscription successfully confirmed
    :status 400:
        Invalid token
    :status 500:
        Unexpected error

    **Example request:**

    .. sourcecode:: http

        GET /v1/subscriptions/confirm?token=string HTTP/1.1
        Host: example.com



    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 500 Internal Server Error
        Content-Type: application/json

        {
            "code": 1,
            "message": "string"
        }

Notification Message
""""""""""""""""""""

This section describes the messages exchanged through notification. All messages
are encoded in ``json``. They are generated by the emitter (the source of the event)
and received by zero, one, or many receivers that have subscribed to the type of event.

.. list-table:: Event Type & Message
    :header-rows: 1
    :widths: 30 70
    :class: longtable
    
    * - Event Type
      - Message
      
    * - ``liveBirth``
      - - ``source``: identification of the system emitting the event
        - ``uin`` of the new born
        - ``uin1`` of the first parent (optional if parent is unknown)
        - ``uin2`` of the second parent (optional if parent is unknown)

        Example:

        .. code-block:: json

            {
                "source": "systemX",
                "uin": "123456789",
                "uin1": "123456789",
                "uin2": "234567890"
            }
            
    * - ``death``
      - - ``source``: identification of the system emitting the event
        - ``uin`` of the dead person

        Example:

        .. code-block:: json

            {
                "source": "systemX",
                "uin": "123456789"
            }
            
    * - ``birthCancellation``
      - - ``source``: identification of the system emitting the event
        - ``uin`` of the person whose birth declaration is being cancelled

        Example:

        .. code-block:: json

            {
                "source": "systemX",
                "uin": "123456789",
            }

    * - ``foetalDeath``
      - - ``source``: identification of the system emitting the event
        - ``uin`` of the new born

        Example:

        .. code-block:: json

            {
                "source": "systemX",
                "uin": "123456789"
            }
            
    * - ``marriage``
      - - ``source``: identification of the system emitting the event
        - ``uin1`` of the first conjoint
        - ``uin2`` of the second conjoint

        Example:

        .. code-block:: json

            {
                "source": "systemX",
                "uin1": "123456789",
                "uin2": "234567890"
            }
            
    * - ``divorce``
      - - ``source``: identification of the system emitting the event
        - ``uin1`` of the first conjoint
        - ``uin2`` of the second conjoint

        Example:

        .. code-block:: json

            {
                "source": "systemX",
                "uin1": "123456789",
                "uin2": "234567890"
            }
            
    * - ``annulment``
      - - ``source``: identification of the system emitting the event
        - ``uin1`` of the first conjoint
        - ``uin2`` of the second conjoint

        Example:

        .. code-block:: json

            {
                "source": "systemX",
                "uin1": "123456789",
                "uin2": "234567890"
            }
            
    * - ``separation``
      - - ``source``: identification of the system emitting the event
        - ``uin1`` of the first conjoint
        - ``uin2`` of the second conjoint

        Example:

        .. code-block:: json

            {
                "source": "systemX",
                "uin1": "123456789",
                "uin2": "234567890"
            }
            
    * - ``adoption``
      - - ``source``: identification of the system emitting the event
        - ``uin`` of the child
        - ``uin1`` of the first parent
        - ``uin2`` of the second parent (optional)

        Example:

        .. code-block:: json

            {
                "source": "systemX",
                "uin": "123456789",
                "uin1": "234567890"
            }
            
    * - ``legitimation``
      - - ``source``: identification of the system emitting the event
        - ``uin`` of the child
        - ``uin1`` of the first parent
        - ``uin2`` of the second parent (optional)

        Example:

        .. code-block:: json

            {
                "source": "systemX",
                "uin": "987654321",
                "uin1": "123456789",
                "uin2": "234567890"
            }
            
    * - ``recognition``
      - - ``source``: identification of the system emitting the event
        - ``uin`` of the child
        - ``uin1`` of the first parent
        - ``uin2`` of the second parent (optional)

        Example:

        .. code-block:: json

            {
                "source": "systemX",
                "uin": "123456789",
                "uin2": "234567890"
            }
            
    * - ``changeOfName``
      - - ``source``: identification of the system emitting the event
        - ``uin`` of the person

        Example:

        .. code-block:: json

            {
                "source": "systemX",
                "uin": "123456789"
            }
            
    * - ``changeOfGender``
      - - ``source``: identification of the system emitting the event
        - ``uin`` of the person

        Example:

        .. code-block:: json

            {
                "source": "systemX",
                "uin": "123456789"
            }
            
    * - ``updatePerson``
      - - ``source``: identification of the system emitting the event
        - ``uin`` of the person

        Example:

        .. code-block:: json

            {
                "source": "systemX",
                "uin": "123456789"
            }
            
    * - ``newPerson``
      - - ``source``: identification of the system emitting the event
        - ``uin`` of the person

        Example:

        .. code-block:: json

            {
                "source": "systemX",
                "uin": "123456789"
            }

    * - ``duplicatePerson``
      - - ``source``: identification of the system emitting the event
        - ``uin`` of the person to be kept
        - ``duplicates``: list of uin for records identified as duplicates

        Example:

        .. code-block:: json

            {
                "source": "systemX",
                "uin": "123456789",
                "duplicates": [
                    "234567890",
                    "345678901"
                ]
            }
            
.. note::

    Anonymized notification of events will be treated separately.


