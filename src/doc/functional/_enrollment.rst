
Enrollment Services
-------------------



Services
""""""""

.. py:function:: createEnrollment(enrollmentID, enrollmentTypeId, enrollmentFlags, requestData, biometricData, biographicData, documentData, transactionID)
    :noindex:

    Insert a new enrollment.

    **Authorization**: :todo:`To be defined`

    :param str enrollmentID: The ID of the enrollment. If the enrollment already exists for the ID an error is returned.
	:param str enrollmentTypeId: The enrollment type ID of the enrollment.
	:param dict enrollmentFlags: The enrollment custom flags.
    :param dict requestData: The enrollment data related to the enrollment itself.
	:param dict biometricData: The enrollment biometric data.
	:param biographicData: The enrollment biographic data.
	:param dict documentData: The enrollment biometric data.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: readEnrollment(enrollmentID, attributes, transactionID)
    :noindex:

    Retrieve the attributes of an enrollment.

    **Authorization**: :todo:`To be defined`

    :param str enrollmentID: The ID of the enrollment.
    :param set attributes: The (optional) set of required attributes to retrieve.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error and in case of success the enrollment data.

.. py:function:: updateEnrollment(enrollmentID, enrollmentTypeId, enrollmentFlags, requestData, biometricData, biographicData, documentData, transactionID)
    :noindex:

    Update an enrollment.

    **Authorization**: :todo:`To be defined`

    :param str enrollmentID: The ID of the enrollment. If the enrollment already exists for the ID an error is returned.
	:param str enrollmentTypeId: The enrollment type ID of the enrollment.
	:param dict enrollmentFlags: The enrollment custom flags.
    :param dict requestData: The enrollment data related to the enrollment itself.
	:param dict biometricData: The enrollment biometric data, this can be partial data.
	:param dict biographicData: The enrollment biographic data.
	:param dict documentData: The enrollment biometric data, this can be partial data.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error.

.. py:function:: findEnrollments(expressions, transactionID)
    :noindex:

    Retrieve a list of enrollments which match passed in search criteria.

    **Authorization**: :todo:`To be defined`

    :param list[(str,str,str)] expressions: The expressions to evaluate. Each expression is described with the attribute's name, the operator (one of ``<``, ``>``, ``=``, ``>=``, ``<=``) and the attribute value
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error and in case of success the matching enrollment list.
	
.. py:function:: finalizeEnrollments(enrollmentID, transactionID)
    :noindex:

    When all the enrollment steps are done, the enrollment client indicates to the enrollment server that all data has been collected and that any further processing can be triggered.

    **Authorization**: :todo:`To be defined`

    :param str enrollmentID: The ID of the enrollment.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error and in case of success the matching enrollment list.

.. py:function:: sendBuffer(enrollmentId, data)
    :noindex:

    This service is used to send separately the buffers of the images. Buffers can be sent any time from the enrollment client prior to the create or update.

    **Authorization**: :todo:`To be defined`

    :param str enrollmentID: The ID of the enrollment.
	:param image data: The image of the request.
    :param string transactionID: The client generated transactionID.
    :return: a status indicating success or error and in case of success the matching enrollment list.

Attributes
""""""

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
	
	* - Enrollment Flags
      - a dictionary (list of names and values) for custom flags.
	 
	* - Request data
      - a dictionary (list of names and values) for data related to the enrollment itself (the operator, the station, the data, etc.).
	  
      - :todo:`TBD`

----------

