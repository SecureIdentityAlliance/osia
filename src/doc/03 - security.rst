
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
    distinguished from a general purpose read or write for proper segregation.

Scopes should be less than 20 characters when possible to limit the size of the bearer token.

Scopes
""""""

The following table is a summary of all scopes defined in OSIA.

.. table:: Scopes List
    :class: longtable
    :widths: 80 80
    
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
    Partial Update Enrollment           ``enroll.write``
    Finalize Enrollment                 ``enroll.write``
    Delete Enrollment                   ``enroll.write``
    Find Enrollments                    ``enroll.read``
    Send Buffer                         ``enroll.buf.write``
    Get Buffer                          ``enroll.buf.read``
    ----------------------------------- -----------------------------------------------
    **Population Registry Services**
    -----------------------------------------------------------------------------------
    Find Persons                        ``pr.person.read``
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
    Update Encounter Status             ``abis.encounter.write``
    update Encounter Galleries          ``abis.encounter.write``
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
    Find Credentials                    ``cms.credential.read``
    Read Credential                     ``cms.credential.read``
    Suspend Credential                  ``cms.credential.write``
    Unsuspend Credential                ``cms.credential.write``
    Revoke Credential                   ``cms.credential.write``
    Set Credential Status               ``cms.credential.write``
    Find Credential Profiles            ``cms.profile.read``
    ----------------------------------- -----------------------------------------------
    **ID Usage** (Work in progress)
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

Privacy by Design
-----------------

*Privacy by design* is a founding principle of the OSIA initiative.

The OSIA API is designed to support the protection of private citizens' Personal Identifiable Information (PII).

The protection of PII data is a central design concern for all identity based systems regardless of where these are based. 

PII data does not recognize geographical boundaries; it moves across systems and jurisdictions.
Similarly, the OSIA initiative is not geographically limited. OSIA takes its strong reference
point from the European Union’s GDPR regulation because this is considered by many as a best
practice approach. GDPR anticipates the possible adverse consequences from the mobility of PII
whether inside or outside the EU.

The General Data Protection Regulation (GDPR) is quite recent. It was introduced across the EU in 2016,
before reaching its full legal effect in 2018. It is adopted by all EU governments and carries
direct regulatory and legal force for any organization handling Personal Identifiable Information (PII),
either in the EU or in connection with EU citizens or residents. Compliance failure in respect
of GDPR carries significant financial penalties, reflecting the rights of individuals and groups,
as well as the importance of the issue.

GDPR is not the only defined standard, but it is seen as a best practice one. It is exemplary approach
for the safeguarding of PII; but, it should also be seen as a safeguard for a system owner/operator's
interests. It is a major driver for government leadership in Identity Management is to prevent identity fraud.

Privacy for end-to-end systems
""""""""""""""""""""""""""""""

For privacy the bigger goal is to protect PII across the full reach of ID systems.
The OSIA API is a fundamental part and principle of the building process, providing definitions
of how components are connected.

This is a part of a wider story. An end-to-end solution making use of the OSIA API should
address three specific areas of concern for PII.

Correct implementation of the API definition
''''''''''''''''''''''''''''''''''''''''''''

PII data flows through systems. API based connectivity between functional components is by definition
a way of sharing information, which will focus mostly on PII. The OSIA API defines what
should happen between application endpoints involving OSIA framework components.
It defines content and a minimum acceptable security standard for implementation.

PII safeguards within the components connected by the APIs
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

The API concept is built around functional components: the sub-systems for Identity Management.

As well as the correct implementation or use of the appropriate API, a component should also
meet PII requirements while this is present within the component. Such internal component
design and PII behavior is the responsibility of the component supplier.

The customer architect responsible for an API connected solution should therefore ensure
that the internal logic of an individual component is itself GDPR compliant.
The API concept cannot itself provide any guarantee that components are designed with
the same or sufficient internal levels of PII safeguards. What the API can do is to
preserve this level of trust and prevent the creation of new vulnerabilities between these components.

The workflow connecting components in an OSIA enabled solution
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

OSIA provides a model for an open architecture. An end-to-end identity system may use some,
or all of the OSIA components. It may use additional components to move data through the system.
Wherever the system uses components to move data that are not covered by the OSIA framework
definition then these should support end-to-end security with the same objective of GDPR compliance.

PII actors
""""""""""

The GDPR approach provides simple definitions.

- PII is a very wide category of information. It can be a name, a photo, a biometric, an email
  address, bank details, social media postings, medical data, and even an IP address;
- The PII data belongs to a Data Subject who is a natural person that might identified directly
  or indirectly using the PII;
- The usage, rules, and means of processing PII are determined by a Data Controller
  (e.g. the Government agency);
- The data is processed by a Data Processor.

When a government department acts as owner of an ID system then it is a Data Controller.
It may also act as the Data Processor if it operates this system 'in house'.

However, in today's commercial world the Data Controller is equally likely to delegate some processing
to a data center or to a business service for all or part of the system. In this case these delegated
parties are Data Processors, and they also subject to the PII considerations.

Suppliers of the systems purchased and commissioned by Data Controllers, and operated by
Data Processors are not directly subject to the regulation.

Data subject rights
"""""""""""""""""""

A GDPR data subject has several rights that should be reflected throughout the wider ID systems architecture.

The right to be forgotten
'''''''''''''''''''''''''

A subject may ask for her data to be deleted.

Depending on the purpose and the authority of the system this right may be restricted or blocked,
however the deletion of non-essential PII data may be a requirement according to some local laws.
The Data Controller should be able to justify why specific items of PII need to be retained
against the subject’s wishes, and when there is no reason for retention then the automated
purging of unnecessary data is generally recommended.

*An example impact of this for API usage is where an enrolment client holds enrollee data
until receiving a response via the API from the enrollment server to the effect that any
client stored data can be deleted. The Data Processor operating the client is responsible
to ensure this deletion is systematically applied. Typically this may be done with a
configuration in the component product used.*

Privacy by design
'''''''''''''''''

Systems should be designed to limit data collection, retention and accessibility.

This applies equally to APIs as to the system components themselves. No more data should be
passed over an API than is required. A component passing or receiving data should consider
how to minimize what new PII it collects, shares, and stores. The Data Controller should
know by design what data is held and where; as well as which APIs are sharing what data.

*An example of this principle for API usage can be where a credential management system
receives PII over an API for credential production, then deletes the PII once the document
is produced successfully. The system may limit its retained data to production audit data.
A credential management system with a different set of responsibilities defined by the Data
Controller may justify the retention of a wider set of PII, which might be replicated
elsewhere in the system. A subject might ask to know where this data sits. The Controller
should be able to tell the subject, and the Processor able to prove it.*

Breach notifications
''''''''''''''''''''

Supervisory powers vary globally. In the EU organizations have to notify their national
supervisory authority in the event of a discovered data breach involving PII.
They are given a 72 hour period to do this after becoming aware of the breach.
The purpose of this notice period is to allow the organization to determine the nature
and the impact of the data breach.

Data subjects have the right to be informed about data breaches involving their personal data.

By following the *Privacy by Design* approach, detection and data exposure can be assessed
more accurately and quickly. Data is typically in transit between sub-systems, then at rest
or in use within a given sub-system. When correctly implemented the OSIA API concept provides
assurance against breaches at the API in-transit level. Combined with the knowledge of what
data is stored, and where, this Privacy by Design approach assists in the detection of breaches.

*At the time of GDPR's introduction the biggest issuing facing most organizations was
not the implementation of new controls, but the discovery of where and what data was in
their possession. The made it very difficult to know if data was ever compromised.*

Risk and impact assessments
'''''''''''''''''''''''''''

Looking at systems overall an organization has to perform a privacy impact assessment.

This describes what PII is collected, and how this is maintained, protected, and shared.
This may be done as part of a wider ISO 27000 process including risk assessment,
but this is not mandatory.

Today most providers of components within the OSIA framework will provide such a privacy
impact assessment statement for their products, including the GDPR controls in that product.

Taken together with the OSIA API specification then these assessments can be compiled
to an overall statement of system PII compliance.

Consent
'''''''

Systems that deal with identity as their core subject matter may not be legally required
to obtain consent for the capture and use of PII data. However, in this service-centric
world more and more transactional and contextual data is captured, so this should not be
assumed. If this data is to be collected then organizations have to obtain valid and
explicit consent from the individuals.

The organizations must also be able to prove that they have gotten consent, not forgetting
that in the EU individuals may withdraw their consent.

In the EU additional safeguards apply, where parental consent is required if personal data
is to be collected about children under the age of 16.

An API usually indicates that the use or status of data is changing, so it should always
be considered. Passing PII over an API requires that the consent covers the scope of this
data sharing.

*An example of this situation might be where an enrolment system captures biometric data
to be loaded to a credential using an API. The Data Controller later decides that the
same captured data will be passed via a new API to a biometric matching system.
Both the Data Controller and Processor might find that they are processing this data
contrary to the principle of consent. If consent matters in this case then the introduction
of the new API may alert the user to a change of use. This is not to say that such changes
only happen where APIs are concerned, but the OSIA API framework does represent different
functions across Identity Management, and therefore indicates that consent may be a
relevant consideration.*

Data portability
''''''''''''''''

The portability of requirement was conceived for both transparency and commercial reasons.

PII held should be usable by the Data Subject upon request. For privacy it may be held
encrypted in the Data Processor system, but must be provided in a structured and commonly
useable format to the Data Subject under reasonable terms of access.

*An example scenario might be where a Data Subject wishes to have a copy of a child's birth
record in a printed format or a format recognized by a third party. The concept of data
portability may in some cases be implemented by a report service, or in some cases use an
OSIA API to support the retrieval of personal attribute data to meet this demand.*

What should OSIA API implementors do to prepare for safe PII?
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

1. Appoint someone as the organization’s own GDPR or PII data expert. Someone who understands
   the Data Controller business requirements, and knows the technologies likely to be used for
   data processing.
2. GDPR is a good example of best practice in PII Management, but it is vital to understand
   the current local regulatory environment. Local existing laws and regulations take
   precedence unless subject to GDPR, and even then local laws may be stricter.
3. Use the OSIA API specification to understand the security organization of functional systems
   that might be needed and document an overall assessment of the PII privacy risk.
   Pay particular attention to sensitive data, and to the aggregation of PII.
4. Ensure that component suppliers understand and support the principles of good PII management,
   or GDPR. Most suppliers provide a description of how this is enforced in their products or
   systems. They may even provide a user manual and training for this function.
5. Document the design and lifecycle of data in the end-to-end system. The OSIA API
   Specification will help with this. It does not provide the full PII story, but it does
   provide the basis for the parts between components that the customer or its systems
   integrator will be responsible for.
6. Consider the Data Subject consent requirements, based on the functions that subject
   data will be subject to.
7. If the role is Data Controller, but not Data Processor then ensure that the organization
   used for Data Processing can understand and meet the guidelines for PII protection.
8. Remember that good planning and execution are essential, but it might be asked to prove
   correct operation. Systems logs and audit data should be available. This should include
   API usage to indicate where data has been transferred.



