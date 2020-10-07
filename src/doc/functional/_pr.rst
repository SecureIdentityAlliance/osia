
Population Registry Services
----------------------------

This interface describes services to manage a registry of the population in the context of an identity system. It is based on
the following principles:

- It supports a history of identities, meaning that a person has one identity and this identity
  has a history.
- Images can be passed by value or reference. When passed by value, they are base64-encoded.
- Existing standards are used whenever possible.
- This interface is complementary to the data access interface. The data access interface is used
  to query the persons and uses the reference identity to return attributes.
- The population registry can store the biometric data or can rely on the ABIS subsystem to do it.
  The preferred solution, for a clean separation of data of different nature and by application
  of GDPR principles, is to put the biometric data only in the ABIS. Yet many existing systems
  store biometric data with the biographic data and this specification gives the flexibility to do it.

See :ref:`annex-interface-pr` for the technical details of this interface.

Services
""""""""

.. py:function:: createPerson(personID, personData, transactionID)
    :noindex:

    Create a new person.

    **Authorization**: ``pr.person.write``

    :param str personID: The ID of the person. If the person already exists for the ID an error is returned.
    :param personData: The person attributes.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :return: a status indicating success or error.

.. py:function:: readPerson(personID, transactionID)
    :noindex:

    Read the attributes of a person.

    **Authorization**: ``pr.person.read``

    :param str personID: The ID of the person.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :return: a status indicating success or error and in case of success the person data.

.. py:function:: updatePerson(personID, personData, transactionID)
    :noindex:

    Update a person.

    **Authorization**: ``pr.person.write``

    :param str personID: The ID of the person.
    :param dict personData: The person data.
    :return: a status indicating success or error.

.. py:function:: deletePerson(personID, transactionID)
    :noindex:

    Delete a person and all its identities.

    **Authorization**: ``pr.person.write``

    :param str personID: The ID of the person.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :return: a status indicating success or error.

.. py:function:: mergePerson(personID1, personID2, transactionID)
    :noindex:

    Merge two person records into a single one. Identity ID are preserved and in case of duplicates
    an error is returned and no changes are done.
    The reference identity is not changed.

    **Authorization**: ``pr.person.write``

    :param str personID1: The ID of the person that will receive new identities
    :param str personID2: The ID of the person that will give its identities. It will be deleted if the move of all identities is successful.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :return: a status indicating success or error.

----------

.. py:function:: createIdentity(personID, identityID, identity, transactionID)
    :noindex:

    Create a new identity in a person. If no identityID is provided, a new one is generated. If identityID
    is provided, it is checked for uniqueness and used for the identity if unique.
    An error is returned if the provided identityID is not unique.

    **Authorization**: ``pr.identity.write``

    :param str personID: The ID of the person.
    :param str identityID: The ID of the identity.
    :param identity: The new identity data.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :return: a status indicating success or error.

.. py:function:: readIdentity(personID, identityID, transactionID)
    :noindex:

    Read one or all the identities of one person.

    **Authorization**: ``pr.identity.read``

    :param str personID: The ID of the person.
    :param str identityID: The ID of the identity. If not provided, all identities are returned.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :return: a status indicating success or error, and in case of success a list of identities.

.. py:function:: updateIdentity(personID, identityID, identity, transactionID)
    :noindex:

    Update an identity. An identity can be updated only in the status ``claimed``.

    **Authorization**: ``pr.identity.write``

    :param str personID: The ID of the person.
    :param str identityID: The ID of the identity.
    :param identity: The identity data.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :return: a status indicating success or error.

.. py:function:: partialUpdateIdentity(personID, identityID, identity, transactionID)
    :noindex:

    Update part of an identity. Not all attributes are mandatory. The payload
    is defined as per :rfc:`7396`.
    An identity can be updated only in the status ``claimed``.

    **Authorization**: ``pr.identity.write``

    :param str personID: The ID of the person.
    :param str identityID: The ID of the identity.
    :param identity: Part of the identity data.
    :return: a status indicating success or error.

.. py:function:: deleteIdentity(personID, identityID, transactionID)
    :noindex:

    Delete an identity.

    **Authorization**: ``pr.identity.write``

    :param str personID: The ID of the person.
    :param str identityID: The ID of the identity.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :return: a status indicating success or error.

.. py:function:: setIdentityStatus(personID, identityID, status, transactionID)
    :noindex:

    Set an identity status.

    **Authorization**: ``pr.identity.write``

    :param str personID: The ID of the person.
    :param str identityID: The ID of the identity.
    :param str status: The new status of the identity.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :return: a status indicating success or error.

----------

.. py:function:: defineReference(personID, identityID, transactionID)
    :noindex:

    Define the reference identity of one person.

    **Authorization**: ``pr.reference.write``

    :param str personID: The ID of the person.
    :param str identityID: The ID of the identity being now the reference.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :return: a status indicating success or error.

.. py:function:: readReference(personID, transactionID)
    :noindex:

    Read the reference identity of one person.

    **Authorization**: ``pr.reference.read``

    :param str personID: The ID of the person.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :return: a status indicating success or error and in case of success the reference identity.

----------

.. py:function:: readGalleries(transactionID)
    :noindex:

    Read the ID of all the galleries.

    **Authorization**: ``pr.gallery.read``

    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :return: a status indicating success or error, and in case of success a list of gallery ID.

.. py:function:: readGalleryContent(galleryID, transactionID, offset, limit)
    :noindex:

    Read the content of one gallery, i.e. the IDs of all the records linked to this gallery.

    **Authorization**: ``pr.gallery.read``

    :param str galleryID: Gallery whose content will be returned.
    :param str transactionID: A free text used to track the system activities related to the same transaction.
    :param int offset: The offset of the query (first item of the response) (optional, default to ``0``)
    :param int limit: The maximum number of items to return (optional, default to ``1000``)
    :return: a status indicating success or error. In case of success a list of person/identity IDs.


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
      - Person who is known to an identity assurance system. A person record has:
      
        - a status, such as ``active`` or ``inactive``, defining the status of the record
          (the record can be excluded from queries based on this status),
        - a physical status, such as ``alive`` or ``dead``, defining the status of the person,
        - a set of identities, keeping track of all identity data submitted by the person during
          the life of the system,
        - a reference identity, i.e. a consolidated view of all the identities
          defining the current correct identity of the person. It corresponds usually to the last
          valid identity but it can also include data from previous identities.
      - N/A

    * - Identity
      - The attributes describing an identity of a person.
        An identity has a status such as: ``claimed`` (identity not yet validated), ``valid``
        (the identity is valid), ``invalid`` (the identity is  not valid), ``revoked`` (the identity
        cannot be used any longer).

        An identity can be updated only in the status ``claimed``.

        The allowed transitions for the status are represented below:

        .. uml::
            :scale: 30%

            [*] --> claimed
            claimed --> valid
            claimed -->invalid
            valid --> revoked

        The attributes are separated into two categories: the biographic data and the contextual data.

      - N/A

    * - Biographic Data
      - A dictionary (list of names and values) giving the biographic data of the identity
      - ``firstName``, ``lastName``, ``dateOfBirth``, etc.

    * - Contextual Data
      - A dictionary (list of names and values) attached to the context of establishing the identity
      - ``operatorName``, ``enrollmentDate``, etc.

    * - Biometric Data
      - Digital representation of biometric characteristics.
        All images can be passed by value (image buffer is in the request) or by reference (the address of the
        image is in the request).
        All images are compliant with ISO 19794. ISO 19794 allows multiple encoding and supports additional
        metadata specific to fingerprint, palmprint, portrait, iris, signature.
      - fingerprint, portrait, iris, signature

    * - Document
      - The document data (images) attached to the identity and used to validate it.
      - Birth certificate, invoice

.. uml::
    :caption: Population Registry Data Model
    :scale: 50%

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
    
    class BiometricData {
    string type
    string subType
    byte[] image
    URL imageRef
    ...
    }
    Identity "1" -- "0..*" BiometricData

    class Document {
      enum type: Doc1 | Doc2 | Signature | etc;
      string instance;
    }

    class DocumentPart {
      int[] pages;
      byte[] data;
      URL dataRef;
      int width;
      int height;
      date captureDate;
      string captureDevice;
      string format;
    }

    Identity "1" -- "0..*" Document

    Document "1" -- "1..*" DocumentPart
