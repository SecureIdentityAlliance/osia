
Enrolment Services
------------------



Services
""""""""

.. py:function:: createPerson(personID, personData, options)
    :noindex:

    Insert a new person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person. If the person already exists for the ID an error is returned.
    :param dict personData: The person attributes.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error.

.. py:function:: readPerson(personID, filter, options)
    :noindex:

    Retrieve the attributes of a person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param set filter: A set of required attributes to retrieve.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error and in case of success the person data.

.. py:function:: updatePerson(personID, personData, options)
    :noindex:

    Update a person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param dict personData: The person data.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error.

.. py:function:: deletePerson(personID, options)
    :noindex:

    Delete a person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error.

----------

.. py:function:: createDocument(personID, documentID, documentData, options)
    :noindex:

    Add a new document for a person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str documentID: The ID of the document.
    :param documentData: The content and attributes of the document.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error.  In the case of success, a document identifier.

.. py:function:: readDocument(documentID, filter, options)
    :noindex:

    Retrieve document data.

    **Authorization**: :todo:`To be defined`

    :param str documentID: The ID of the document.
    :param set filter: A set of required attributes to retrieve.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error, and in case of success the document data.

.. py:function:: updateDocument(documentID, documentData, options)
    :noindex:

    Update a document for a person.

    **Authorization**: :todo:`To be defined`

    :param str documentID: The ID of the document.
    :param documentData: The content and attributes of the document.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error.

.. py:function:: deleteDocument(documentID, options)
    :noindex:

    Delete a document for a person.

    **Authorization**: :todo:`To be defined`

    :param str documentID: The ID of the document.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error.

.. py:function:: updateDocumentValidationStatus(documentID, status, options)
    :noindex:

    Updates the status of a document validation.

    **Authorization**: :todo:`To be defined`

    :param str documentValidationID: The ID of the document.
    :param status: The status of the document validation, e.g. 'ready' to validate.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error.

.. py:function:: readDocumentValidationStatus(documentID, options)
    :noindex:

    Retrieve the status of a document validation.

    **Authorization**: :todo:`To be defined`

    :param str documentValidationID: The ID of the document.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error, and in case of success the document validation status and its metadata.

----------

.. py:function:: createBiometric(personID, biometricID, biometricData, options)
    :noindex:

    Add a new biometric for a person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str biometricID: The ID of the biometric.
    :param biometricData: The content and attributes of the biometric.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error.  In the case of success, a biometric identifier.

.. py:function:: readBiometric(biometricID, filter, options)
    :noindex:

    Retrieve biometric data.

    **Authorization**: :todo:`To be defined`

    :param str biometricValidationID: The ID of the biometric.
    :param set filter: A set of required attributes to retrieve.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error, and in case of success the biometric data.

.. py:function:: updateBiometric(biometricID, biometricData, options)
    :noindex:

    Update a biometric for a person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str biometricID: The ID of the biometric.
    :param biometricData: The content and attributes of the biometric.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error.

.. py:function:: deleteBiometric(biometricID, options)
    :noindex:

    Delete a biometric for a person.

    **Authorization**: :todo:`To be defined`

    :param str biometricID: The ID of the biometric.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error.

.. py:function:: updateBiometricValidationStatus(biometricID, status, options)
    :noindex:

    Updates the status of a biometric validation.

    **Authorization**: :todo:`To be defined`

    :param str biometricValidationID: The ID of the biometric.
    :param status: The status of the biometric validation, e.g. 'ready' to validate.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error, and in case of success the biometric validation status.

.. py:function:: readBiometricValidationStatus(biometricID, options)
    :noindex:

    Retrieve the status of a biometric validation.

    **Authorization**: :todo:`To be defined`

    :param str biometricValidationID: The ID of the biometric.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error, and in case of success the biometric validation status and metadata.

----------

.. py:function:: createBiographic(personID, biographicID, biographicData, options)
    :noindex:

    Add a new biographic for a person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str biographicID: The ID of the biographic.
    :param biographicData: The content and attributes of the biographic.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error.  In the case of success, a biographic identifier.

.. py:function:: readBiographic(biographicID, filter, options)
    :noindex:

    Retrieve biographic data.

    **Authorization**: :todo:`To be defined`

    :param str biographicValidationID: The ID of the biographic.
    :param set filter: A set of required attributes to retrieve.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error, and in case of success the biographic data.

.. py:function:: updateBiographic(biographicID, biographicData, options)
    :noindex:

    Update a biographic for a person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str biographicID: The ID of the biographic.
    :param biographicData: The content and attributes of the biographic.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error.

.. py:function:: deleteBiographic(biographicID, options)
    :noindex:

    Delete a biographic for a person.

    **Authorization**: :todo:`To be defined`

    :param str biographicID: The ID of the biographic.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error.

.. py:function:: updateBiographicValidationStatus(biographicID, status, options)
    :noindex:

    Updates the status of a biographic validation.

    **Authorization**: :todo:`To be defined`

    :param str biographicValidationID: The ID of the biographic.
    :param status: The status of the biographic validation, e.g. 'ready' to validate.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error, and in case of success the biographic validation status.

.. py:function:: readBiographicValidationStatus(biographicID, options)
    :noindex:

    Retrieve the status of a biographic validation.

    **Authorization**: :todo:`To be defined`

    :param str biomgraphicValidationID: The ID of the biographic.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error, and in case of success the biographic validation status and metadata.

----------

Filter
""""""

The "filter" parameter used in "read" calls is used to provide a set of
identifiers that limit the amount of data that is returned.
It is often the case that the whole data set is not required, but instead,
a subset of that data.
Where possible, existing standards based identifiers should be used for the
attributes to retrieve.

E.g. For surname/familyname, use OID 2.5.4.4 or id-at-surname.

Some calls may require new filter attributes to be defined.  E.g. when
retrieving biometric data, the caller may only want the meta data about
that biometric, rather than the actual biometric data.

Options
"""""""

.. list-table:: Enrolment Services Options
    :header-rows: 1
    :widths: 25 75

    * - Name
      - Description

    * - ``transactionID``
      - A string provided by the client application to identity the request being submitted.
        It is optional in most cases. When provided, it can be used for tracing and debugging.

Data Model
""""""""""

.. list-table:: Enrolment Data Model
    :header-rows: 1
    :widths: 25 50 25

    * - Type
      - Description
      - Example

    * - Person
      - Person who is known to an identity assurance system.
      - :todo:`TBD`

    * - Document Data
      - a dictionary (list of names and values) giving the document data of interest for the document services.
      - :todo:`TBD`

    * - Biometric Data
      - Digital representation of biometric characteristics.
        All images can be passed by value (image buffer is in the request) or by reference (the address of the
        image is in the request).
        All images are compliant with ISO 19794. ISO 19794 allows multiple encoding and supports additional
        metadata specific to fingerprint, palmprint, portrait or iris.
      - Finger print, portrait, iris

    * - Biographic Data
      - a dictionary (list of names and values) giving the biographic data of interest for the biographic services.
      - :todo:`TBD`
