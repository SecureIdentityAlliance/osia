
Notification
------------

See :ref:`annex-interface-notification` for the technical details of this interface.

Services
""""""""

.. py:function:: subscribe(type,URL)
    :noindex:

    Subscribe a URL to receive notifications for one kind of event

    :param str type: Event type
    :param str URL: URL to be called when a notification is available
    :return: bool

This service is synchronous.

.. py:function:: unsubscribe(type,URL)
    :noindex:

    Unsubscribe a URL from the list of receiver for one kind of event

    :param str type: Event type
    :param str URL: URL used during the subscription
    :return: bool

This service is synchronous.

.. py:function:: notify(type,UIN)
    :noindex:

    Notify of a new event all systems that subscribed to this event

    :param str type: Event type
    :param list[str] UIN: Records affected by the event
    :return: N/A

This service is asynchronous.

.. uml::
    :caption: ``notify`` Sequence Diagram
    :scale: 50%

    !include "skin.iwsd"
    hide footbox
    participant "CR" as CR
    participant "PR" as PR

    note over CR,PR: CR can notify PR of new events
    CR ->> PR: notify(type,[UIN])

    note over CR,PR: PR can notify CR of new events
    PR ->> CR: notify(type,[UIN])

.. note::

    Notifications are possible after the receiver has subscribed to an event.

Dictionaries
""""""""""""

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
