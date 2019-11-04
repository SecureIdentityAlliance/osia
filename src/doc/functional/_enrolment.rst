
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

.. py:function:: getPerson(personID, options)
    :noindex:

    Retrieve the attributes of a person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
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

.. py:function:: createCredentialIssuanceRequest(personID, credentialProfileID, options)
    :noindex:

    Request issuance of a smart card / mobile identity.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str credentialProfileID: The ID of the credential profile to issue to the person.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error.  In the case of success, an issuance identifier.

.. py:function:: getCredentialIssuanceRequest(issuanceID, options)
    :noindex:

    Retrieve the attributes/status of an issuance.

    **Authorization**: :todo:`To be defined`

    :param str issuanceID: The ID of the issuance.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error, and in case of success the issuance data/status.

----------

.. py:function:: createPersonDocument(personID, documentID, documentData, options)
    :noindex:

    Add a new document for to a person.  This will trigger a document validation process.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str documentID: The ID of the document.
    :param documentData: The content and attributes of the document to be validated.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error.  In the case of success, a document validation identifier.

.. py:function:: getDocumentValidationStatus(documentValidationID, options)
    :noindex:

    Retrieve the status of a document validation.

    **Authorization**: :todo:`To be defined`

    :param str documentValidationID: The ID of the document.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error, and in case of success the document validation status.

.. py:function:: createPersonBiometric(personID, biometricID, biometricData, options)
    :noindex:

    Add a new biometric for to a person.  This will trigger a biometric validation process.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str documentID: The ID of the biometric data.
    :param documentData: The content and attributes of the biometric to be validated.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error.  In the case of success, a biometric validation identifier.

.. py:function:: getBiometricValidationStatus(biometricValidationID, options)
    :noindex:

    Retrieve the status of a biometric validation.

    **Authorization**: :todo:`To be defined`

    :param str biometricValidationID: The ID of the biometric data.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error, and in case of success the biometric validation status.

.. py:function:: createPersonBiographic(personID, biometricID, biometricData, options)
    :noindex:

    Add a new biographic for to a person.  This will trigger a biographic validation process.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str documentID: The ID of the biographic data.
    :param documentData: The content and attributes of the biographic to be validated.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error.  In the case of success, a biographic validation identifier.

.. py:function:: getBiographicValidationRequest(biographicValidationID, options)
    :noindex:

    Retrieve the attributes/status of a biographic validation.

    **Authorization**: :todo:`To be defined`

    :param str biographicValidationID: The ID of the biographic data.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error, and in case of success the biographic validation status.

Options
"""""""

.. list-table:: Population Registry Services Options
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
