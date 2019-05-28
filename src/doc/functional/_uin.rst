
UIN Management
--------------

See :ref:`annex-interface-uin` for the technical details of this interface.

Services
""""""""

.. py:function:: createUIN(attributes)
    :noindex:

    Generate a new UIN.

    :param list[(str,str)] attributes: A list of pair (attribute name, value) that can be used to allocate a new UIN
    :return: a new UIN or an error if the generation is not possible

This service is synchronous.

.. uml::
    :caption: ``createUIN`` Sequence Diagram
    :scale: 50%

    !include "skin.iwsd"
    hide footbox
    participant "CR" as CR
    participant "PR" as PR
    participant "UIN Generator" as UIN

    note over CR,UIN: CR can request a new UIN
    CR -> UIN: createUIN([attributes])
    UIN -->> CR: UIN

    note over PR,UIN: PR can request a new UIN
    PR -> UIN: createUIN([attributes])
    UIN -->> PR: UIN
