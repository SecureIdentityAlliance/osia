
Functional Specifications
-------------------------


This chapter describes the following group of services.

- UIN management. This service can be implemented by PR, by CR or by another system. We will consider it is provided
  by a system called *UIN Generator*.
- Notifications. When data is changed, a notification is sent and received by systems that registered for
  this type of events. For instance, PR can register for the events *birth* emitted by CR.
- Data access. A set of services to access data.
- Usage. Identity based services implemented on top of Identity system mainly *Identity Verification* and
  *Identity Attribute* sharing.

The design is based on the following assumptions:

#. All persons recorded in CR have a :term:`UIN`. The UIN can be used as a key to access person data for all records.
#. All persons recorded in PR have a UIN. The UIN can be used as a key to access person data for all records.
#. The CR and PR are both considered as centralized systems that are connected. If CR is architectured in a
   decentralized way, and it is often the case, one of its component must be centralized, connected to the network,
   and in charge of the exchanges with PR.
#. Since all instances of CR and PR are customized for each business needs, dictionaries must be explicitly
   defined to describe the attributes, the event types, and the document types. See :ref:`technical-specifications`
   for the mandatory elements of those dictionaries.
#. The relationship parent/child is not mandatory in PR. A PR implementation may manage this relationship
   or may ignore it and rely on CR to manage it.
#. All persons are stored in PR. There is no record in CR that is not also in PR.
#. The interface does not expose biometric services. Usage of biometrics is optional and is described in other
   standards already defined.

The services described in this chapter are summarized in the following table:

======================= ======= ======= =========== ======= ======= =========== =========== =======
ID ecosystem components
---------------------------------------------------------------------------------------------------
Services                Enroll  PR      UIN gen.    ABIS    CR      ID Card     Funct. Reg  Usage
======================= ======= ======= =========== ======= ======= =========== =========== =======
**Notification**
---------------------------------------------------------------------------------------------------
Notify event                    U                           U
Subscribe                       U                   U       U       U           U
Unsubscribe                     U                   U       U       U           U
Event callback                  I                   I       I       I           I
----------------------- ------- ------- ----------- ------- ------- ----------- ----------- -------
**UIN Management**
---------------------------------------------------------------------------------------------------
Generate UIN                    U       I                   U       U
----------------------- ------- ------- ----------- ------- ------- ----------- ----------- -------
**Data Access**
---------------------------------------------------------------------------------------------------
Get Person Attributes   U       IU                  U       IU      U           U           U
Match Person Attributes         IU                          IU      U           U           U
Verify Person Attribute         IU                          IU      U           U           U
Get Person UIN          U       IU                          IU      U           U
Get document                    IU                          IU
----------------------- ------- ------- ----------- ------- ------- ----------- ----------- -------
**Biometrics**
---------------------------------------------------------------------------------------------------
Verify                  U                           I               U           U           U
Identify                U                           I               U           U           U
Insert                          U                   I               U
Read                            U                   I               U           U           U
Update                          U                   I               U
Delete                          U                   I               U
Get Gallery                     U                   I               U           U
Get Gallery content             U                   I               U           U
----------------------- ------- ------- ----------- ------- ------- ----------- ----------- -------
**3rd parties services**
---------------------------------------------------------------------------------------------------
Verify ID                                                                                   I
Identify ID                                                                                 I
Get Attributes                                                                              I
Get Attributes set                                                                          I
======================= ======= ======= =========== ======= ======= =========== =========== =======

where:

- ``I`` is used when a service is implemented (provided) by a component
- ``U`` is used when a service is used (consumed) by a component

Notifications
"""""""""""""

Services
''''''''

.. py:function:: subscribe(type,URL)

   Subscribe a URL to receive notifications for one kind of event

   :param str type: Event type
   :param str URL: URL to be called when a notification is available
   :return: bool

This service is synchronous.

.. py:function:: unsubscribe(type,URL)

   Unsubscribe a URL from the list of receiver for one kind of event

   :param str type: Event type
   :param str URL: URL used during the subscription
   :return: bool

This service is synchronous.

.. py:function:: notify(type,UIN)

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
''''''''''''

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

UIN Management
""""""""""""""

Services
''''''''

.. py:function:: createUIN(attributes)

   Generate a new UIN.

   :param list[(str,str)] attributes: A list of pair (attribute name, value) that can be used to allocate a new UIN
   :return: a new UIN or an error if the generation is not possible

This service is synchronous.

.. uml::
    :caption: ``createUIN`` Sequence Diagram
    :scale: 50%

    !include "skin.iwsd"
    hide footbox
    participant "CR" as CR
    participant "PR" as PR
    participant "UIN Generator" as UIN

    note over CR,UIN: CR can request a new UIN
    CR -> UIN: createUIN([attributes])
    UIN -->> CR: UIN

    note over PR,UIN: PR can request a new UIN
    PR -> UIN: createUIN([attributes])
    UIN -->> PR: UIN


Data Access
"""""""""""

Services
''''''''

.. py:function:: getPersonAttributes(UIN, names)

   Retrieve person attributes.

   :param str UIN: The person's UIN
   :param list[str] names: The names of the attributes requested
   :return: a list of pair (name,value). In case of error (unknown attributes, unauthorized access, etc.) the value is replaced with an error

This service is synchronous. It can be used to retrieve attributes from CR or from PR.

.. uml::
    :caption: ``getPersonAttributes`` Sequence Diagram
    :scale: 50%

    !include "skin.iwsd"
    hide footbox
    participant "CR" as CR
    participant "PR" as PR

    note over CR,PR: CR can request person's attributes from PR
    CR -> PR: getPersonAttributes(UIN,[names])
    PR -->> CR: attributes

    note over CR,PR: PR can request person's attributes from CR
    PR -> CR: getPersonAttributes(UIN,[names])
    CR -->> PR: attributes

-------

.. py:function:: matchPersonAttributes(UIN, attributes)

    Match person attributes. This service is used to check the value of attributes without exposing private data
    
    :param str UIN: The person's UIN
    :param list[(str,str)] attributes: The attributes to match. Each attribute is described with its name and the expected value
    :return: If all attributes match, a *Yes* is returned. If one attribute does not match, a *No* is returned along with a list of (name,reason) for each non-matching attribute.
    
This service is synchronous. It can be used to match attributes in CR or in PR.

.. uml::
    :caption: ``matchPersonAttributes`` Sequence Diagram
    :scale: 50%

    !include "skin.iwsd"
    hide footbox
    participant "CR" as CR
    participant "PR" as PR

    note over CR,PR: CR can match person's attributes in PR
    CR -> PR: matchPersonAttributes(UIN,[attributes])
    PR -->> CR: Y/N+reasons

    note over CR,PR: PR can match person's attributes in CR
    PR -> CR: matchPersonAttributes(UIN,[attributes])
    CR -->> PR: Y/N+reasons

-------

.. py:function:: verifyPersonAttributes(UIN, expressions)

    Evaluate expressions on person attributes. This service is used to evaluate simple expressions on person's attributes
    without exposing private data
    
    :param str UIN: The person's UIN
    :param list[(str,str,str)] expressions: The expressions to evaluate. Each expression is described with the attribute's name, the operator (one of ``<``, ``>``, ``=``, ``>=``, ``<=``) and the attribute value
    :return: A *Yes* if all expressions are true, a *No* if one expression is false, a *Unknown* if :todo:`To be defined`
    
This service is synchronous. It can be used to verify attributes in CR or in PR.

.. uml::
    :caption: ``verifyPersonAttributes`` Sequence Diagram
    :scale: 50%

    !include "skin.iwsd"
    hide footbox
    participant "CR" as CR
    participant "PR" as PR

    note over CR,PR: CR can verify person's attributes in PR
    CR -> PR: verifyPersonAttributes(UIN,[expressions])
    PR -->> CR: Y/N/U

    note over CR,PR: PR can verify person's attributes in CR
    PR -> CR: verifyPersonAttributes(UIN,[expressions])
    CR -->> PR: Y/N/U

-------

.. py:function:: getPersonUIN(attributes)

    Retrieve UIN based on a set of attributes. This service is used when the UIN is unknown.

    :param list[(str,str)] attributes: The attributes to be used to find UIN. Each attribute is described with its name and its value
    :return: a list of matching UIN
    
This service is synchronous. It can be used to get the UIN of a person.

.. uml::
    :caption: ``getPersonUIN`` Sequence Diagram
    :scale: 50%

    !include "skin.iwsd"
    hide footbox
    participant "CR" as CR
    participant "PR" as PR

    note over CR,PR: CR can get UIN from PR
    CR -> PR: getPersonUIN([attributes])
    PR -->> CR: [UIN]

    note over CR,PR: PR can get UIN from CR
    PR -> CR: getPersonUIN([attributes])
    CR -->> PR: [UIN]

-------

.. py:function:: getDocument(UINs,documentType,format)

    Retrieve in a selected format (PDF, image, ...) a document such as a marriage certificate.

    :param list[str] UIN: The list of UINs for the persons concerned by the document
    :param str documentType: The type of document (birth certificate, etc.)
    :param str format: The format of the returned/requested document
    :return: The list of the requested documents
    
This service is synchronous. It can be used to get the documents for a person.

.. uml::
    :caption: ``getDocument`` Sequence Diagram
    :scale: 50%

    !include "skin.iwsd"
    hide footbox
    participant "CR" as CR
    participant "PR" as PR

    note over CR,PR: CR can get a document from PR
    CR -> PR: getDocument([UIN],documentType,format)
    PR -->> CR: [documents]

    note over CR,PR: PR can get a document from CR
    PR -> CR: getDocument([UIN],documentType,format)
    CR -->> PR: [documents]

Dictionaries
''''''''''''

.. list-table:: Person Attributes
    :header-rows: 1
    
    * - Attribute Name
      - In CR
      - In PR
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
      - In PR
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
      - In PR
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
      - In PR
      - Description

    * - parent1 UIN
      - |tick|
      -
      -
    * - parent2 UIN
      - |tick|
      -
      -

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

Biometrics
""""""""""

.. note:: Synchronous and Asynchronous Processing

    Some services can be very slow depending on the algorithm used, the system workload, etc.
    Services are described so that:

    - If possible, the answer is provided synchronously in the response of the service.
    - If not possible for some reason, a status *PENDING* is returned and the answer, when available, is
      pushed to a callback provided by the client.

    If no callback is provided, this indicates that the client wants a synchronous answer, whatever the time it takes.

    If a callback is provided, the server will decide if the processing is done synchronously or asynchronously.

  :todo:`add sequence diagrams`

..  admonition:: Principles

    - Support only multi-encounter model
    - Do not expose templates (only images) for CRUD services
    - Focus on simple essential services (CRUD, identify, verify)
    - Images can be passed by value or reference
    - Image format: ISO-19794

Services
''''''''

.. py:function:: insert(subjectID, encounterID, galleryID, biographicData, contextualData, biometricData, clientData,callback, options)

    Insert a new encounter. No identify is performed. This service is synchronous.

    :param str subjectID: The subject ID
    :param str encounterID: The encounter ID. This is optional
    :param list(str) galleryID: the gallery ID to which this encounter belongs
    :param dict biographicData: The biographic data (ex: name, date of birth, gender, etc.)
    :param dict contextualData: The contextual data (ex: encounter date, location, etc.)
    :param list biometricData: the biometric data (images)
    :param bytes clientData: additional data not interpreted by the server but stored as is and returned
        when encounter data is requested.
    :param callback: The address of a service to be called when the result is available.
    :param dict options: the processing options. Supported options are ``transactionID``, ``priority``, ``algorithm``.
    :return: a status indicating success, error, or pending operation.
        In case of success, the subject ID and the encounter ID are returned.
        In case of pending operation, the result will be sent later.

.. py:function:: read(subjectID, encounterID, callback, options)

    Retrieve the data of an encounter.

    :param str subjectID: The subject ID
    :param str encounterID: The encounter ID. This is optional. If not provided, all the
        encounters of the subject are returned.
    :param callback: The address of a service to be called when the result is available.
    :param dict options: the processing options. Supported options are ``transactionID``, ``priority``.
    :return: a status indicating success, error, or pending operation.
        In case of success, the encounter data is returned.
        In case of pending operation, the result will be sent later.

.. py:function:: update(subjectID, encounterID, galleryID, biographicData, contextualData, biometricData, callback, options)

    Update an encounter.

    :param str subjectID: The subject ID
    :param str encounterID: The encounter ID
    :param list(str) galleryID: the gallery ID to which this encounter belongs
    :param dict biographicData: The biographic data (ex: name, date of birth, gender, etc.)
    :param dict contextualData: The contextual data (ex: encounter date, location, etc.)
    :param list biometricData: the biometric data (images)
    :param bytes clientData: additional data not interpreted by the server but stored as is and returned
        when encounter data is requested.
    :param callback: The address of a service to be called when the result is available.
    :param dict options: the processing options. Supported options are ``transactionID``, ``priority``, ``algorithm``.
    :return: a status indicating success, error, or pending operation.
        In case of success, the subject ID and the encounter ID are returned.
        In case of pending operation, the result will be sent later.

.. py:function:: delete(subjectID, encounterID, callback, options)

    Delete an encounter.

    :param str subjectID: The subject ID
    :param str encounterID: The encounter ID. This is optional. If not provided, all the
        encounters of the subject are deleted.
    :param callback: The address of a service to be called when the result is available.
    :param dict options: the processing options. Supported options are ``transactionID``, ``priority``.
    :return: a status indicating success, error, or pending operation.
        In case of pending operation, the operation status will be sent later.

----------

.. py:function:: identify(galleryID, filter, biometricData, callback, options)

    Identify a subject using biometrics data and filters on biographic or contextual data. This may include multiple
    operations, including manual operations.

    :param str galleryID: Search only in this gallery.
    :param dict filter: The input data (filters and biometric data)
    :param biometricData: the biometric data.
    :param callback: The address of a service to be called when the result is available.
    :param dict options: the processing options. Supported options are ``transactionID``, ``priority``,
        ``maxNbCand``, ``threshold``, ``accuracyLevel``.
    :return: a status indicating success, error, or pending operation.
        A list of candidates is returned, either synchronously or using the callback.

.. py:function:: identify(galleryID, filter, subjectID, callback, options)

    Identify a subject using biometrics data of a subject existing in the system and filters on biographic or
    contextual data. This may include multiple operations, including manual operations.

    :param str galleryID: Search only in this gallery.
    :param dict filter: The input data (filters and biometric data)
    :param subjectID: the subject ID
    :param callback: The address of a service to be called when the result is available.
    :param dict options: the processing options. Supported options are ``transactionID``, ``priority``,
        ``maxNbCand``, ``threshold``, ``accuracyLevel``.
    :return: a status indicating success, error, or pending operation.
        A list of candidates is returned, either synchronously or using the callback.

.. py:function:: verify(galleryID, subjectID, biometricData, callback, options)

    Verify an identity using biometrics data.

    :param str galleryID: Search only in this gallery. If the subject does not belong to this gallery,
        an error is returned.
    :param str subjectID: The subject ID
    :param biometricData: The biometric data
    :param callback: The address of a service to be called when the result is available.
    :param dict options: the processing options. Supported options are ``transactionID``, ``priority``,
        ``threshold``, ``accuracyLevel``.
    :return: a status indicating success, error, or pending operation.
        A status (boolean) is returned, either synchronously or using the callback. Optionally, details
        about the matching result can be provided like the score per biometric and per encounter.

.. py:function:: verify(biometricData1, biometricData2, callback, options)

    Verify that two sets of biometrics data correspond to the same subject.

    :param biometricData1: The first set of biometric data
    :param biometricData2: The second set of biometric data
    :param callback: The address of a service to be called when the result is available.
    :param dict options: the processing options. Supported options are ``transactionID``, ``priority``,
        ``threshold``, ``accuracyLevel``.
    :return: a status indicating success, error, or pending operation.
        A status (boolean) is returned, either synchronously or using the callback. Optionally, details
        about the matching result can be provided like the score per the biometric.

----------

.. py:function:: getGalleries(callback, options)

    Get the ID os all the galleries.

    :param callback: The address of a service to be called when the result is available.
    :param dict options: the processing options. Supported options are ``transactionID``, ``priority``.
    :return: a status indicating success, error, or pending operation.
        A list of gallery ID is returned, either synchronously or using the callback.

.. py:function:: getGalleryContent(galleryID, callback, options)

    Get the content of one gallery, i.e. the IDs of all the records linked to this gallery.

    :param str galleryID: Gallery whose content will be returned.
    :param callback: The address of a service to be called when the result is available.
    :param dict options: the processing options. Supported options are ``transactionID``, ``priority``.
    :return: a status indicating success, error, or pending operation.
        A list of subjects/encounters is returned, either synchronously or using the callback.


Options
'''''''

.. list-table:: Biometric Services Options
    :header-rows: 1
    :widths: 25 75

    * - Name
      - Description

    * - ``transactionID``
      - A string provided by the client application to identity the request being submitted.
        It is optional in most cases. When provided, it can be used for tracing and debugging.
        It is mandatory for asynchronous services and is included in the response pushed asynchronously.
    * - ``priority``
      - Priority of the request. Values range from 0 to 9
    * - ``maxNbCand``
      - The maximum number of candidates to return.
    * - ``threshold``
      - The threshold to apply on the score to filter the candidates during an identification,
        authentication or verification.
    * - ``algorithm``
      - Specify the type of algorithm to be used.
    * - ``accuracyLevel``
      - Specify the accuracy expected of the request. This is to support different use cases, when
        different behavior of the ABIS is expected (response time, accuracy, consolidation/fusion, etc.).

Data Model
''''''''''

.. list-table:: Biometric Data Model
    :header-rows: 1
    :widths: 25 50 25

    * - Type
      - Description
      - Example

    * - Gallery
      - A group of subjects related by a common purpose, designation, or status.
        A subject can belong to multiple galleries.
      - :todo:`TBD`

    * - Subject
      - Person who is known to an identity assurance system.
      - :todo:`TBD`

    * - Encounter
      - Event in which the client application interacts with a subject resulting in data being
        collected during or about the encounter. An encounter is characterized by an *identifier* and a *type*
        (also called *purpose* in some context).
      - :todo:`TBD`

    * - Biographic Data
      - a dictionary (list of names and values) giving the biographic data of interest for the biometric services.
      - :todo:`TBD`

    * - Filters
      - a dictionary (list of names and values or *range* of values) describing the filters during a search.
        Filters can apply on biographic data, contextual data or encounter type.
      - :todo:`TBD`

    * - Biometric Data
      - Digital representation of biometric characteristics.
        As an example, a record containing the image of a finger is a biometric data.
        All images can be passed by value (image buffer is in the request) or by reference (the address of the
        image is in the request).
        All images are compliant with ISO 19794. ISO 19794 allows multiple encoding and supports additional
        metadata specific to fingerprint, palmprint, portrait or iris.
      - :todo:`TBD`

    * - Candidate
      - Information about a candidate found during an identification
      - :todo:`TBD`

    * - CandidateScore
      - Detailed information about a candidate found during an identification. It includes
        the score for the biometrics used.
      - :todo:`TBD`
      
.. uml::
    :caption: Biometric Data Model
    :scale: 50%

    !include "skin.iwsd"

    class Gallery {
        string galleryID;
    }

    class Subject {
        string subjectID;
    }

    Subject "*" - "*" Gallery

    class Encounter {
        string encounterID;
        string encounterType;
        byte[] clientData;
    }

    Subject o-- "*" Encounter

    class BiographicData {
        string field1;
        int field2;
        date field3;
        ...
    }
    Encounter o- BiographicData

    class ContextualData {
        string field1;
        int field2;
        date field3;
        ...
    }
    ContextualData -o Encounter
    
    class Filters {
        string filter1;
        int filter2Min;
        int filter2Max;
        date filter3Min;
        date filter3Max;
        ...
    }


    class BiometricData {
    }

    Encounter o-- "*" BiometricData

    class Finger {
        byte[] fingerImage;
        URL fingerImageRef;
    }
    BiometricData <|-- Finger

    class Palm {
        byte[] palmImage;
        URL palmImageRef;
    }
    BiometricData <|-- Palm

    class Portrait {
        byte[] portraitImage;
        URL portraitImageRef;
    }
    BiometricData <|-- Portrait
    
    class Iris {
        byte[] irisImage;
        URL irisImageRef;
    }
    BiometricData <|-- Iris
    
    class Candidate {
      int rank;
      int score;
    }
    Candidate . Subject

    class CandidateScore {
      int score;
      string encounterID;
      enum biometricType;
      enum biometricSubType;
    }
    Candidate -- "*" CandidateScore

Third Party Services
""""""""""""""""""""

Services
''''''''

.. py:function:: verifyIdentity(UIN, [IDAttribute])

    Verify Identity based on UIN and set of Identity Attributes.
    Attributes can be Biometric data, Civil data or a credential.

    :param str UIN: The person's UIN
    :param list[str] IDAttribute: A list of list of pair (name,value) requested
    :return: Y or N
    
    In case of error (unknown attributes, unauthorized access, etc.) the value is replaced with an error

.. py:function:: identify([inIDAttribute], [outIDAttribute])

    Identify a person based on a set of inIDAttribute Identity Attributes.
    Attributes can be Biometric data, Civil data or a credential.
    Returns list of identities with attributes specified in outIDAttribute

    :param list[str] inIDAttribute: A list of list of pair (name,value) requested
    :param list[str] outIDAttribute: A list of list of attribute names requested
    :return: Y or N
    
    In case of error (unknown attributes, unauthorized access, etc.) the value is replaced with an error

.. py:function:: getAttributes(UIN, names)

    Retrieve person attributes.

    :param str UIN: The person's UIN
    :param list[str] names: The names of the attributes requested
    :return: a list of pair (name,value). In case of error (unknown attributes, unauthorized access, etc.)
        the value is replaced with an error

.. py:function:: getAttributeSet(UIN, setName)

    Retrieve person attributes corresponding to a predefined set name.

    :param str UIN: The person's UIN
    :param str setName: The name of predefined attributes set name
    :return: a list of pair (name,value). In case of error (unknown attributes, unauthorized access, etc.)
        the value is replaced with an error

   
 