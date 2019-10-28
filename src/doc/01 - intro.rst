
Introduction
============

Problem Statement: vendor lock-in
---------------------------------

Target 16.9 of the UN Sustainable Development Goals is to "provide legal identity for all, including birth registration"
by the year 2030. But there is a major barrier: the lack of vendor/provider and technology neutrality - commonly
known as "vendor lock-in".

The lack of partner and technology neutrality and its consequences becomes apparent when a customer needs to
replace one component of the identity management solution with one from another provider, or expand the scope
of their solution by linking to new components. Technology barriers are the following:

1. *Solution architectures are not interoperable by design*. The lack of common definitions as to the overall
   scope of an identity ecosystem, as well as in the main functionalities of a system’s components (civil registry,
   biometric identification system, population registry etc.), blurs the lines between components and leads to
   inconsistencies. This lack of so-called irreducibly modular architectures makes it difficult,
   if not impossible, to switch to a third-party component intended to provide the same function and
   leads to incompatibilities when adding a new component to an existing ecosystem.

2. *Standardized interfaces (APIs) do not exist*. Components are often unable to communicate with each
   other due to varying interfaces (APIs) and data formats, making it difficult to swap out components
   or add new ones to the system.

For government policy makers tasked with implementing national identification systems, vendor lock-in
is now one of their biggest concerns.

.. figure:: images/vendorlockin.*

    Vendor Lock-In

The OSIA Initiative
-------------------

Launched by the not-for-profit Secure Identity Alliance, *Open Standard Identity APIs* (OSIA) is an
initiative created for the public good to address vendor lock-in problem.

OSIA addresses the vendor lock-in concern by providing a simple, open standards-based connectivity layer
between all key components within the national identity ecosystem.

OSIA scope is as follows:

**1. Address the lack of common definitions within the identity ecosystem – NON PRESCRIPTIVE**

    Components of the identity ecosystem (civil registry, population registry, biometric identification system etc.)
    from different vendors are functionally incompatible due to the absence of a common definition/understanding of
    broader functionalities and scope.

    OSIA first step has been to formalize definitions, scope and main functionalities of each component
    within the identity ecosystem.

**2. Create a set of standardized interfaces – PRESCRIPTIVE**

    This core piece of work develops the set of interfaces and standardized data formats to connect the multiple
    identity ecosystem components to ensure seamless interaction via pre-defined services.

    Process of interaction among components (hence type of services each component implements) is down to each government
    to define and implement according to local laws and regulations.

With OSIA, governments are free to select the components they need, from the suppliers
they choose – without fear of lock in.

And because OSIA operates at the interface layer, interoperability is assured without the need to rearchitect
environments or rebuild solutions from the ground up. ID ecosystem components are simply swapped in and out
as the use case demands – from best-of-breed options already available on the market.

This real-world approach dramatically reduces operational and financial risk, increases the effectiveness of
existing identity ecosystems, and rapidly moves government initiatives from proof of concept to live environments.


Diffusion, Audience, and Access
-------------------------------

This specification is hosted in `GitHub <https://github.com/SecureIdentityAlliance/osia>`_ and can be
downloaded from `ReadTheDocs <https://osia.readthedocs.io/en/latest/>`_.

This specification is licensed under `The MIT License <https://opensource.org/licenses/MIT>`_.

Any country, technology partner or individual is free to download the functional and technical specifications
to implement it in their customized foundational and sectoral ID systems or components.
Governments can also reference OSIA as Open Standards in tenders.
For more information on how to reference OSIA please see Section :ref:`osia-versions-ref`.

Document Overview
-----------------

This document aims at:

- formalizing definitions, scope and main functionalities of each component within the identity ecosystem,
- defining standardized interface and data format to connect the multiple ecosystem components to ensure
  seamless interaction via pre-defined services.

This document is structured as follows:

- Chapter 1 Introduction
- Chapter 2 Functional View
- Chapter 3 Security and Privacy
- Chapter 4 OSIA Versions and Referencing
- Chapter 5 Interfaces
- Chapter 6 Components

Convention and Typographical Rules
----------------------------------

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and
"OPTIONAL" in this document are to be interpreted as described in `RFC 2119 <http://www.ietf.org/rfc/rfc2119.txt>`_.

Code samples highlighted in blocks appear like that:

.. code-block:: json

    {
        "key": "value",
        "another_key": 23
    }
    
.. note::
    
    Indicates supplementary explanations and useful tips.

.. warning::

    Indicates that the specific condition or procedure must be
    respected.
    

Revision History
----------------

.. list-table::
   :header-rows: 1

   * - Version
     - Date
     - Notes
   * - 1.0
     - 2018-12
     - First release
   * - 2.0
     - 2019-06
     - Second release


