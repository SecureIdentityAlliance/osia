
Credential Services
-------------------

This interface describes services to manage credentials and credential
requests in the context of an identity system.

Services
""""""""

.. py:function:: createCredentialRequest(personID, credentialProfileID, additionalData, transactionID)
    :noindex:

    Request issuance of a secure credential.

    **Authorization**: ``cms.request.write``

    :param str personID: The ID of the person.
    :param str credentialProfileID: The ID of the credential profile to issue to the person.
    :param dict additionalData: Additional data relating to the requested credential profile,
        e.g. credential lifetime if overriding default, delivery addresses, etc.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.  In the case of success, a credential request identifier.

.. py:function:: readCredentialRequest(credentialRequestID, attributes, transactionID)
    :noindex:

    Retrieve the data/status of a credential request.

    **Authorization**: ``cms.request.read``

    :param str credentialRequestID: The ID of the credential request.
    :param set attributes: The (optional) set of required attributes to retrieve.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error, and in case of success the issuance data/status.

.. py:function:: updateCredentialRequest(credentialRequestID, additionalData, transactionID)
    :noindex:

    Update the requested issuance of a secure credential.

    **Authorization**: ``cms.request.write``

    :param str credentialRequestID: The ID of the credential request.
    :param string transactionID: The client generated transactionID.
    :param dict additionalData: Additional data relating to the requested credential profile,
        e.g. credential lifetime if overriding default, delivery addresses, etc.
    :return: a status indicating success or error.

.. py:function:: updateCredentialRequestMailingAddress(credentialRequestID, deliveryAddress, transactionID)
    :noindex:

    Update the delivery address of a credential request.

    **Authorization**: ``cms.request.write``

    :param str credentialRequestID: The ID of the credential request.
    :param string transactionID: The client generated transactionID.
    :param dict deliveryAddress: Delivery address attributes, e.g. address1, city, state, postalCode, country, etc.
    :return: a status indicating success or error.

.. py:function:: updateCredentialRequestPriority(credentialRequestID, priority, transactionID)
    :noindex:

    Update the priority of a credential request.

    **Authorization**: ``cms.request.write``

    :param str credentialRequestID: The ID of the credential request.
    :param string transactionID: The client generated transactionID.
    :param int priority: New priority to be applied to the credential request.
    :return: a status indicating success or error.

.. py:function:: holdCredentialRequest(credentialRequestID, reason, comment, transactionID)
    :noindex:

    Place the requested issuance of a secure credential on hold.

    **Authorization**: ``cms.request.write``

    :param str credentialRequestID: The ID of the credential request.
    :param string reason: The reason for the hold.
    :param string comment: Comments related to the hold, optional.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: releaseCredentialRequest(credentialRequestID, reason, comment, transactionID)
    :noindex:

    Release the hold on the requested issuance of a secure credential.

    **Authorization**: ``cms.request.write``

    :param str credentialRequestID: The ID of the credential request.
    :param string reason: The reason for releasing the hold.
    :param string comment: Comments related to the release, optional.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: cancelCredentialRequest(credentialRequestID, transactionID)
    :noindex:

    Cancel the requested issuance of a secure credential.

    **Authorization**: ``cms.request.write``

    :param str credentialRequestID: The ID of the credential request.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.

----------

.. py:function:: findCredentials(expressions, transactionID)
    :noindex:

    Retrieve a list of credentials that match the passed in search criteria.

    **Authorization**: ``cms.credential.read``

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

    **Authorization**: ``cms.credential.read``

    :param str credentialID: The ID of the credential.
    :param set attributes: The (optional) set of required attributes to retrieve.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error, in the case of success the
        requested data will be returned.

.. py:function:: suspendCredential(credentialID, additionalData, transactionID)
    :noindex:

    Suspend an issued credential.  For electronic credentials this will suspend any
    PKI certificates that are present.

    **Authorization**: ``cms.credential.write``

    :param str credentialID: The ID of the credential.
    :param dict additionalData: Additional data relating to the request,
        e.g. reason for suspension.
    :param string transactionID: The (optional) client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: unsuspendCredential(credentialID, additionalData, transactionID)
    :noindex:

    Unsuspend an issued credential.  For electronic credentials this will unsuspend any
    PKI certificates that are present.

    **Authorization**: ``cms.credential.write``

    :param str credentialID: The ID of the credential.
    :param dict additionalData: Additional data relating to the request,
        e.g. reason for unsuspension.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: revokeCredential(credentialID, additionalData, transactionID)
    :noindex:

    Revoke an issued credential.  For electronic credentials this will revoke any
    PKI certificates that are present.

    **Authorization**: ``cms.credential.write``

    :param str credentialID: The ID of the credential.
    :param dict additionalData: Additional data relating to the request,
        e.g. reason for revocation.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: setCredentialStatus(credentialID, status, reason, requester, comment, transactionID)
    :noindex:

    Change the status of a credential. This is an extension of the revoke/suspend services,
    supporting more statuses and transitions.

    **Authorization**: ``cms.credential.write``

    :param str credentialID: The ID of the credential.
    :param string status: The new status of the credential
    :param string reason: A text describing the cause of the change of status
    :param string requester: The client generated transactionID.
    :param string comment: A free text comment
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.

----------

.. py:function:: findCredentialProfiles(expressions, transactionID)
    :noindex:

    Retrieve a list of credential profils that match the passed in search criteria

    **Authorization**: ``cms.profile.read``

    :param list[(str,str,str)] expressions: The expressions to evaluate. Each expression is described with the attribute's name, the operator (one of ``<``, ``>``, ``=``, ``>=``, ``<=``, ``!=``) and the attribute value
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error, and in case of success the matching credential profile list.


Attributes
""""""""""

The "attributes" parameter used in "read" calls is used to provide a set of
identifiers that limit the amount of data that is returned.
It is often the case that the whole data set is not required, but instead,
a subset of that data.

Some calls may require new attributes to be defined.  E.g. when
retrieving biometric data, the caller may only want the meta data about
that biometric, rather than the actual biometric data.

Data Model
""""""""""

.. list-table:: Credential Data Model
    :header-rows: 1
    :widths: 25 50 25

    * - Type
      - Description
      - Example

    * - Credential
      - The attributes of the credential itself

        The proposed transitions for the status are represented below. It can be adapted if needed.

        .. uml::
            :scale: 30%

            [*] --> new
            new --> active: issue
            active -> suspended: suspend
            suspended -> active: unsuspend
            active --> revoked
            suspended --> revoked

      - ID, status, dates, serial number

    * - Biometric Data
      - Digital representation of biometric characteristics.
      
        All images can be passed by value (image buffer is in the request) or by reference (the address of the
        image is in the request).
        All images are compliant with ISO 19794. ISO 19794 allows multiple encoding and supports additional
        metadata specific to fingerprint, palmprint, portrait, iris or signature.

        A biometric data can be associated to no image or a partial image if it includes information about
        the missing items (example: one finger may be amputated on a 4 finger image)
      - fingerprint, portrait, iris, signature

    * - Biographic Data
      - a dictionary (list of names and values) giving the biographic data of interest for the biometric services.
      - first name, last name, date of birth, etc.

    * - Request Data
      - a dictionary (list of names and values) for data related to the request itself.
      - Type of credential, action to execute, priority

.. uml::
    :caption: Credential Data Model
    :scale: 50%

    class Credential {
        string credentialID;
        string status;
        string personID;
        string serialNumber;
        ...
    }

    class CredentialRequest {
        string CredentialRequestID;
        string status;
        string personID;
    }
    CredentialRequest . Credential

    class BiographicData {
        string firstName;
        string lastName;
        date dateOfBirth;
        ...
    }
    BiographicData -o CredentialRequest

    class BiometricData {
        byte[] image;
        URL imageRef;
        byte[] template;
    }
    CredentialRequest o-- "*" BiometricData

    class RequestData {
        int priority;
        string credentialProfileID;
        string requestType;
        ...
    }
    RequestData --o CredentialRequest

