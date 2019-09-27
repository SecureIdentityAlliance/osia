
Population Registry
-------------------

This interface describes services to manage a registry of the population in the context of an identity system. It is based on
the following principles:

- It supports a historized identity model, meaning that a person has one identity and this identity
  has a history.
- Images can be passed by value or reference. When passed by value, they are base64-encoded.
- Existing standards are used whenever possible.
- The services to access and exchange the data stored by the population registry are described separately and shared
  with multiple registries.

See :ref:`annex-interface-pr` for the technical details of this interface.

Services
""""""""

.. py:function:: insert(personID, galleryID, biographicData, contextualData, clientData, options)
    :noindex:

    Insert a new identity in a new or existing person. This service is synchronous.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person. If the person does not exist, it is created with a status XXX
    :param list(str) galleryID: the gallery ID to which this person belongs
    :param dict biographicData: The biographic data (ex: name, date of birth, gender, etc.)
    :param dict contextualData: The contextual data (ex: enrolment date, location, etc.)
    :param bytes clientData: additional data not interpreted by the server but stored as is and returned
        when identity data is requested.
    :param dict options: the processing options. Supported options are ``transactionID``.
    :return: a status indicating success or error and the ID of the new identity.

.. py:function:: read(personID, identityID, callback, options)
    :noindex:

    Retrieve the data of an identity.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str identityID: The ID of the identity to be returned. This is optional. If not provided, all the
        identities of the person are returned.
    :param dict options: the processing options. Supported options are ``transactionID``.
    :return: a status indicating success or error and the identity data.

.. py:function:: update(personID, identityID, galleryID, biographicData, contextualData, clientData, options)
    :noindex:

    Update an identity.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str identityID: The ID of the identity to be updated.
    :param list(str) galleryID: the gallery ID to which this identity belongs
    :param dict biographicData: The biographic data (ex: name, date of birth, gender, etc.)
    :param dict contextualData: The contextual data (ex: encounter date, location, etc.)
    :param bytes clientData: additional data not interpreted by the server but stored as is and returned
        when encounter data is requested.
    :param dict options: the processing options. Supported options are ``transactionID``.
    :return: a status indicating success or error.

.. py:function:: delete(personID, identityID, options)
    :noindex:

    Delete an encounter.

    **Authorization**: :todo:`To be defined`

    :param str personID: The ID of the person.
    :param str identityID: The ID of the identity to be deleted. If not provided, all the
        identities of the person are deleted.
    :param dict options: the processing options. Supported options are ``transactionID``.
    :return: a status indicating success, error, or pending operation.
        In case of pending operation, the operation status will be sent later.

----------

.. py:function:: getGalleries(options)
    :noindex:

    Get the ID of all the galleries.

    **Authorization**: :todo:`To be defined`

    :param dict options: the processing options. Supported options are ``transactionID``.
    :return: a status indicating success or error and a list of gallery ID.

.. py:function:: getGalleryContent(galleryID, options)
    :noindex:

    Get the content of one gallery, i.e. the IDs of all the records linked to this gallery.

    **Authorization**: :todo:`To be defined`

    :param str galleryID: Gallery whose content will be returned.
    :param dict options: the processing options. Supported options are ``transactionID``.
    :return: a status indicating success or error and a list of persons/identities.


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

    Person "*" - "*" Gallery

    class Identity {
        string identityID;
        enum status: Claimed | Valid | Invalid | Revoked;
        byte[] clientData;
    }

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
    
    class Filters {
        string filter1;
        int filter2Min;
        int filter2Max;
        date filter3Min;
        date filter3Max;
        ...
    }

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
      

