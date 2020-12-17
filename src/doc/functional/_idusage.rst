
ID Usage
--------

ID Usage consists of a set of services implemented on top of identity systems to favour third parties
consumption of identity data. The services can be classified in three sets:

- Relying Party API: submitting citizen ID attributes for validation

  The purpose of the Relying Party (RP) API is to extend the use of government-issued identity to registered
  third party services. The individual will submit their ID attributes to the relying party in order to enroll
  for, or access, a particular service. The relying party will leverage the RP API to access the identity
  management system and verify the individual’s identity. In this way, external relying parties can quickly and
  easily verify individuals based on their government issued ID attributes.

  .. admonition:: Use case applications: telco enrolment

      The RP API enables a telco operator to check an individual’s identity when applying for a service contract.
      The telco relies on the government to confirm that the attributes submitted by the individual match against
      the data held in the database therefore being able to confidently identify the new subscriber. This scenario
      can be replicated across multiple sectors including banking and finance.

- Digital Credential Management API: delegating digital issuance to third parties

  The purpose of the Digital Credential Management (DCM) API is to enable external
  wallet providers to manage government issued digital credentials distribution,
  storage and usage.

  .. admonition:: Use case applications: digital driver license

      The DCM API enables individuals to request a digital driver license as a digital credential in their selected
      wallet to use for online and offline identification. The user initiates a request for digital driver license
      using the Digital Credential Distribution System (DCDS) frontend, which sends the request to the identity
      management system. The Credential Management System (CMS) then issues the digital credential by dedicated API
      endpoint of the DCDS.

- Federation API: user-initiated attributes sharing

  The purpose of the federation API is to enable the user to share their attributes with a chosen relying party using
  well-known internet protocol: OpenID Connect. The relying party benefits from the government’s verified attributes.

  .. admonition:: Use case applications: on-line registration to gambling website

      The Federation API enables individuals to log-in with their government credential (log-in/password) and share
      verified attributes ex. age (above 18) with the relying party.

Relying Party API
"""""""""""""""""

.. py:function:: verifyIdentity(Identifier, attributeSet)
    :noindex:

    Verify an Identity based on an identifier (UIN, token…) and a set of Identity Attributes. Verification is strictly
    matching all provided identity attributes to compute the global Boolean matching result.

    **Authorization**: `id.verify`

    :param str Identifier: The person's Identifier
    :param list[str] attributeSet: A set of identity attributes associated to the identifier and to be verified by the system
    :return: Y or N
    
    In case of error (unknown attributes, unauthorized access, etc.) the value is replaced with an error

.. py:function:: identify(attributeSet, outputAttributeSet)
    :noindex:

    Identify possibly matching identities against an input set of attributes. Returns an array of predefined
    datasets as described by outputAttributeSet.

    Note: This service may be limited to some specific government RPs

    **Authorization**: `id.identify`

    :param list[str] attributeSet: A list of pair (name,value) requested
    :param list[str] outputAttributeSet: An array of attributes requested
    :return: Y or N
    
    In case of error (unknown attributes, unauthorized access, etc.) the value is replaced with an error

.. py:function:: readAttributes(Identifier, outputAttributeSet)
    :noindex:

    Get a list of identity attributes attached to a given identifier.

    **Authorization**: `id.read`

    :param str Identifier: The person's Identifier
    :param list[str] outputAttributeSet: defining the identity attributes to be provided back to the caller
    :return: An array of the requested attributes

    In case of error (unknown attributes, unauthorized access, etc.) the value is replaced with an error

.. py:function:: readAttributeSet(Identifier, AttributeSetName)
    :noindex:

    Get a set of identity attributes as defined by attributeSet, attached to a given identifier.

    **Authorization**: `id.set.read`

    :param str Identifier: The person's Identifier
    :param str attributeSetName: The name of predefined attributes set name
    :return: An array of the requested attributes

    In case of error (unknown attributes, unauthorized access, etc.) the value is replaced with an error

Attribute set
"""""""""""""

When identity attributes are exchanged, they are included in an attribute set, possibly containing groups like
biographic data, biometric data, document data, contact data... This structure is extensible and may be complemented
with other data groups, and each group may contain any number of attribute name / attribute value pairs.

Attribute set name
""""""""""""""""""

Attribute sets are by definition structures with variable and optional content, hence it may be useful to pre-agree
on a given attribute set content and name between two or more systems in a given project scope.

Any string may be used to define an attribute set name, but in the scope of this specification following names are
reserved and predefined:

.. list-table::

    * - "DEFAULT_SET_01"
      - Minimum demographic data
      - | First name
        | Last name
        | DoB
        | Place of birth
    * - "DEFAULT_SET_02"
      - Minimum demographic and portrait
      - Minimum demographic data + portrait
    * - "DEFAULT_SET_EIDAS"
      - Set expected to comply with eIDAS pivotal attributes.
      - :todo:`TBD`


Output Attribute set
""""""""""""""""""""

To specify what identity attributes are expected in return when performing e.g. an identify request or a read attributes.
