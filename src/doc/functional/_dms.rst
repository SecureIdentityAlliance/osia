
Credential Management Services
-----------------



Services
""""""""

.. py:function:: createCredentialIssuanceRequest(personID, credentialProfileID, options)
    :noindex:

    Request issuance of a secure document / credential.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str credentialProfileID: The ID of the credential profile to issue to the person.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error.  In the case of success, an issuance identifier.

.. py:function:: readCredentialIssuanceRequest(issuanceID, filter, options)
    :noindex:

    Retrieve the attributes/status of an issuance.

    **Authorization**: :todo:`To be defined`

    :param str issuanceID: The ID of the issuance.
    :param set filter: A set of required attributes to retrieve.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error, and in case of success the issuance data/status.

.. py:function:: updateCredentialIssuanceRequest(issuanceID, options)
    :noindex:

    Update the requested issuance of a secure document / credential.

    **Authorization**: :todo:`To be defined`

    :param str issuanceID: The ID of the issuance.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error.

.. py:function:: deleteCredentialIssuanceRequest(issuanceID, options)
    :noindex:

    Delete the requested issuance of a secure document / credential.

    **Authorization**: :todo:`To be defined`

    :param str issuanceID: The ID of the issuance.
    :param dict options: The processing options. Supported options are transactionID.
    :return: a status indicating success or error.

