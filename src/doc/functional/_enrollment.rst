
Enrollment Services
-------------------



Services
""""""""

.. py:function:: createEnrollment(enrollmentID, enrollmentData, transactionID)
    :noindex:

    Insert a new enrollment.

    **Authorization**: ``enroll.write``

    :param str enrollmentID: The ID of the enrollment. If the enrollment already exists for the ID an error is returned.
    :param dict enrollmentData: The enrollment attributes.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: readEnrollment(enrollmentID, filter, transactionID)
    :noindex:

    Retrieve the attributes of an enrollment.

    **Authorization**: ``enroll.read``

    :param str enrollmentID: The ID of the enrollment.
    :param set filter: The (optional) set of required attributes to retrieve.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error and in case of success the enrollment data.

.. py:function:: updateEnrollment(enrollmentID, enrollmentData, transactionID)
    :noindex:

    Update an enrollment.

    **Authorization**: ``enroll.write``

    :param str enrollmentID: The ID of the enrollment.
    :param dict enrollmentData: The enrollment data, this can be partial data.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: deleteEnrollment(enrollmentID, transactionID)
    :noindex:

    Delete an enrollment.

    **Authorization**: ``enroll.write``

    :param str enrollmentID: The ID of the enrollment.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: findEnrollment(filter, transactionID)
    :noindex:

    Retrieve a list of enrollments which match passed in search criteria.

    **Authorization**: ``enroll.read``

    :param dict filter: The search criteria to match on.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error and in case of success the matching enrollment list.

----------

.. py:function:: createDocumentCapture(enrollmentID, documentID, documentData, transactionID)
    :noindex:

    Add a new document for an enrollment.

    **Authorization**: ``enroll.doc.write``

    :param str enrollmentID: The ID of the enrollment.
    :param str documentID: The ID of the document.
    :param documentData: The content and attributes of the document.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.  In the case of success, a document identifier.

.. py:function:: readDocumentCapture(documentID, filter, transactionID)
    :noindex:

    Retrieve document data.

    **Authorization**: ``enroll.doc.read``

    :param str documentID: The ID of the document.
    :param set filter: The (optional) set of required attributes to retrieve.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error, and in case of success the document data.

.. py:function:: updateDocumentCapture(documentID, documentData, transactionID)
    :noindex:

    Update a document for an enrollment.

    **Authorization**: ``enroll.doc.write``

    :param str documentID: The ID of the document.
    :param documentData: The content and attributes of the document, this can be partial data.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: deleteDocumentCapture(documentID, transactionID)
    :noindex:

    Delete a document for an enrollment.

    **Authorization**: ``enroll.doc.write``

    :param str documentID: The ID of the document.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.


Filter
""""""

The "filter" parameter used in "read" calls is used to provide a set of
identifiers that limit the amount of data that is returned.
It is often the case that the whole data set is not required, but instead,
a subset of that data.
Where possible, existing standards based identifiers should be used for the
attributes to retrieve.

E.g. For surname/familyname, use OID 2.5.4.4 or id-at-surname.

Some calls may require new filter attributes to be defined.  E.g. when
retrieving biometric data, the caller may only want the meta data about
that biometric, rather than the actual biometric data.

Transaction ID
""""""""""""""
The ``transactionID`` is a string provided by the client application to identity
the request being submitted. It can be used for tracing and debugging.


Data Model
""""""""""

.. list-table:: Enrolment Data Model
    :header-rows: 1
    :widths: 25 50 25

    * - Type
      - Description
      - Example

    * - Enrollment
      - Set of person data which are captured.
      - :todo:`TBD`

    * - Document Data
      - a dictionary (list of names and values) giving the document data of interest for the document services.
      - :todo:`TBD`

    * - Biometric Data
      - Digital representation of biometric characteristics.
        All images can be passed by value (image buffer is in the request) or by reference (the address of the
        image is in the request).
        All images are compliant with ISO 19794. ISO 19794 allows multiple encoding and supports additional
        metadata specific to fingerprint, palmprint, portrait or iris.
      - fingerprint, portrait, iris

    * - Biographic Data
      - a dictionary (list of names and values) giving the biographic data of interest for the biographic services.
      - :todo:`TBD`

----------

