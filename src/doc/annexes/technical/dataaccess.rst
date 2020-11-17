
.. _annex-interface-dataaccess:

Data Access
-----------

.. only:: html

    Get the OpenAPI file for this interface: `dataaccess.yaml <../../dataaccess.yaml>`_

.. raw:: latex

    Get the OpenAPI file for this interface: \textattachfile[]{../html/dataaccess.yaml}{dataaccess.yaml}

.. sidebar:: Data Access Services

    .. hlist::
        :columns: 2

        - `queryPersonList <#get--v1-persons>`_
        - `queryPersonUIN <#get--v1-persons>`_
        - `readPersonAttributes <#get--v1-persons-uin>`_
        - `matchPersonAttributes <#post--v1-persons-uin-match>`_
        - `verifyPersonAttributes <#post--v1-persons-uin-verify>`_
        - `readDocument <#get--v1-persons-uin-document>`_

Services
""""""""

.. openapi:: ../../yaml/dataaccess.yaml
    :examples:
    :group:

Data Model
""""""""""

.. _person-attributes:

Person Attributes
'''''''''''''''''

When exchanged in the services described in this document, the persons attributes
will apply the following rules:

.. list-table:: Person Attributes
    :header-rows: 1
    :widths: 20 30 50
    
    * - Attribute Name
      - Description
      - Format
      
    * - ``uin``
      - Unique Identity Number
      - Text
    * - ``firstName``
      - First name
      - Text
    * - ``lastName``
      - Last name
      - Text
    * - ``spouseName``
      - Spouse name
      - Text
    * - ``dateOfBirth``
      - Date of birth
      - Date (iso8601). Example: ``1987-11-17``
    * - ``placeOfBirth``
      - Place of birth
      - Text
    * - ``gender``
      - Gender
      - Number (iso5218). One of 0 (Not known), 1 (Male), 2 (Female), 9 (Not applicable)
    * - ``dateOfDeath``
      - Date of death
      - Date (iso8601). Example: ``2018-11-17``
    * - ``placeOfDeath``
      - Place of death
      - Text
    * - ``reasonOfDeath``
      - Reason of death
      - Text
    * - ``status``
      - Status. Example: missing, wanted, dead, etc.
      - Text

    
.. _matching-error:

Matching Error
''''''''''''''

A list of:

.. list-table:: Matching Error Object
    :header-rows: 1
    :widths: 25 20 35 10
    
    * - Attribute
      - Type
      - Description
      - Mandatory

    * - ``attributeName``
      - String
      - Attribute name (See :ref:`person-attributes`)
      - Yes

    * - ``errorCode``
      - 32 bits integer
      - Error code. Possible values: ``0`` (attribute does not exist); ``1`` (attribute exists but does not match)
      - Yes

.. _expression:

Expression
''''''''''

.. list-table:: Expression Object
    :header-rows: 1
    :widths: 25 20 35 10
    
    * - Attribute
      - Type
      - Description
      - Mandatory

    * - ``attributeName``
      - String
      - Attribute name (See :ref:`person-attributes`)
      - Yes

    * - ``operator``
      - String
      - Operator to apply. Possible values: ``<``, ``>``, ``=``, ``>=``, ``<=``
      - Yes

    * - ``value``
      - string, or integer, or boolean
      - The value to be evaluated
      - Yes

.. _error:

Error
'''''

.. list-table:: Error Object
    :header-rows: 1
    :widths: 25 20 35 10
    
    * - Attribute
      - Type
      - Description
      - Mandatory

    * - ``code``
      - 32 bits integer
      - Error code
      - Yes

    * - ``message``
      - String
      - Error message
      - Yes

