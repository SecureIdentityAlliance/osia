
Enrollment Services
-------------------

This interface describes enrollment services in the context of an identity system. It is based on
the following principles:

- When enrollment is done in one step, the CreateEnrollment can contain all the data and an additional flag (finalize) to indicate all data was collected.
- During the process, enrollment structure can be updated. Only the data that changed need to be transferred. Data not included is left unchanged on the server. In the following example, the biographic data is not changed.
- Images can be passed by value or reference. When passed by value, they are base64-encoded.
- Existing standards are used whenever possible, for instance preferred image format for biometric data is ISO-19794.

.. admonition:: About documents

    Adding one document or deleting one document implies that:
    
    - The full document list is read (ReadEnrollment)
    - The document list is altered locally to the enrollment client (add or delete)
    - The full document list is sent back using the UpdateEnrollment service

Services
""""""""

.. py:function:: createEnrollment(enrollmentID, enrollmentTypeId, enrollmentFlags, requestData, contextualData, biometricData, biographicData, documentData, finalize, transactionID)
    :noindex:

    Insert a new enrollment.

    **Authorization**: ``enroll.write``

    :param str enrollmentID: The ID of the enrollment. If the enrollment already exists for the ID an error is returned.
    :param str enrollmentTypeId: The enrollment type ID of the enrollment.
    :param dict enrollmentFlags: The enrollment custom flags.
    :param dict requestData: The enrollment data related to the enrollment itself.
    :param dict contextualData: Information about the context of the enrollment
    :param list biometricData: The enrollment biometric data.
    :param dict biographicData: The enrollment biographic data.
    :param list documentData: The enrollment biometric data.
    :param str finalize: Flag to indicate that data was collected.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: readEnrollment(enrollmentID, attributes, transactionID)
    :noindex:

    Retrieve the attributes of an enrollment.

    **Authorization**: ``enroll.read``

    :param str enrollmentID: The ID of the enrollment.
    :param set attributes: The (optional) set of required attributes to retrieve.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error and in case of success the enrollment data.

.. py:function:: updateEnrollment(enrollmentID, enrollmentTypeId, enrollmentFlags, requestData, contextualData, biometricData, biographicData, documentData, finalize, transactionID)
    :noindex:

    Update an enrollment.

    **Authorization**: ``enroll.write``

    :param str enrollmentID: The ID of the enrollment. If the enrollment already exists for the ID an error is returned.
    :param str enrollmentTypeId: The enrollment type ID of the enrollment.
    :param dict enrollmentFlags: The enrollment custom flags.
    :param dict requestData: The enrollment data related to the enrollment itself.
    :param dict contextualData: Information about the context of the enrollment
    :param list biometricData: The enrollment biometric data, this can be partial data.
    :param dict biographicData: The enrollment biographic data.
    :param list documentData: The enrollment biometric data, this can be partial data.
    :param str finalize: Flag to indicate that data was collected.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.
	
.. py:function:: partialupdateEnrollment(enrollmentID, enrollmentTypeId, enrollmentFlags, requestData, contextualData, biometricData, biographicData, documentData, finalize, transactionID)
    :noindex:

    Update part of an enrollment. Not all attributes are mandatory. The payload
    is defined as per :rfc:`7396`.

    **Authorization**: ``enroll.write``

    :param str enrollmentID: The ID of the enrollment. If the enrollment already exists for the ID an error is returned.
    :param str enrollmentTypeId: The enrollment type ID of the enrollment.
    :param dict enrollmentFlags: The enrollment custom flags.
    :param dict requestData: The enrollment data related to the enrollment itself.
    :param dict contextualData: Information about the context of the enrollment
    :param list biometricData: The enrollment biometric data, this can be partial data.
    :param dict biographicData: The enrollment biographic data.
    :param list documentData: The enrollment biometric data, this can be partial data.
    :param str finalize: Flag to indicate that data was collected.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: finalizeEnrollment(enrollmentID, transactionID)
    :noindex:

    When all the enrollment steps are done, the enrollment client indicates to the enrollment server that all data has been collected and that any further processing can be triggered.

    **Authorization**: ``enroll.write``

    :param str enrollmentID: The ID of the enrollment.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.
    
.. py:function:: readEnrollmentResult(enrollmentID, transactionID, names)
    :noindex:

    Retrieve the result(s) of the processing of an enrollment.
    The results are available only after the finalization of the enrollment.

    **Authorization**: ``enroll.read``

    :param str enrollmentID: The ID of the enrollment.
    :param string transactionID: The client generated transactionID.
    :param list[str] names: The names of the results requested
    :return: a dictionary with a list of (name,value). The value can be replaced with a structure to indicate an error or a result not yet available.

.. py:function:: deleteEnrollment(enrollmentID, transactionID)
    :noindex:

    Deletes the enrollment

    **Authorization**: ``enroll.write``

    :param str enrollmentID: The ID of the enrollment.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: findEnrollments(expressions, offset, limit, transactionID)
    :noindex:

    Retrieve a list of enrollments which match passed in search criteria.

    **Authorization**: ``enroll.read``

    :param list[(str,str,str)] expressions: The expressions to evaluate. Each expression is described with the attribute's name, the operator (one of ``<``, ``>``, ``=``, ``>=``, ``<=``) and the attribute value
    :param int offset: The offset of the query (first item of the response) (optional, default to ``0``)
    :param int limit: The maximum number of items to return (optional, default to ``100``)
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error and in case of success the matching enrollment list.

.. py:function:: createBuffer(enrollmentId, data, digest)
    :noindex:

    This service is used to send separately the buffers of the images. Buffers can be sent any time from the enrollment client prior to the create or update.

    **Authorization**: ``enroll.buf.write``

    :param str enrollmentID: The ID of the enrollment.
    :param image data: The buffer data.
    :param string transactionID: The client generated transactionID.
    :param string digest: The digest (hash) of the buffer used by the server to check the integrity of the data received.
    :return: a status indicating success or error and in case of success the buffer ID.

.. py:function:: readBuffer(enrollmentId, bufferId)
    :noindex:

    This service is used to get the data of a buffer.

    **Authorization**: ``enroll.buf.read``

    :param str enrollmentID: The ID of the enrollment.
    :param str bufferID: The ID of the buffer.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error and in case of success the data of the buffer and a digest.

Attributes
""""""""""

The "attributes" parameter used in "read" calls is used to provide a set of
identifiers that limit the amount of data that is returned.
It is often the case that the whole data set is not required, but instead,
a subset of that data.
Where possible, existing standards based identifiers should be used for the
attributes to retrieve.

E.g. For surname/familyname, use OID 2.5.4.4 or id-at-surname.

Some calls may require new attributes to be defined.  E.g. when
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
      - The document data of the enrollment.
      - :todo:`TBD`

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
      - :todo:`TBD`

    * - Enrollment Flags
      - a dictionary (list of names and values) for custom flags.
      - :todo:`TBD`
 
    * - Request Data
      - a dictionary (list of names and values) for data related to the enrollment itself (the operator, the station, the data, etc.).
      - :todo:`TBD`

    * - Contextual Data
      - A dictionary (list of names and values) attached to the context of establishing the identity
      - ``operatorName``, ``enrollmentDate``, etc.

    * - Attributes
      - a dictionary (list of names and values or *range* of values) describing the attributes to return.
        Attributes can apply on biographic data, document data, request data, or enrollment flag data.
      - :todo:`TBD`

    * - Expressions
      - Each expression is described with the attribute's name, the operator (one of ``<``, ``>``, ``=``, ``>=``, ``<=``, ``!=``) and the attribute value
      - :todo:`TBD`

.. uml::
    :caption: Enrollment Data Model
    :scale: 50%

    class Enrollment {
        string enrollmentID;
    }

    class ContextualData {
        string operator;
        date date;
        ...
    }
    Enrollment o- ContextualData

    class BiographicData {
        string field1;
        int field2;
        date field3;
        ...
    }
    BiographicData -o Enrollment

    class BiometricData {
        byte[] image;
        URL imageRef;
    }
    Enrollment o-- "*" BiometricData

    class DocumentData {
        int documentType;
    }
    Enrollment o-- "*" DocumentData

    class DocumentPart {
        byte[] image;
        URL imageRef;
    }
    DocumentData o-- "*" DocumentPart

    class RequestData {
        string field1;
        int field2;
        date field3;
        ...
    }
    RequestData --o Enrollment

    class EnrollmentFlagsData {
        string field1;
        int field2;
        date field3;
        ...
    }
    EnrollmentFlagsData --o Enrollment
