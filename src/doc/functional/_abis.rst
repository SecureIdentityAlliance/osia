
Biometrics
----------

This interface is described biometric services in the context of an identity system. It is based on
the following principles:

- It supports only multi-encounter model, meaning that an identity can have multiple set of biometric data,
  one for each encounter.
- It does not expose templates (only images) for CRUD services, with one exception to support
  the use case of documents with biometrics.
- Images can be passed by value or reference. When passed by value, they are base64-encoded.
- Existing standards are used whenever possible, for instance image preferred format is ISO-19794.

.. note:: Synchronous and Asynchronous Processing

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

.. py:function:: insert(subjectID, encounterID, galleryID, biographicData, contextualData, biometricData, clientData,callback, options)
    :noindex:

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
    :noindex:

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
    :noindex:

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
    :noindex:

    Delete an encounter.

    :param str subjectID: The subject ID
    :param str encounterID: The encounter ID. This is optional. If not provided, all the
        encounters of the subject are deleted.
    :param callback: The address of a service to be called when the result is available.
    :param dict options: the processing options. Supported options are ``transactionID``, ``priority``.
    :return: a status indicating success, error, or pending operation.
        In case of pending operation, the operation status will be sent later.

.. py:function:: getTemplate(subjectID, encounterID, biometricType, biometricSubType, callback, options)
    :noindex:

    Retrieve the data of an encounter.

    :param str subjectID: The subject ID
    :param str encounterID: The encounter ID. This is optional. If not provided, all the
        encounters of the subject are returned.
    :param str biometricType: The type of biometrics to consider
    :param str biometricSubType: The subtype of biometrics to consider
    :param callback: The address of a service to be called when the result is available.
    :param dict options: the processing options. Supported options are ``transactionID``, ``priority``.
    :return: a status indicating success, error, or pending operation.
        In case of success, a list of template data is returned.
        In case of pending operation, the result will be sent later.


----------

.. py:function:: identify(galleryID, filter, biometricData, callback, options)
    :noindex:

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
    :noindex:

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
    :noindex:

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
    :noindex:

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
    :noindex:

    Get the ID os all the galleries.

    :param callback: The address of a service to be called when the result is available.
    :param dict options: the processing options. Supported options are ``transactionID``, ``priority``.
    :return: a status indicating success, error, or pending operation.
        A list of gallery ID is returned, either synchronously or using the callback.

.. py:function:: getGalleryContent(galleryID, callback, options)
    :noindex:

    Get the content of one gallery, i.e. the IDs of all the records linked to this gallery.

    :param str galleryID: Gallery whose content will be returned.
    :param callback: The address of a service to be called when the result is available.
    :param dict options: the processing options. Supported options are ``transactionID``, ``priority``.
    :return: a status indicating success, error, or pending operation.
        A list of subjects/encounters is returned, either synchronously or using the callback.


Options
"""""""

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
""""""""""

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

    * - Template
      - A computed buffer corresponding to a biometric and allowing the comparison of biometrics.
        A template has a format that can be a standard format or a vendor-specific format.
      - N/A
      
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

    class Template {
          byte[] buffer;
        string format;
    }

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

    Finger -- Template
    Palm -- Template
    Portrait -- Template
    Iris -- Template

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
