
Third Party Services
--------------------

Services
""""""""

.. py:function:: verifyIdentity(UIN, [IDAttribute])
    :noindex:

    Verify Identity based on UIN and set of Identity Attributes.
    Attributes can be Biometric data, Civil data or a credential.

    **Authorization**: :todo:`To be defined`

    :param str UIN: The person's UIN
    :param list[str] IDAttribute: A list of list of pair (name,value) requested
    :return: Y or N
    
    In case of error (unknown attributes, unauthorized access, etc.) the value is replaced with an error

.. py:function:: identify([inIDAttribute], [outIDAttribute])
    :noindex:

    Identify a person based on a set of inIDAttribute Identity Attributes.
    Attributes can be Biometric data, Civil data or a credential.
    Returns list of identities with attributes specified in outIDAttribute

    **Authorization**: :todo:`To be defined`

    :param list[str] inIDAttribute: A list of list of pair (name,value) requested
    :param list[str] outIDAttribute: A list of list of attribute names requested
    :return: Y or N
    
    In case of error (unknown attributes, unauthorized access, etc.) the value is replaced with an error

.. py:function:: getAttributes(UIN, names)
    :noindex:

    Retrieve person attributes.

    **Authorization**: :todo:`To be defined`

    :param str UIN: The person's UIN
    :param list[str] names: The names of the attributes requested
    :return: a list of pair (name,value). In case of error (unknown attributes, unauthorized access, etc.)
        the value is replaced with an error

.. py:function:: getAttributeSet(UIN, setName)
    :noindex:

    Retrieve person attributes corresponding to a predefined set name.

    **Authorization**: :todo:`To be defined`

    :param str UIN: The person's UIN
    :param str setName: The name of predefined attributes set name
    :return: a list of pair (name,value). In case of error (unknown attributes, unauthorized access, etc.)
        the value is replaced with an error

   