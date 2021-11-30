
Notification
------------

See :ref:`annex-interface-notification` for the technical details of this interface.

The subscription & notification process is managed by a middleware and is described
in the following diagram:

.. uml::
    :caption: Subscription & Notification Process
    :scale: 50%

    hide footbox
    participant "Emitter" as PR
    participant "Notification\nEngine" as N
    participant "Subscriber" as CR

    note over PR,N: First step is to create the topic
    PR -> N: create_topic(name)
    activate PR
    activate N
    N --> PR: uuid
    deactivate N
    deactivate PR

    note over N,CR: Then a system can subscribe for events published on that topic

    CR -> N: subscribe(topic,notify_URL)
    activate CR
    activate N
    N --> CR: id
    deactivate CR
    deactivate N

    ... later ...

    note over N,CR: confirm the address before the subscription is active

    N -> CR: notify(message)
    activate N
    activate CR
    CR -> N: confirm(token)
    activate N #FFBBBB
    N --> CR: ok
    deactivate N
    CR --> N: ok
    deactivate CR
    deactivate N

    note over PR,CR: it is now possible to publish notification

    PR -> N: publish(message)
    activate PR
    activate N
    N -> N: store
    N --> PR: ok
    deactivate PR

    ...

    loop subscriptions
      N -> CR: notify(message)
      activate CR
      CR --> N: ok
      deactivate CR
    end
    deactivate N



Services
""""""""

For the Subscriber
''''''''''''''''''

.. py:function:: subscribe(topic,URL)
    :noindex:

    Subscribe a URL to receive notifications sent to one topic

    **Authorization**: ``notif.sub.write``

    :param str topic: Topic
    :param str URL: URL to be called when a notification is available
    :return: a subscription ID

This service is synchronous.

.. py:function:: listSubscriptions()
    :noindex:

    Get all subscriptions

    **Authorization**: ``notif.sub.read``

    :param str URL: URL to be called when a notification is available
    :return: a subscription ID

This service is synchronous.

.. py:function:: unsubscribe(id)
    :noindex:

    Unsubscribe a URL from the list of receiver for one topic

    **Authorization**: ``notif.sub.write``

    :param str id: Subscription ID
    :return: bool

This service is synchronous.

.. py:function:: confirm(token)
    :noindex:

    Used to confirm that the URL used during the subscription is valid

    **Authorization**: ``notif.sub.write``

    :param str token: A token send through the URL.
    :return: bool

This service is synchronous.

For the Publisher
'''''''''''''''''

.. py:function:: createTopic(topic)
    :noindex:

    Create a new topic. This is required before an event can be sent to it.

    **Authorization**: ``notif.topic.write``

    :param str topic: Topic
    :return: N/A

This service is synchronous.

.. py:function:: listTopics()
    :noindex:

    Get the list of all existing topics.

    **Authorization**: ``notif.topic.read``

    :return: N/A

This service is synchronous.

.. py:function:: deleteTopic(topic)
    :noindex:

    Delete a topic.

    **Authorization**: ``notif.topic.write``

    :param str topic: Topic
    :return: N/A

This service is synchronous.

.. py:function:: publish(topic,subject,message)
    :noindex:

    Notify of a new event all systems that subscribed to this topic

    **Authorization**: ``notif.topic.publish``

    :param str topic: Topic
    :param str subject: The subject of the message
    :param str message: The message itself (a string buffer)
    :return: N/A

This service is asynchronous (systems that subscribed on this topic are notified asynchronously).

For the Receiver
''''''''''''''''

.. py:function:: notify(message)
    :noindex:

    Receive an event published by a publisher.
    This service needs to be registered through the subscription process.

    :param str message: The message itself (a string buffer)
    :return: N/A

Dictionaries
""""""""""""

As an example, below there is a list of events that each component might handle.

.. list-table:: Event Type
    :header-rows: 1
    
    * - Event Type
      - Emitted by CR
      - Emitted by PR
      
    * - Live birth
      - |tick|
      -
    * - Death
      - |tick|
      -
    * - Fœtal Death
      - |tick|
      -
    * - Marriage
      - |tick|
      -
    * - Divorce
      - |tick|
      -
    * - Annulment
      - |tick|
      -
    * - Separation, judicial
      - |tick|
      -
    * - Adoption
      - |tick|
      -
    * - Legitimation
      - |tick|
      -
    * - Recognition
      - |tick|
      -
    * - Change of name
      - |tick|
      -
    * - Change of gender
      - |tick|
      -
    * - New person
      -
      - |tick|
    * - Duplicate person
      - |tick|
      - |tick|
