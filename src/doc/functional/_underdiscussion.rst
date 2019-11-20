
Under discussion
----------------

Services
""""""""

.. py:function:: listCredentialProfiles(filter, transactionID)
    :noindex:

    Retrieve the list of credential profiles.

    **Authorization**: :todo:`To be defined`

    :param set filter: The (optional) set of required attributes to retrieve.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error, and in case of success the credential profile list.

.. py:function:: readCredentialProfile(credentialProfileID, filter, transactionID)
    :noindex:

    Retrieve the credential profile.

    **Authorization**: :todo:`To be defined`

    :param str credentialProfileID: The ID of the credential profile.
    :param set filter: The (optional) set of required attributes to retrieve.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error, and in case of success the credential profile.

----------

.. py:function:: createDocument(personID, documentID, documentData, transactionID)
    :noindex:

    Add a new document for a person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str documentID: The ID of the document.
    :param documentData: The content and attributes of the document.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error.  In the case of success, a document identifier.

.. py:function:: readDocument(documentID, filter, transactionID)
    :noindex:

    Retrieve document data.

    **Authorization**: :todo:`To be defined`

    :param str documentID: The ID of the document.
    :param set filter: The (optional) set of required attributes to retrieve.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error, and in case of success the document data.

.. py:function:: updateDocument(documentID, documentData, transactionID)
    :noindex:

    Update a document for a person.

    **Authorization**: :todo:`To be defined`

    :param str documentID: The ID of the document.
    :param documentData: The content and attributes of the document, this can be partial data.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: deleteDocument(documentID, transactionID)
    :noindex:

    Delete a document for a person.

    **Authorization**: :todo:`To be defined`

    :param str documentID: The ID of the document.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: updateDocumentValStatus(documentID, status, transactionID)
    :noindex:

    Updates the status of a document validation.

    **Authorization**: :todo:`To be defined`

    :param str documentID: The ID of the document.
    :param status: The status of the document validation, e.g. 'ready' to validate.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: readDocumentValStatus(documentID, transactionID)
    :noindex:

    Retrieve the status of a document validation.

    **Authorization**: :todo:`To be defined`

    :param str documentID: The ID of the document.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error, and in case of success the document validation status and its metadata.

----------

.. py:function:: createBiometric(personID, biometricID, biometricData, transactionID)
    :noindex:

    Add a new biometric for a person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str biometricID: The ID of the biometric.
    :param biometricData: The content and attributes of the biometric.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error.  In the case of success, a biometric identifier.

.. py:function:: readBiometric(biometricID, filter, transactionID)
    :noindex:

    Retrieve biometric data.

    NOTE - do we want this method in the system?  We don't beleive that this data should be
    retrievable.  A separate method is provided for reading enrolled biometric metadata (see below).

    **Authorization**: :todo:`To be defined`

    :param str biometricID: The ID of the biometric.
    :param set filter: The (optional) set of required attributes to retrieve.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error, and in case of success the biometric data.

.. py:function:: readBiometricMetadata(biometricID, filter, transactionID)
    :noindex:

    Retrieve biometric data.

    **Authorization**: :todo:`To be defined`

    :param str biometricID: The ID of the biometric.
    :param set filter: The (optional) set of required attributes to retrieve.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error, and in case of success the biometric metadata.

.. py:function:: updateBiometric(biometricID, biometricData, transactionID)
    :noindex:

    Update a biometric for a person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str biometricID: The ID of the biometric.
    :param biometricData: The content and attributes of the biometric, this can be partial data.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: deleteBiometric(biometricID, transactionID)
    :noindex:

    Delete a biometric for a person.

    **Authorization**: :todo:`To be defined`

    :param str biometricID: The ID of the biometric.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: updateBiometricValStatus(biometricID, status, transactionID)
    :noindex:

    Updates the status of a biometric validation.

    **Authorization**: :todo:`To be defined`

    :param str biometricID: The ID of the biometric.
    :param status: The status of the biometric validation, e.g. 'ready' to validate.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error, and in case of success the biometric validation status.

.. py:function:: readBiometricValStatus(biometricID, transactionID)
    :noindex:

    Retrieve the status of a biometric validation.

    **Authorization**: :todo:`To be defined`

    :param str biometricID: The ID of the biometric.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error, and in case of success the biometric validation status and metadata.

----------

.. py:function:: createBiographic(personID, biographicID, biographicData, transactionID)
    :noindex:

    Add a new biographic for a person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str biographicID: The ID of the biographic.
    :param biographicData: The content and attributes of the biographic.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error.  In the case of success, a biographic identifier.

.. py:function:: readBiographic(biographicID, filter, transactionID)
    :noindex:

    Retrieve biographic data.

    **Authorization**: :todo:`To be defined`

    :param str biographicID: The ID of the biographic.
    :param set filter: The (optional) set of required attributes to retrieve.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error, and in case of success the biographic data.

.. py:function:: updateBiographic(biographicID, biographicData, transactionID)
    :noindex:

    Update a biographic for a person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str biographicID: The ID of the biographic.
    :param biographicData: The content and attributes of the biographic, this can be partial data.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: deleteBiographic(biographicID, transactionID)
    :noindex:

    Delete a biographic for a person.

    **Authorization**: :todo:`To be defined`

    :param str biographicID: The ID of the biographic.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: updateBiographicValStatus(biographicID, status, transactionID)
    :noindex:

    Updates the status of a biographic validation.

    **Authorization**: :todo:`To be defined`

    :param str biographicID: The ID of the biographic.
    :param status: The status of the biographic validation, e.g. 'ready' to validate.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error, and in case of success the biographic validation status.

.. py:function:: readBiographicValStatus(biographicID, transactionID)
    :noindex:

    Retrieve the status of a biographic validation.

    **Authorization**: :todo:`To be defined`

    :param str biographicID: The ID of the biographic.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error, and in case of success the biographic validation status and metadata.

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

Transaction ID
""""""""""""""

The "transactionID" is a string provided by the client application to identity
the request being submitted. It is optional in most cases. When provided, it
can be used for tracing and debugging.


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
      - fingerprint, portrait, iris

    * - Biographic Data
      - a dictionary (list of names and values) giving the biographic data of interest for the biographic services.
      - :todo:`TBD`
