
Credential Services
-------------------

This interface describes services to manage credentials and credential
requests in the context of an identity system.

Services
""""""""

.. py:function:: createCredentialRequest(personID, credentialProfileID, additionalData, transactionID)
    :noindex:

    Request issuance of a secure credential.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str credentialProfileID: The ID of the credential profile to issue to the person.
    :param dict additionalData: Additional data relating to the requested credential profile,
        e.g. credential lifetime if overriding default, delivery addresses, etc.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.  In the case of success, a credential request identifier.

.. py:function:: readCredentialRequest(credentialRequestID, attributes, transactionID)
    :noindex:

    Retrieve the data/status of a credential request.

    **Authorization**: :todo:`To be defined`

    :param str credentialRequestID: The ID of the credential request.
    :param set attributes: The (optional) set of required attributes to retrieve.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error, and in case of success the issuance data/status.

.. py:function:: updateCredentialRequest(credentialRequestID, additionalData, transactionID)
    :noindex:

    Update the requested issuance of a secure credential.

    **Authorization**: :todo:`To be defined`

    :param str credentialRequestID: The ID of the credential request.
    :param string transactionID: The client generated transactionID.
    :param dict additionalData: Additional data relating to the requested credential profile,
        e.g. credential lifetime if overriding default, delivery addresses, etc.
    :return: a status indicating success or error.

.. py:function:: deleteCredentialRequest(credentialRequestID, transactionID)
    :noindex:

    Delete/cancel the requested issuance of a secure credential.

    **Authorization**: :todo:`To be defined`

    :param str credentialRequestID: The ID of the credential request.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.

----------

.. py:function:: findCredentials(expressions, transactionID)
    :noindex:

    Retrieve a list of credentials that match the passed in search criteria.

    **Authorization**: :todo:`To be defined`

    :param list[(str,str,str)] expressions: The expressions to evaluate. Each
        expression is described with the attribute's name, the operator
        (one of ``<``, ``>``, ``=``, ``>=``, ``<=``) and the attribute value.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error, in the case of success the
        list of matching credentials.

.. py:function:: readCredential(credentialID, attributes, transactionID)
    :noindex:

    Retrieve the attributes/status of an issued credential.  A wide range of
    information may be returned, dependant on the type of credential that was
    issued, smart card, mobile, passport, etc.

    **Authorization**: :todo:`To be defined`

    :param str credentialID: The ID of the credential.
    :param set attributes: The (optional) set of required attributes to retrieve.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error, in the case of success the
        requested data will be returned.

.. py:function:: suspendCredential(credentialID, additionalData, transactionID)
    :noindex:

    Suspend an issued credential.  For electronic credentials this will suspend any
    PKI certificates that are present.

    **Authorization**: :todo:`To be defined`

    :param str credentialID: The ID of the credential.
    :param dict additionalData: Additional data relating to the request,
        e.g. reason for suspension.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: unsuspendCredential(credentialID, additionalData, transactionID)
    :noindex:

    Unsuspend an issued credential.  For electronic credentials this will unsuspend any
    PKI certificates that are present.

    **Authorization**: :todo:`To be defined`

    :param str credentialID: The ID of the credential.
    :param dict additionalData: Additional data relating to the request,
        e.g. reason for unsuspension.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: revokeCredential(credentialID, additionalData, transactionID)
    :noindex:

    Revoke an issued credential.  For electronic credentials this will revoke any
    PKI certificates that are present.

    **Authorization**: :todo:`To be defined`

    :param str credentialID: The ID of the credential.
    :param dict additionalData: Additional data relating to the request,
        e.g. reason for revocation.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.

----------

.. py:function:: findCredentialProfiles(expressions, transactionID)
    :noindex:

    Retrieve the data/status of a credential request.

    **Authorization**: :todo:`To be defined`

    :param list[(str,str,str)] expressions: The expressions to evaluate. Each expression is described with the attribute's name, the operator (one of ``<``, ``>``, ``=``, ``>=``, ``<=``, ``!=``) and the attribute value
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error, and in case of success the matching credential profile list.


Attributes
""""""""""

The "attributes" parameter used in "read" calls is used to provide a set of
identifiers that limit the amount of data that is returned.
It is often the case that the whole data set is not required, but instead,
a subset of that data.
@@ -128,7 +128,7 @@ attributes to retrieve.

E.g. For surname/familyname, use OID 2.5.4.4 or id-at-surname.

Some calls may require new attributes to be defined.  E.g. when
retrieving biometric data, the caller may only want the meta data about
that biometric, rather than the actual biometric data.
