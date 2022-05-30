
Data Format
===========

The following data formats are used in OSIA:

.. list-table:: OSIA Data Formats
    :header-rows: 1
    :widths: 20 30 50

    * - Data
      - Format
      - Description

    * - Service Description
      - `OpenAPI 3.0.x <https://swagger.io/specification/>`_
      - All OSIA interfaces are described using OpenAPI 3.0.x format. OpenAPI can use json or YAML file, YAML is preferred for its readability.

    * - Service Payload
      - `json <https://en.wikipedia.org/wiki/JSON>`_
      - json has builtin format for string, integer, floating number, boolean, as well as list and dictionary.
        json is widely used and supported by many different languages and frameworks, making it ideal to favor interoperability.

    * - Date & Time
      - `iso8601 <https://en.wikipedia.org/wiki/ISO_8601>`_
      - The iso8601 defines format for date and date and time. It supports local time as well as UTC time.
        iso8601-2, dated 2019, can be used to represent dates with unknown part.

    * - Biometric Images
      - JPEG, JPEG2000, PNG, WSQ, ISO19794
      - Images can be transfered as a URL or can be embedded in the json. When embedded they are encoded in base64.
        It is highly recommended to use a widely used format such as JPEG, PNG, or WSQ for fingerprints.
        ISO19794 is also recommended when possible.

    * - Documents
      - JPEG, PNG, PDF
      - Documents captured during enrollment can use the JPEG format for monopage document. PDF is also
        widely recognized and very convenient to transfer both images and text in multipage documents.


