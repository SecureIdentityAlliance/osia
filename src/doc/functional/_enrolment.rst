
Enrolment Services
------------------



Services
""""""""

.. py:function:: createPerson(personID, personData)
    :noindex:

    Insert a new person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person. If the person already exists for the ID an error is returned.
    :param dict personData: The person attributes.
    :return: a status indicating success or error.

.. py:function:: getPerson(personID)
    :noindex:

    Retrieve the attributes of a person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :return: a status indicating success or error and in case of success the person data.

.. py:function:: updatePerson(personID, personData)
    :noindex:

    Update a person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param dict personData: The person data.
    :return: a status indicating success or error.

.. py:function:: deletePerson(personID)
    :noindex:

    Delete a person and all their identities.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :return: a status indicating success or error.

----------

.. py:function:: createCredentialIssuanceRequest(personID, credentialProfileID)
    :noindex:

    Request issuance of a smart card / mobile identity.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str credentialProfileID: The ID of the credential profile to issue to the person.
    :return: a status indicating success or error.  In the case of success, an issuance identifier.

.. py:function:: getCredentialIssuanceRequest(issuanceID)
    :noindex:

    Retrieve the attributes/status of an issuance.

    **Authorization**: :todo:`To be defined`

    :param str issuanceID: The ID of the issuance.
    :return: a status indicating success or error, and in case of success the issuance data/status.

----------

.. py:function:: createDocumentValidationRequest(documentID, documentData)
    :noindex:

    Request validation of a document.

    **Authorization**: :todo:`To be defined`

    :param str documentID: The ID of the document.
    :param documentData: The content and attributes of the document to be validated.
    :return: a status indicating success or error.  In the case of success, a document validation identifier.

.. py:function:: getDocumentValidationRequest(documentValidationID)
    :noindex:

    Retrieve the attributes/status of a document validation.

    **Authorization**: :todo:`To be defined`

    :param str issuanceID: The ID of the issuance.
    :return: a status indicating success or error, and in case of success the document validation status.

.. py:function:: createBiometricValidationRequest(biometricID, biometricData)
    :noindex:

    Request validation of biometric data.

    **Authorization**: :todo:`To be defined`

    :param str documentID: The ID of the biometric data.
    :param documentData: The content and attributes of the biometric to be validated.
    :return: a status indicating success or error.  In the case of success, a biometric validation identifier.

.. py:function:: getBiometricValidationRequest(biometricValidationID)
    :noindex:

    Retrieve the attributes/status of a biometric validation.

    **Authorization**: :todo:`To be defined`

    :param str issuanceID: The ID of the issuance.
    :return: a status indicating success or error, and in case of success the biometric validation status.

.. py:function:: createBiographicValidationRequest(biographicID, biometricData)
    :noindex:

    Request validation of biographic data.

    **Authorization**: :todo:`To be defined`

    :param str documentID: The ID of the biographic data.
    :param documentData: The content and attributes of the biographic to be validated.
    :return: a status indicating success or error.  In the case of success, a biographic validation identifier.

.. py:function:: getBiographicValidationRequest(biographicValidationID)
    :noindex:

    Retrieve the attributes/status of a biographic validation.

    **Authorization**: :todo:`To be defined`

    :param str issuanceID: The ID of the issuance.
    :return: a status indicating success or error, and in case of success the biographic validation status.
