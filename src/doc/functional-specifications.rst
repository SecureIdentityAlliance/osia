
Functional Specifications
-------------------------

Hypothesis
""""""""""

The design of this interface is based on the following assumptions:

#. All persons recorded in CR have a :term:`UIN`. The UIN can be used as a key to access person data for all records.
#. All persons recorded in CI have a UIN. The UIN can be used as a key to access person data for all records.
#. The CR and CI are both considered as centralized systems that are connected. If CR is architectured in a
   decentralized way, and it is often the case, one of its component must be centralized, connected to the network,
   and in charge of the exchanges with CI.
#. Since all instances of CR and CI are customized for each business needs, dictionaries must be explicitly
   defined to describe the attributes, the event types, and the document types. See `Dictionaries`_ for
   the mandatory elements of those dictionaries.
#. The relationship parent/child is not mandatory in CI. A CI implementation may manage this relationship
   or may ignore it and rely on CR to manage it.
#. All persons are stored in CI. There is no record in CR that is not also in CI.
#. The interface does not expose biometric services. Usage of biometrics is optional and is described in other
   standards already defined.

Concepts
""""""""

:todo:`To be completed`

Interface
"""""""""

Functions/Sevices
'''''''''''''''''

This chapter describes in pseudo code the services defined between CR and CI.
There three categories of services:

- UIN creation. This service can be implemented by CI, by CR or by another system. We will consider it is provided
  by a system called *UIN Generator*.
- Events notification. When data is changed, a notification can be sent and received by systems that registered for
  this type of events. For instance, CI can register for the events *birth* emitted by CR.
- Data access. A set of services to exchange data.

UIN Creation
~~~~~~~~~~~~~

.. py:function:: createUIN(attributes)

   Generate a new UIN.

   :param list[(str,str)] attributes: A list of pair (attribute name, value) that can be used to allocate a new UIN
   :return: a new UIN or an error if the generation is not possible

This service is synchronous.

.. uml::
    :caption: createUIN

    !include "skin.iwsd"
    hide footbox
    participant "CR" as CR
    participant "CI" as CI
    participant "UIN Generator" as UIN

    note over CR,UIN: CR can request a new UIN
    CR -> UIN: createUIN([attributes])
    UIN -->> CR: UIN

    note over CI,UIN: CI can request a new UIN
    CI -> UIN: createUIN([attributes])
    UIN -->> CI: UIN


Notifications
~~~~~~~~~~~~~

.. py:function:: notify(type,UIN)

   Notify of a new event all systems that subscribed to this event

   :param str type: Event type
   :param list[str] UIN: Records affected by the event
   :return: N/A

This service is asynchronous.

.. uml::
    :caption: notify

    !include "skin.iwsd"
    hide footbox
    participant "CR" as CR
    participant "CI" as CI

    note over CR,CI: CR can notify CI of new events
    CR ->> CI: notify(type,[UIN])

    note over CR,CI: CI can notify CR of new events
    CI ->> CR: notify(type,[UIN])

.. note::

    Notifications are possible after the receiver has subscribed to an event. This subscription is dependent on
    the middleware used and not described in this document.
    
Data Access Services
~~~~~~~~~~~~~~~~~~~~

.. py:function:: getPersonAttributes(UIN, names)

   Retrieve person attributes.

   :param str UIN: The person's UIN
   :param list[str] names: The names of the attributes requested
   :return: a list of pair (name,value). In case of error (unknown attributes, unauthorized access, etc.) the value is replaced with an error

This service is synchronous. It can be used to retrieve attributes from CR or from CI.

.. uml::
    :caption: getPersonAttributes

    !include "skin.iwsd"
    hide footbox
    participant "CR" as CR
    participant "CI" as CI

    note over CR,CI: CR can request person's attributes from CI
    CR -> CI: getPersonAttributes(UIN,[names])
    CI -->> CR: attributes

    note over CR,CI: CI can request person's attributes from CR
    CI -> CR: getPersonAttributes(UIN,[names])
    CR -->> CI: attributes

-------

.. py:function:: matchPersonAttributes(UIN, attributes)

    Match person attributes. This service is used to check the value of attributes without exposing private data
    
    :param str UIN: The person's UIN
    :param list[(str,str)] attributes: The attributes to match. Each attribute is described with its name and the expected value
    :return: If all attributes match, a *Yes* is returned. If one attribute does not match, a *No* is returned along with a list of (name,reason) for each non-matching attribute.
    
This service is synchronous. It can be used to match attributes in CR or in CI.

.. uml::
    :caption: matchPersonAttributes

    !include "skin.iwsd"
    hide footbox
    participant "CR" as CR
    participant "CI" as CI

    note over CR,CI: CR can match person's attributes in CI
    CR -> CI: matchPersonAttributes(UIN,[attributes])
    CI -->> CR: Y/N+reasons

    note over CR,CI: CI can match person's attributes in CR
    CI -> CR: matchPersonAttributes(UIN,[attributes])
    CR -->> CI: Y/N+reasons

-------

.. py:function:: verifyPersonAttributes(UIN, expressions)

    Evaluate expressions on person attributes. This service is used to evaluate simple expressions on person's attributes
    without exposing private data
    
    :param str UIN: The person's UIN
    :param list[(str,str,str)] expressions: The expressions to evaluate. Each expression is described with the attribute's name, the operator (one of ``<``, ``>``, ``=``, ``>=``, ``<=``) and the attribute value
    :return: A *Yes* if all expressions are true, a *No* if one expression is false, a *Unknown* if :todo:`To be defined`
    
This service is synchronous. It can be used to verify attributes in CR or in CI.

.. uml::
    :caption: verifyPersonAttributes

    !include "skin.iwsd"
    hide footbox
    participant "CR" as CR
    participant "CI" as CI

    note over CR,CI: CR can verify person's attributes in CI
    CR -> CI: verifyPersonAttributes(UIN,[expressions])
    CI -->> CR: Y/N/U

    note over CR,CI: CI can verify person's attributes in CR
    CI -> CR: verifyPersonAttributes(UIN,[expressions])
    CR -->> CI: Y/N/U

-------

.. py:function:: getPersonUIN(attributes)

    Retrieve UIN based on a set of attributes. This service is used when the UIN is unknown.

    :param list[(str,str)] attributes: The attributes to be used to find UIN. Each attribute is described with its name and its value
    :return: a list of matching UIN
    
This service is synchronous. It can be used to get the UIN of a person.

.. uml::
    :caption: getPersonUIN

    !include "skin.iwsd"
    hide footbox
    participant "CR" as CR
    participant "CI" as CI

    note over CR,CI: CR can get UIN from CI
    CR -> CI: getPersonUIN([attributes])
    CI -->> CR: [UIN]

    note over CR,CI: CI can get UIN from CR
    CI -> CR: getPersonUIN([attributes])
    CR -->> CI: [UIN]

-------

.. py:function:: getScannedDocument(UIN,type)

    Retrieve in an unstructured format (PDF, image) a document such as a marriage certificate.

    :param list[str] UIN: The list of UIN for the persons concerned by the document
    :parent str type: The type of document
    :return: a list of buffers for the requested document
    
This service is synchronous. It can be used to get the documents for a person.

.. uml::
    :caption: getScannedDocument

    !include "skin.iwsd"
    hide footbox
    participant "CR" as CR
    participant "CI" as CI

    note over CR,CI: CR can get a document from CI
    CR -> CI: getScannedDocument([UIN],type)
    CI -->> CR: [buffers]

    note over CR,CI: CI can get a document from CR
    CI -> CR: getScannedDocument([UIN],type)
    CR -->> CI: [buffers]

Dictionaries
''''''''''''

Attributes
~~~~~~~~~~

.. list-table:: Person Attributes
    :header-rows: 1
    
    * - Attribute Name
      - In CR
      - In CI
      - Description
      
    * - UIN
      - |tick|
      - |tick|
      -
    * - first name
      - |tick|
      - |tick|
      -
    * - last name
      - |tick|
      - |tick|
      -
    * - spouse name
      - |tick|
      - |tick|
      -
    * - date of birth
      - |tick|
      - |tick|
      -
    * - place of birth
      - |tick|
      - |tick|
      -
    * - gender
      - |tick|
      - |tick|
      -
    * - date of death
      - |tick|
      - |tick|
      -
    * - place of death
      - |tick|
      -
      -
    * - reason of death
      - |tick|
      -
      -
    * - status
      -
      - |tick|
      - Example: missing, wanted, dead, etc.

.. list-table:: Certificate Attributes
    :header-rows: 1
    
    * - Attribute Name
      - In CR
      - In CI
      - Description

    * - officer name
      - |tick|
      -
      -
    * - number
      - |tick|
      -
      -
    * - date
      - |tick|
      -
      -
    * - place
      - |tick|
      -
      -
    * - type
      - |tick|
      -
      -

.. list-table:: Union Attributes
    :header-rows: 1
    
    * - Attribute Name
      - In CR
      - In CI
      - Description

    * - date of union
      - |tick|
      -
      -
    * - place of union
      - |tick|
      -
      -
    * - conjoint1 UIN
      - |tick|
      -
      -
    * - conjoint2 UIN
      - |tick|
      -
      -
    * - date of divorce
      - |tick|
      -
      -

.. list-table:: Filiation Attributes
    :header-rows: 1
    
    * - Attribute Name
      - In CR
      - In CI
      - Description

    * - parent1 UIN
      - |tick|
      -
      -
    * - parent2 UIN
      - |tick|
      -
      -


Events
~~~~~~

.. list-table:: Event Type
    :header-rows: 1
    
    * - Event Type
      - Emitted by CR
      - Emitted by CI
      
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

Documents
~~~~~~~~~

.. list-table:: Document Type
    :header-rows: 1
    
    * - Document Type
      - Description
      
    * - birth certificate
      - :todo:`To be completed`
    * - death certificate
      - :todo:`To be completed`

    * - marriage certificate
      - :todo:`To be completed`


Use Cases
"""""""""

Birth Use Case
''''''''''''''

.. uml::
    :caption: Birth Use Case

    !include "skin.iwsd"
    hide footbox
    actor "Mother or Father" as parent
    participant "CR" as CR
    participant "CI" as CI
    participant "UIN Generator" as UINGen
    
    parent -> CR
    activate parent
    activate CR
    
    group 1. Checks
        CR -> CI: matchPersonAttributes(mother attributes)
        CR -> CI: matchPersonAttributes(father attributes)
        CR -> CI: getPersonAttributes(mother)
        CR -> CI: getPersonAttributes(father)
        CR -> CI: getPersonUIN(new born attributes)
        CR -> CR: Additional checks
    end
    
    group 2. Creation
        CR -> UINGen: createUIN()
        CR -> CR
        note right: register the birth

        CR -->> parent: certificate
        destroy parent
    end
    
    group 3. Notification
        CR ->> CI: notify(birth,UIN)
        deactivate CR

        ...
        
        CI -> CR: getPersonAttributes(new born)
        activate CI
        CI -> CR: getPersonAttributes(mother)
        CI -> CR: getPersonAttributes(father)
        CI -> CI
        note right: create/update identities
        deactivate CI
    end
  
1. Checks

   When a request is submitted, the CR may run checks against the data available in the CI using:

   - ``matchPersonAttributes``: to check the exactitude of the parents' attributes as known in the CI
   - ``getPersonAttributes``: to get missing data about the parents's identity
   - ``getPersonUIN``: to check if the new born is already known to CI or not

   How the CR will process the request in case of data discrepancy is specific to each CR implementation
   and not in the scope of this document.

2. Creation

   The birth is registered in the CR. The first step after the checks is to generate a new UIN
   a call to ``createUIN``.
    
3. Notification

   As part of the birth registration, it is the responsibility of the CR to notify other systems, including the CI,
   of this event using:
   
   - ``notify``: to send a *birth* along with the new ``UIN``.
   
   The CI, upon reception of the birth event, will update the identity registry with this new identity using:
    
   - ``getPersonAttributes``: to get the attributes of interest to the CI for the parents and the new child.

Death Use Case
''''''''''''''

:todo:`To be completed`

Fœtal Death Use Case
''''''''''''''''''''

:todo:`To be completed`

Marriage Use Case
'''''''''''''''''

:todo:`To be completed`

Divorce Use Case
''''''''''''''''

:todo:`To be completed`

Annulment Use Case
''''''''''''''''''

:todo:`To be completed`

Separation Use Case
'''''''''''''''''''

:todo:`To be completed`

Adoption Use Case
'''''''''''''''''

:todo:`To be completed`

Legitimation Use Case
'''''''''''''''''''''

:todo:`To be completed`

Recognition Use Case
''''''''''''''''''''

:todo:`To be completed`

Change of Name/Gender Use Case
''''''''''''''''''''''''''''''

:todo:`To be completed`

Transcription Use Case
''''''''''''''''''''''

:todo:`To be completed`

Change of Nationality Use Case
''''''''''''''''''''''''''''''

(To be confirmed)

