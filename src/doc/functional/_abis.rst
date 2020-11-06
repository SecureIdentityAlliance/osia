
Biometrics
----------

This interface describes biometric services in the context of an identity system. It is based on
the following principles:

- It supports only multi-encounter model, meaning that an identity can have multiple set of biometric data,
  one for each encounter.
- It does not expose templates (only images) for CRUD services, with one exception to support
  the use case of credentials with biometrics.
- Images can be passed by value or reference. When passed by value, they are base64-encoded.
- Existing standards are used whenever possible, for instance preferred image format for biometric data is ISO-19794.

.. admonition:: About synchronous and asynchronous processing

    Some services can be very slow depending on the algorithm used, the system workload, etc.
    Services are described so that:

    - If possible, the answer is provided synchronously in the response of the service.
    - If not possible for some reason, a status *PENDING* is returned and the answer, when available, is
      pushed to a callback provided by the client.

    If no callback is provided, this indicates that the client wants a synchronous answer, whatever the time it takes.

    If a callback is provided, the server will decide if the processing is done synchronously or asynchronously.

See :ref:`annex-interface-abis` for the technical details of this interface.

Services
""""""""

.. py:function:: createEncounter(personID, encounterID, galleryID, biographicData, contextualData, biometricData, clientData,callback, transactionID, options)
    :noindex:

    Create a new encounter. No identify is performed.

    **Authorization**: ``abis.encounter.write``

    :param str personID: The person ID. This is optional and will be generated if not provided
    :param str encounterID: The encounter ID. This is optional and will be generated if not provided
    :param list(str) galleryID: the gallery ID to which this encounter belongs. A minimum of one gallery must be provided
    :param dict biographicData: The biographic data (ex: name, date of birth, gender, etc.)
    :param dict contextualData: The contextual data (ex: encounter date, location, etc.)
    :param list biometricData: the biometric data (images)
    :param bytes clientData: additional data not interpreted by the server but stored as is and returned
        when encounter data is requested.
    :param callback: The address of a service to be called when the result is available.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :param dict options: the processing options. Supported options are ``priority``, ``algorithm``.
    :return: a status indicating success, error, or pending operation.
        In case of success, the person ID and the encounter ID are returned.
        In case of pending operation, the result will be sent later.

.. py:function:: readEncounter(personID, encounterID, callback, transactionID, options)
    :noindex:

    Read the data of an encounter.

    **Authorization**: ``abis.encounter.read``

    :param str personID: The person ID
    :param str encounterID: The encounter ID. This is optional. If not provided, all the
        encounters of the person are returned.
    :param callback: The address of a service to be called when the result is available.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :param dict options: the processing options. Supported options are ``priority``.
    :return: a status indicating success, error, or pending operation.
        In case of success, the encounter data is returned.
        In case of pending operation, the result will be sent later.

.. py:function:: updateEncounter(personID, encounterID, galleryID, biographicData, contextualData, biometricData, callback, transactionID, options)
    :noindex:

    Update an encounter.

    **Authorization**: ``abis.encounter.write``

    :param str personID: The person ID
    :param str encounterID: The encounter ID
    :param list(str) galleryID: the gallery ID to which this encounter belongs. A minimum of one gallery must be provided
    :param dict biographicData: The biographic data (ex: name, date of birth, gender, etc.)
    :param dict contextualData: The contextual data (ex: encounter date, location, etc.)
    :param list biometricData: the biometric data (images)
    :param bytes clientData: additional data not interpreted by the server but stored as is and returned
        when encounter data is requested.
    :param callback: The address of a service to be called when the result is available.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :param dict options: the processing options. Supported options are ``priority``, ``algorithm``.
    :return: a status indicating success, error, or pending operation.
        In case of success, the person ID and the encounter ID are returned.
        In case of pending operation, the result will be sent later.

.. py:function:: deleteEncounter(personID, encounterID, callback, transactionID, options)
    :noindex:

    Delete an encounter.

    **Authorization**: ``abis.encounter.write``

    :param str personID: The person ID
    :param str encounterID: The encounter ID. This is optional. If not provided, all the
        encounters of the person are deleted.
    :param callback: The address of a service to be called when the result is available.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :param dict options: the processing options. Supported options are ``priority``.
    :return: a status indicating success, error, or pending operation.
        In case of pending operation, the operation status will be sent later.

.. py:function:: mergeEncounter(personID1, personID2, callback, transactionID, options)
    :noindex:

    Merge two sets of encounters into a single set. Merging a set of *N* encounters with a set of *M* encounters
    will result in a single set of *N+M* encounters. Encounter ID are preserved and in case of duplicates
    an error is returned and no changes are done.

    **Authorization**: ``abis.encounter.write``

    :param str personID1: The ID of the person that will receive new encounters
    :param str personID2: The ID of the person that will give its encounters
    :param callback: The address of a service to be called when the result is available.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :param dict options: the processing options. Supported options are ``priority``.
    :return: a status indicating success, error, or pending operation.
        In case of pending operation, the result will be sent later.

.. py:function:: readTemplate(personID, encounterID, biometricType, biometricSubType, templateFormat, qualityFormat, callback, transactionID, options)
    :noindex:

    Read the generated template.

    **Authorization**: ``abis.encounter.read``

    :param str personID: The person ID
    :param str encounterID: The encounter ID.
    :param str biometricType: The type of biometrics to consider (optional)
    :param str biometricSubType: The subtype of biometrics to consider (optional)
    :param str templateFormat: the format of the template to return (optional)
    :param str qualityFormat: the format of the quality to return (optional)
    :param callback: The address of a service to be called when the result is available.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :param dict options: the processing options. Supported options are ``priority``.
    :return: a status indicating success, error, or pending operation.
        In case of success, a list of template data is returned.
        In case of pending operation, the result will be sent later.

.. py:function:: updateEncounterStatus(personID, encounterID, status, transactionID)
    :noindex:

    Set an encounter status.

    **Authorization**: ``abis.encounter.write``

    :param str personID: The ID of the person.
    :param str encounterID: The encounter ID.
    :param str status: The new status of the encounter.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :return: a status indicating success or error.

.. py:function:: updateEncounterGalleries(personID, encounterID, galleries, transactionID)
    :noindex:

    Update the galleries of an encounter.
    This service is used to move one encounter from one gallery
    to another one without updating the full encounter, which maybe
    resource consuming in a biometric system.

    **Authorization**: ``abis.encounter.write``

    :param str personID: The ID of the person.
    :param str encounterID: The encounter ID.
    :param list[str] galleries: The new list of galleries for this encounter.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :return: a status indicating success or error.

----------

.. py:function:: readGalleries(callback, transactionID, options)
    :noindex:

    Read the ID of all the galleries.

    **Authorization**: ``abis.gallery.read``

    :param callback: The address of a service to be called when the result is available.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :param dict options: the processing options. Supported options are ``priority``.
    :return: a status indicating success, error, or pending operation.
        A list of gallery ID is returned, either synchronously or using the callback.

.. py:function:: readGalleryContent(galleryID, callback, transactionID, offset, limit, options)
    :noindex:

    Read the content of one gallery, i.e. the IDs of all the records linked to this gallery.

    **Authorization**: ``abis.gallery.read``

    :param str galleryID: Gallery whose content will be returned.
    :param callback: The address of a service to be called when the result is available.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :param int offset: The offset of the query (first item of the response) (optional, default to ``0``)
    :param int limit: The maximum number of items to return (optional, default to ``1000``)
    :param dict options: the processing options. Supported options are ``priority``.
    :return: a status indicating success, error, or pending operation.
        A list of persons/encounters is returned, either synchronously or using the callback.

----------

.. py:function:: identify(galleryID, filter, biometricData, callback, transactionID, options)
    :noindex:

    Identify a person using biometrics data and filters on biographic or contextual data. This may include multiple
    operations, including manual operations.

    **Authorization**: ``abis.identify``

    :param str galleryID: Search only in this gallery.
    :param dict filter: The input data (filters and biometric data)
    :param biometricData: the biometric data.
    :param callback: The address of a service to be called when the result is available.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :param dict options: the processing options. Supported options are ``priority``,
        ``maxNbCand``, ``threshold``, ``accuracyLevel``.
    :return: a status indicating success, error, or pending operation.
        A list of candidates is returned, either synchronously or using the callback.

.. py:function:: identify(galleryID, filter, personID, callback, transactionID, options)
    :noindex:

    Identify a person using biometrics data of a person existing in the system and filters on biographic or
    contextual data. This may include multiple operations, including manual operations.

    **Authorization**: ``abis.verify``

    :param str galleryID: Search only in this gallery.
    :param dict filter: The input data (filters and biometric data)
    :param personID: the person ID
    :param callback: The address of a service to be called when the result is available.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :param dict options: the processing options. Supported options are ``priority``,
        ``maxNbCand``, ``threshold``, ``accuracyLevel``.
    :return: a status indicating success, error, or pending operation.
        A list of candidates is returned, either synchronously or using the callback.

.. py:function:: verify(galleryID, personID, biometricData, callback, transactionID, options)
    :noindex:

    Verify an identity using biometrics data.

    **Authorization**: ``abis.verify``

    :param str galleryID: Search only in this gallery. If the person does not belong to this gallery,
        an error is returned.
    :param str personID: The person ID
    :param biometricData: The biometric data
    :param callback: The address of a service to be called when the result is available.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :param dict options: the processing options. Supported options are ``priority``,
        ``threshold``, ``accuracyLevel``.
    :return: a status indicating success, error, or pending operation.
        A status (boolean) is returned, either synchronously or using the callback. Optionally, details
        about the matching result can be provided like the score per biometric and per encounter.

.. py:function:: verify(biometricData1, biometricData2, callback, transactionID, options)
    :noindex:

    Verify that two sets of biometrics data correspond to the same person.

    **Authorization**: ``abis.verify``

    :param biometricData1: The first set of biometric data
    :param biometricData2: The second set of biometric data
    :param callback: The address of a service to be called when the result is available.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :param dict options: the processing options. Supported options are ``priority``,
        ``threshold``, ``accuracyLevel``.
    :return: a status indicating success, error, or pending operation.
        A status (boolean) is returned, either synchronously or using the callback. Optionally, details
        about the matching result can be provided like the score per the biometric.

Options
"""""""

.. list-table:: Biometric Services Options
    :header-rows: 1
    :widths: 25 75

    * - Name
      - Description

    * - ``priority``
      - Priority of the request. Values range from ``0`` to ``9``.
        ``0`` indicates the lowest priority, ``9`` indicates the highest priority.
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
""""""""""

.. list-table:: Biometric Data Model
    :header-rows: 1
    :widths: 25 50 25

    * - Type
      - Description
      - Example

    * - Gallery
      - A group of persons related by a common purpose, designation, or status.
        A person can belong to multiple galleries.
      - :todo:`TBD`

    * - Person
      - Person who is known to an identity assurance system.
      - :todo:`TBD`

    * - Encounter
      - Event in which the client application interacts with a person resulting in data being
        collected during or about the encounter. An encounter is characterized by an *identifier* and a *type*
        (also called *purpose* in some context).

        An encounter has a status indicating if this encounter is used in the biometric searches. Allowed values
        are ``active`` or ``inactive``.

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
      
        All images can be passed by value (image buffer is in the request) or by reference (the address of the
        image is in the request).
        All images are compliant with ISO 19794. ISO 19794 allows multiple encoding and supports additional
        metadata specific to fingerprint, palmprint, portrait, iris or signature.

        A biometric data can be associated to no image or a partial image if it includes information about
        the missing items (example: one finger may be amputated on a 4 finger image)
      - fingerprint, portrait, iris, signature

    * - Candidate
      - Information about a candidate found during an identification
      - :todo:`TBD`

    * - CandidateScore
      - Detailed information about a candidate found during an identification. It includes
        the score for the biometrics used. It can also be extended with proprietary information to better describe
        the matching result (for instance: rotation needed to align the probe and the candidate)
      - :todo:`TBD`

    * - Template
      - A computed buffer corresponding to a biometric and allowing the comparison of biometrics.
        A template has a format that can be a standard format or a vendor-specific format.
      - N/A
      
.. uml::
    :caption: Biometric Data Model
    :scale: 50%

    class Gallery {
        string galleryID;
    }

    class Person {
        string personID;
    }

    class Encounter {
        string encounterID;
        string status;
        string encounterType;
        byte[] clientData;
    }

    Encounter "*" -- "*" Gallery

    Person o-- "*" Encounter

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
        byte[] image;
        URL imageRef;
    }

    Encounter o-- "*" BiometricData

    class Template {
        byte[] buffer;
        string format;
    }
    BiometricData -- Template

    class Candidate {
        int rank;
        int score;
    }
    Candidate . Person

    class CandidateScore {
        float score;
        string encounterID;
        enum biometricType;
        enum biometricSubType;
        ...
    }
    Candidate -- "*" CandidateScore
