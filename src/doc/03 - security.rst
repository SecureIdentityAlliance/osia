
Security & Privacy
==================

Introduction
------------

:todo:`Insert diagram of security & privacy features`

Virtual UIN
-----------

:todo:`Explain: using a different UIN in each subsystem - no direct/easy
links between the records in different subsystems`

Authorization
-------------

.. comment: Source of inspiration: https://opensource.zalando.com/restful-api-guidelines/#security

Because OSIA is a set of interfaces/API and not a full system, this chapter describes only how to secure those API,
through the usage of standard JWT, and not how to generate and protect such tokens, nor how to secure the full system.

Securing the API is one mandatory step on the way to a secure system, but securing a full system includes
more than just that: hardware & software components, processes & methodology, audit, etc.
that are not in the scope of this document.

Principles
""""""""""

Securing OSIA services is implemented with the following principles:

- Rely on JWT: "JSON Web Token (JWT) is a compact, URL-safe means of representing claims to be transferred between two parties"
  It can be "digitally signed or integrity protected with a Message Authentication Code (MAC) and/or encrypted".
  [:rfc:`7519`]
- Tokens of type "Bearer Token" are used. [:rfc:`6750`]
  The generation and management of those tokens are not in the scope of this document.
- Validating the token is the responsibility of the service implementation, with the help of components
  not described in this document (PKI, authorization server, etc.)
- The service implementations are responsible for extracting information from the token
  and give access or not to the service according to the claims contained in the token
  and the *scope* defined for each service in this document.
- The service implementations are free to change the security scheme used, for instance to use
  OAuth2 or OpenID Connect, if it fits the full system security policy. **Scopes must not be changed**.
- All HTTP exchanges must be secured with TLS. Mutual authentication is not mandatory.

.. note::

    The added use of peer-to-peer payload encryption - e.g. to protect biometric data - is
    not in the scope of this document.

.. note::

    OSIA does not define ACL (Access Control List) to protect the access to a subset of the data.
    This may be added in a future version.

.. warning::

    Bearer tokens are sensitive and subject to security issues if not handled properly. Please refer to
    `JSON Web Token Best Current Practices <https://tools.ietf.org/id/draft-ietf-oauth-jwt-bcp-02.html>`_
    for advice on proper implementation.
    
Rules
"""""

All scopes are named according to the following rules:

    ``application[.resource].action``

where:

- application is a key identifying the interface group listed in :ref:`chapter-interfaces`.
  Examples: ``notif``, ``pr``, ``cr``, ``abis``, etc.
- resource is a key identifying the resource. Examples: ``person``, ``encounter``, ``identity``, etc.
- action is one of:

  - ``read``: for read access to the data represented by the *resource* and managed by the *application*.
  - ``write``: for creating, updating or deleting the data.
  - or another value, for specific actions such as match or verify that need to be
    distinguished from a general purpose read or write for proper segreggation.

Scopes should be less than 20 characters when possible to limit the size of the bearer token.

Scopes
""""""

The following table is a summary of all scopes defined in OSIA.

.. table:: Scopes List
    :class: longtable
    :widths: 50 80
    
    =================================== ===============================================
    **Services**                        **Scope**
    ----------------------------------- -----------------------------------------------
    **Notification**
    -----------------------------------------------------------------------------------
    Subscribe                           ``notif.sub.write``
    List Subscription                   ``notif.sub.read``
    Unsubscribe                         ``notif.sub.write``
    Confirm                             ``notif.sub.write``
    Create Topic                        ``notif.topic.write``
    List Topics                         ``notif.topic.read``
    Delete Topic                        ``notif.topic.write``
    Publish                             ``notif.topic.publish``
    ----------------------------------- -----------------------------------------------
    **Data Access**
    -----------------------------------------------------------------------------------
    Read Person Attributes              ``pr.person.read`` or ``cr.person.read``
    Match Person Attributes             ``pr.person.match`` or ``cr.person.match``
    Verify Person Attributes            ``pr.person.verify`` or ``cr.person.verify``
    Query Person UIN                    ``pr.person.read`` or ``cr.person.read``
    Query Person List                   ``pr.person.read`` or ``cr.person.read``
    Read document                       ``pr.document.read`` or ``cr.document.read``
    ----------------------------------- -----------------------------------------------
    **UIN Management**
    -----------------------------------------------------------------------------------
    Generate UIN                        ``uin.generate``
    ----------------------------------- -----------------------------------------------
    **Enrollment Services**
    -----------------------------------------------------------------------------------
    Create Enrollment                   ``enroll.write``
    Read Enrollment                     ``enroll.read``
    Update Enrollment                   ``enroll.write``
    Delete Enrollment                   ``enroll.write``
    Find Enrollment                     ``enroll.read``
    Create Document Capture             ``enroll.doc.write``
    Read Document Capture               ``enroll.doc.read``
    Update Document Capture             ``enroll.doc.write``
    Delete Document Capture             ``enroll.doc.write``
    ----------------------------------- -----------------------------------------------
    **Population Registry Services**
    -----------------------------------------------------------------------------------
    Create Person                       ``pr.person.write``
    Read Person                         ``pr.person.read``
    Update Person                       ``pr.person.write``
    Delete Person                       ``pr.person.write``
    Merge Persons                       ``pr.person.write``
    Create Identity                     ``pr.identity.write``
    Read Identity                       ``pr.identity.read``
    Update Identity                     ``pr.identity.write``
    Partial Update Identity             ``pr.identity.write``
    Delete Identity                     ``pr.identity.write``
    Set Identity Status                 ``pr.identity.write``
    Define Reference                    ``pr.reference.write``
    Read Reference                      ``pr.reference.read``
    Read Galleries                      ``pr.gallery.read``
    Read Gallery Content                ``pr.gallery.read``
    ----------------------------------- -----------------------------------------------
    **Biometrics**
    -----------------------------------------------------------------------------------
    Create Encounter                    ``abis.encounter.write``
    Read Encounter                      ``abis.encounter.read``
    Update Encounter                    ``abis.encounter.write``
    Delete Encounter                    ``abis.encounter.write``
    Merge Encounter                     ``abis.encounter.write``
    Set Encounter Status                ``abis.encounter.write``
    Read Template                       ``abis.encounter.read``
    Read Galleries                      ``abis.gallery.read``
    Read Gallery content                ``abis.gallery.read``
    Identify                            ``abis.identify``
    Verify                              ``abis.verify``
    ----------------------------------- -----------------------------------------------
    **Credential Services**
    -----------------------------------------------------------------------------------
    Create Credential Request           ``cms.request.write``
    Read Credential Request             ``cms.request.read``
    Update Credential Request           ``cms.request.write``
    Delete Credential Request           ``cms.request.write``
    Read Credential                     ``cms.credential.read``
    Suspend Credential                  ``cms.credential.write``
    Unsuspend Credential                ``cms.credential.write``
    Cancel Credential                   ``cms.credential.write``
    ----------------------------------- -----------------------------------------------
    **ID Usage**
    -----------------------------------------------------------------------------------
    Verify ID                           ``id.verify``
    Identify                            ``id.identify``
    Read Attributes                     ``id.read``
    Read Attributes set                 ``id.set.read``
    =================================== ===============================================

REST Interface Implementation
"""""""""""""""""""""""""""""

The `OpenAPI <https://swagger.io/docs/specification/authentication/>`_ files
included in this document must be changed to:

#. Define the `security scheme <https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.3.md#securitySchemeObject>`_.
   This is done with the additional piece of code:

   .. code-block:: yaml
   
        components:
          securitySchemes:
            BearerAuth:
              type: http
              scheme: bearer
              bearerFormat: JWT

#. Apply the security scheme and define the scope (i.e. permission) for each service. Example:

   .. code-block:: yaml
   
        paths:
          /yyy:
            get:
              security:
                - BearerAuth: [id.read]	# List of scopes
              responses:
                '200':
                  description: OK
                '401':
                  description: Not authenticated (bad token)
                '403':
                  description: Access token does not have the required scope

See the different YAML files provided in :ref:`chapter-tech-specs`.

GDPR
----

:todo:`To be completed`

