
Population Registry
-------------------

This interface describes services to manage a registry of the population in the context of an identity system. It is based on
the following principles:

- It supports a history of identities, meaning that a person has one identity and this identity
  has a history.
- Images can be passed by value or reference. When passed by value, they are base64-encoded.
- Existing standards are used whenever possible.
- This interface is complementary to the data access interface. The data access interface is used
  to query the persons and uses the reference identity to return attributes.

See :ref:`annex-interface-pr` for the technical details of this interface.

Services
""""""""

.. py:function:: insertPerson(personID, personData, options)
    :noindex:

    Insert a new person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person. If the person already exists for the ID an error is returned.
    :param personData: The person attributes.
    :param dict options: the processing options. Supported options are ``transactionID``.
    :return: a status indicating success or error.

.. py:function:: readPerson(personID, options)
    :noindex:

    Retrieve the attributes of a person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param dict options: the processing options. Supported options are ``transactionID``.
    :return: a status indicating success or error and in case of success the person data.

.. py:function:: updatePerson(personID, personData, options)
    :noindex:

    Update a person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param dict personData: The person data.
    :param dict options: the processing options. Supported options are ``transactionID``.
    :return: a status indicating success or error.

.. py:function:: deletePerson(personID, options)
    :noindex:

    Delete a person and all its identities.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param dict options: the processing options. Supported options are ``transactionID``.
    :return: a status indicating success or error.

----------

.. py:function:: getIdentities(personID, options)
    :noindex:

    Get all the identities of one person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param dict options: the processing options. Supported options are ``transactionID``.
    :return: a status indicating success or error, and in case of success a list of identities.

.. py:function:: insertIdentity(personID, identity, options)
    :noindex:

    Insert a new identity in a person and generate the identity ID.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param identity: The new identity data.
    :param dict options: the processing options. Supported options are ``transactionID``.
    :return: a status indicating success or error, and in case of success the ID allocated to the identity.

.. py:function:: insertIdentityWithId(personID, identityID, identity, options)
    :noindex:

    Insert a new identity in a person and use the provided identity ID. An error is returned if this
    ID is already used for another identity.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str identityID: The ID of the identity.
    :param identity: The new identity data.
    :param dict options: the processing options. Supported options are ``transactionID``.
    :return: a status indicating success or error.

.. py:function:: readIdentity(personID, identityID, options)
    :noindex:

    Retrieve one identity of one person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str personID: The ID of the identity.
    :param dict options: the processing options. Supported options are ``transactionID``.
    :return: a status indicating success or error, and in case of success the identity data.

.. py:function:: updateIdentity(personID, identityID, identity, options)
    :noindex:

    Update an identity.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str personID: The ID of the identity.
    :param identity: The identity data.
    :param dict options: the processing options. Supported options are ``transactionID``.
    :return: a status indicating success or error.

.. py:function:: deleteIdentity(personID, identityID, options)
    :noindex:

    Delete an identity.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str personID: The ID of the identity.
    :param dict options: the processing options. Supported options are ``transactionID``.
    :return: a status indicating success or error.

.. py:function:: setIdentityStatus(personID, identityID, status, options)
    :noindex:

    Update an identity status.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str personID: The ID of the identity.
    :param str status: The new status of the identity.
    :param dict options: the processing options. Supported options are ``transactionID``.
    :return: a status indicating success or error.

----------

.. py:function:: defineReference(personID, identityID, options)
    :noindex:

    Define the reference identity of one person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str personID: The ID of the identity being now the reference.
    :param dict options: the processing options. Supported options are ``transactionID``.
    :return: a status indicating success or error.

.. py:function:: readReference(personID, options)
    :noindex:

    Retrieve the reference identity of one person.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param dict options: the processing options. Supported options are ``transactionID``.
    :return: a status indicating success or error and in case of success the reference identity.

----------

.. py:function:: getGalleries(options)
    :noindex:

    Get the ID of all the galleries.

    **Authorization**: :todo:`To be defined`

    :param dict options: the processing options. Supported options are ``transactionID``.
    :return: a status indicating success or error, and in case of success a list of gallery ID.

.. py:function:: getGalleryContent(galleryID, options)
    :noindex:

    Get the content of one gallery, i.e. the IDs of all the records linked to this gallery.

    **Authorization**: :todo:`To be defined`

    :param str galleryID: Gallery whose content will be returned.
    :param dict options: the processing options. Supported options are ``transactionID``.
    :return: a status indicating success or error. In case of success a list of person/identity IDs.


Options
"""""""

.. list-table:: Population Registry Services Options
    :header-rows: 1
    :widths: 25 75

    * - Name
      - Description

    * - ``transactionID``
      - A string provided by the client application to identity the request being submitted.
        It is optional in most cases. When provided, it can be used for tracing and debugging.

Data Model
""""""""""


.. list-table:: Population Registry Data Model
    :header-rows: 1
    :widths: 25 50 25

    * - Type
      - Description
      - Example

    * - Gallery
      - A group of persons related by a common purpose, designation, or status.
        A person can belong to multiple galleries.
      - ``VIP``, ``Wanted``, etc.

    * - Person
      - Person who is known to an identity assurance system. A person record has a status such as:
        ``active`` or ``inactive`` (the record is excluded from identification searches), a set
        of identities, and a reference identity (i.e. the current correct identity of the person).
      - N/A

    * - Identity
      - The attributes describing an identity of a person.
        An identity has a status such as: ``claimed`` (identity not yet validated), ``valid``
        (the identity is valid), ``invalid`` (the identity is  not valid), ``revoked`` (the identity is
        no longer valid).

        The attributes are separated into two categories: the biographic data and the contextual data.
      - N/A

    * - Biographic Data
      - A dictionary (list of names and values) giving the biographic data of the identity
      - ``firstName``, ``lastName``, ``dateOfBirth``, etc.

    * - Contextual Data
      - A dictionary (list of names and values) attached to the context of establishing the identity
      - ``operatorName``, ``enrolmentDate``, etc.

    * - Document
      - The document data (images) attached to the identity and used to validate it.
      - Birth certificate, invoice

    * - Portrait
      - The portrait (image) at the time the identity record was created. This is stored for information
        purpose but not used for automatic processing.
      - N/A

.. uml::
    :caption: Population Registry Data Model
    :scale: 50%

    !include "skin.iwsd"

    class Gallery {
        string galleryID;
    }

    class Person {
        string personID;
        enum status: Active | Inactive;
        enum physicalStatus: Alive | Dead;
    }

    class Identity {
        string identityID;
        enum status: Claimed | Valid | Invalid | Revoked;
        byte[] clientData;
    }

    Gallery "*" -- "*" Identity

    Person -- "*" Identity: "identities"
    Person -- Identity: "reference"

    class BiographicData {
        string firstName;
        string lastName;
        date dateOfBirth;
        date dateOfDeath;
        string addressLine1;
        ...
    }
    Identity o- BiographicData

    class ContextualData {
        string field1;
        int field2;
        date field3;
        ...
    }
    ContextualData -o Identity
    
    class Document {
      string documentID;
      enum type: Doc1 | Doc2 | Signature | etc;
      int page;
      byte[] image;
      URL imageRef;
    }

    class Portrait {
      string portraitID;
      enum type: F1 | etc;
      byte[] image;
      URL imageRef;
    }
    
    Identity "1" -- "0..*" Document
    Identity "1" -- "0..*" Portrait
      

:todo:`XXX state diagram for the identity`

:todo:`XXX explain status of Person and Identity`

