
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

.. py:function:: verifyIdentity(UIN, [IDAttribute])
    :noindex:

    Verify Identity based on UIN and set of Identity Attributes (biometric data, credential, etc.)

    **Authorization**: :todo:`To be defined`

    :param str UIN: The person's UIN
    :param list[str] IDAttribute: A list of list of pair (name,value) requested
    :return: Y or N
    
    In case of error (unknown attributes, unauthorized access, etc.) the value is replaced with an error

.. py:function:: identify([inIDAttribute], [outIDAttribute])
    :noindex:

    Identify a person based on a set of Identity Attributes (biometric data, credential, etc.)

    **Authorization**: :todo:`To be defined`

    :param list[str] inIDAttribute: A list of list of pair (name,value) requested
    :param list[str] outIDAttribute: A list of list of attribute names requested
    :return: Y or N
    
    In case of error (unknown attributes, unauthorized access, etc.) the value is replaced with an error

.. py:function:: readAttributes(UIN, names)
    :noindex:

    Read person attributes.

    **Authorization**: :todo:`To be defined`

    :param str UIN: The person's UIN
    :param list[str] names: The names of the attributes requested
    :return: a list of pair (name,value). In case of error (unknown attributes, unauthorized access, etc.)
        the value is replaced with an error

.. py:function:: readAttributeSet(UIN, setName)
    :noindex:

    Read person attributes corresponding to a predefined set name.

    **Authorization**: :todo:`To be defined`

    :param str UIN: The person's UIN
    :param str setName: The name of predefined attributes set name
    :return: a list of pair (name,value). In case of error (unknown attributes, unauthorized access, etc.)
        the value is replaced with an error

