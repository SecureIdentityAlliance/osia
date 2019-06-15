
Data Access
-----------

See :ref:`annex-interface-dataaccess` for the technical details of this interface.

Services
""""""""

.. py:function:: getPersonAttributes(UIN, names)
    :noindex:

    Retrieve person attributes.

    **Authorization**: :todo:`To be defined`

    :param str UIN: The person's UIN
    :param list[str] names: The names of the attributes requested
    :return: a list of pair (name,value). In case of error (unknown attributes, unauthorized access, etc.) the value is replaced with an error

This service is synchronous. It can be used to retrieve attributes from CR or from PR.

.. uml::
    :caption: ``getPersonAttributes`` Sequence Diagram
    :scale: 50%

    !include "skin.iwsd"
    hide footbox
    participant "CR" as CR
    participant "PR" as PR

    note over CR,PR: CR can request person's attributes from PR
    CR -> PR: getPersonAttributes(UIN,[names])
    PR -->> CR: attributes

    note over CR,PR: PR can request person's attributes from CR
    PR -> CR: getPersonAttributes(UIN,[names])
    CR -->> PR: attributes

-------

.. py:function:: matchPersonAttributes(UIN, attributes)
    :noindex:

    Match person attributes. This service is used to check the value of attributes without exposing private data
    
    **Authorization**: :todo:`To be defined`

    :param str UIN: The person's UIN
    :param list[(str,str)] attributes: The attributes to match. Each attribute is described with its name and the expected value
    :return: If all attributes match, a *Yes* is returned. If one attribute does not match, a *No* is returned along with a list of (name,reason) for each non-matching attribute.
    
This service is synchronous. It can be used to match attributes in CR or in PR.

.. uml::
    :caption: ``matchPersonAttributes`` Sequence Diagram
    :scale: 50%

    !include "skin.iwsd"
    hide footbox
    participant "CR" as CR
    participant "PR" as PR

    note over CR,PR: CR can match person's attributes in PR
    CR -> PR: matchPersonAttributes(UIN,[attributes])
    PR -->> CR: Y/N+reasons

    note over CR,PR: PR can match person's attributes in CR
    PR -> CR: matchPersonAttributes(UIN,[attributes])
    CR -->> PR: Y/N+reasons

-------

.. py:function:: verifyPersonAttributes(UIN, expressions)
    :noindex:

    Evaluate expressions on person attributes. This service is used to evaluate simple expressions on person's attributes
    without exposing private data
    
    **Authorization**: :todo:`To be defined`

    :param str UIN: The person's UIN
    :param list[(str,str,str)] expressions: The expressions to evaluate. Each expression is described with the attribute's name, the operator (one of ``<``, ``>``, ``=``, ``>=``, ``<=``) and the attribute value
    :return: A *Yes* if all expressions are true, a *No* if one expression is false, a *Unknown* if :todo:`To be defined`
    
This service is synchronous. It can be used to verify attributes in CR or in PR.

.. uml::
    :caption: ``verifyPersonAttributes`` Sequence Diagram
    :scale: 50%

    !include "skin.iwsd"
    hide footbox
    participant "CR" as CR
    participant "PR" as PR

    note over CR,PR: CR can verify person's attributes in PR
    CR -> PR: verifyPersonAttributes(UIN,[expressions])
    PR -->> CR: Y/N/U

    note over CR,PR: PR can verify person's attributes in CR
    PR -> CR: verifyPersonAttributes(UIN,[expressions])
    CR -->> PR: Y/N/U

-------

.. py:function:: getPersonUIN(attributes)
    :noindex:

    Retrieve UIN based on a set of attributes. This service is used when the UIN is unknown.

    **Authorization**: :todo:`To be defined`

    :param list[(str,str)] attributes: The attributes to be used to find UIN. Each attribute is described with its name and its value
    :return: a list of matching UIN
    
This service is synchronous. It can be used to get the UIN of a person.

.. uml::
    :caption: ``getPersonUIN`` Sequence Diagram
    :scale: 50%

    !include "skin.iwsd"
    hide footbox
    participant "CR" as CR
    participant "PR" as PR

    note over CR,PR: CR can get UIN from PR
    CR -> PR: getPersonUIN([attributes])
    PR -->> CR: [UIN]

    note over CR,PR: PR can get UIN from CR
    PR -> CR: getPersonUIN([attributes])
    CR -->> PR: [UIN]

-------

.. py:function:: getDocument(UINs,documentType,format)
    :noindex:

    Retrieve in a selected format (PDF, image, ...) a document such as a marriage certificate.

    **Authorization**: :todo:`To be defined`

    :param list[str] UIN: The list of UINs for the persons concerned by the document
    :param str documentType: The type of document (birth certificate, etc.)
    :param str format: The format of the returned/requested document
    :return: The list of the requested documents
    
This service is synchronous. It can be used to get the documents for a person.

.. uml::
    :caption: ``getDocument`` Sequence Diagram
    :scale: 50%

    !include "skin.iwsd"
    hide footbox
    participant "CR" as CR
    participant "PR" as PR

    note over CR,PR: CR can get a document from PR
    CR -> PR: getDocument([UIN],documentType,format)
    PR -->> CR: [documents]

    note over CR,PR: PR can get a document from CR
    PR -> CR: getDocument([UIN],documentType,format)
    CR -->> PR: [documents]

Dictionaries
""""""""""""

As an example, below there is a list of attributes/documents that each component might handle.

.. list-table:: Person Attributes
    :header-rows: 1
    
    * - Attribute Name
      - In CR
      - In PR
      - Description
      
    * - UIN
      - |tick|
      - |tick|
      -
    * - first name
      - |tick|
      - |tick|
      -
    * - last name
      - |tick|
      - |tick|
      -
    * - spouse name
      - |tick|
      - |tick|
      -
    * - date of birth
      - |tick|
      - |tick|
      -
    * - place of birth
      - |tick|
      - |tick|
      -
    * - gender
      - |tick|
      - |tick|
      -
    * - date of death
      - |tick|
      - |tick|
      -
    * - place of death
      - |tick|
      -
      -
    * - reason of death
      - |tick|
      -
      -
    * - status
      -
      - |tick|
      - Example: missing, wanted, dead, etc.

.. list-table:: Certificate Attributes
    :header-rows: 1
    
    * - Attribute Name
      - In CR
      - In PR
      - Description

    * - officer name
      - |tick|
      -
      -
    * - number
      - |tick|
      -
      -
    * - date
      - |tick|
      -
      -
    * - place
      - |tick|
      -
      -
    * - type
      - |tick|
      -
      -

.. list-table:: Union Attributes
    :header-rows: 1
    
    * - Attribute Name
      - In CR
      - In PR
      - Description

    * - date of union
      - |tick|
      -
      -
    * - place of union
      - |tick|
      -
      -
    * - conjoint1 UIN
      - |tick|
      -
      -
    * - conjoint2 UIN
      - |tick|
      -
      -
    * - date of divorce
      - |tick|
      -
      -

.. list-table:: Filiation Attributes
    :header-rows: 1
    
    * - Attribute Name
      - In CR
      - In PR
      - Description

    * - parent1 UIN
      - |tick|
      -
      -
    * - parent2 UIN
      - |tick|
      -
      -

.. list-table:: Document Type
    :header-rows: 1
    
    * - Document Type
      - Description
      
    * - birth certificate
      - :todo:`To be completed`
    * - death certificate
      - :todo:`To be completed`

    * - marriage certificate
      - :todo:`To be completed`