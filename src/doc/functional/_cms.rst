
Credential Services
-------------------

Services
""""""""

.. py:function:: createCredential(personID, credentialProfileID, additionalData, transactionID)
    :noindex:

    Request issuance of a secure document / credential.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str credentialProfileID: The ID of the credential profile to issue to the person.
    :param dict additionalData: Additional data relating to the requested credential profile,
        e.g. credential lifetime if overriding default, delivery addresses, etc.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.  In the case of success, an issuance identifier.

.. py:function:: readCredentialIssuance(issuanceID, filter, transactionID)
    :noindex:

    Retrieve the data/status of an issuance.

    **Authorization**: :todo:`To be defined`

    :param str issuanceID: The ID of the issuance.
    :param set filter: The (optional) set of required attributes to retrieve.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error, and in case of success the issuance data/status.

.. py:function:: updateCredential(issuanceID, additionalData, transactionID)
    :noindex:

    Update the requested issuance of a secure document / credential.

    **Authorization**: :todo:`To be defined`

    :param str issuanceID: The ID of the issuance.
    :param string transactionID: The client generated transactionID.
    :param dict additionalData: Additional data relating to the requested credential profile,
        e.g. credential lifetime if overriding default, delivery addresses, etc.
    :return: a status indicating success or error.

.. py:function:: deleteCredential(issuanceID, transactionID)
    :noindex:

    Delete/cancel the requested issuance of a secure document / credential.

    **Authorization**: :todo:`To be defined`

    :param str issuanceID: The ID of the issuance.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.

----------

.. py:function:: readCredential(credentialID, filter, transactionID)
    :noindex:

    Retrieve the attributes/status of an issued credential.  A wide range of
    information may be returned, dependant on the type of credential that was
    issued, smart card, mobile, passport, etc.

    **Authorization**: :todo:`To be defined`

    :param str credentialID: The ID of the credential.
    :param set filter: The (optional) set of required attributes to retrieve.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error, in the case of success the
        requested data will be returned.

.. py:function:: suspendCredential(credentialID, transactionID)
    :noindex:

    Suspend an issued credential.  For electronic credentials this will suspend any
    PKI certificates that are present.

    **Authorization**: :todo:`To be defined`

    :param str credentialID: The ID of the credential.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: unsuspendCredential(credentialID, transactionID)
    :noindex:

    Unsuspend an issued credential.  For electronic credentials this will unsuspend any
    PKI certificates that are present.

    **Authorization**: :todo:`To be defined`

    :param str credentialID: The ID of the credential.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: cancelCredential(credentialID, transactionID)
    :noindex:

    Cancel an issued credential.  For electronic credentials this will revoke any
    PKI certificates that are present.

    **Authorization**: :todo:`To be defined`

    :param str credentialID: The ID of the credential.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.

