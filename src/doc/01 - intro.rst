
.. _chapter-intro:

Introduction
============

Identity systems that are built on specific vendor solutions lack interoperability among
the main system modules. Lack of vendor and technology interoperability causes difficulties
in replacing a building block of an identity management system from vendor A with an equivalent
building block from vendor B or when expanding the scope of an existing system by linking to
new building blocks. The main technology barrier is the lack of standardized interfaces (APIs).
Building blocks are often unable to communicate with each other due to varying interfaces (APIs)
and data formats, making it difficult to swap out building blocks or add new ones to the system.

This |specification| describes a set of standardized application program interfaces (APIs) needed
to connect the multiple building blocks of an identity management solution.

Problem Statement: lack of interoperability in identity systems
---------------------------------------------------------------

.. only:: not itu

    Target 16.9 of the UN Sustainable Development Goals is to "provide legal identity for all,
    including birth registration" by the year 2030. But there is a major barrier: the lack of vendor/provider
    and technology neutrality - commonly known as "vendor lock-in".

Lack of vendor and technology neutrality causes difficulties in replacing a building block of an
identity management system from vendor A with an equivalent building block from vendor B,
or expand the scope of an existing system by linking to new building blocks.
The main technology barrier is the lack of standardized interfaces (APIs).
Building blocks are often unable to communicate with each other due to varying interfaces (APIs)
and data formats, making it difficult to swap out building blocks or add new ones to the system.

This |specification| addresses the vendor lock-in concern by providing a set of standardized interfaces
needed to connect the multiple building blocks of an identity management system.

.. note::

    The specified APIs in this |specification| can cover different use cases based on an organization requirement.
    The implementation of APIs in this |specification| should adhere to relevant security and compliance standards
    within an organization based on its security policy. Care should be taken to ensure that the APIs are secured
    with proper access control to ensure the privacy of user identities. The trust of the data
    as used in this |specification| is a function of the data source which means that authoritative sources
    such as government sources will be highly reliable.

The OSIA Initiative
-------------------

Launched by the not-for-profit Secure Identity Alliance, *Open Standard Identity APIs* (OSIA) is an
initiative created for the public good to address vendor lock-in problem.

OSIA addresses the vendor lock-in concern by providing a simple, open standards-based connectivity
layer between all key building blocks within the national identity ecosystem.

OSIA scope is as follows:

1. **Build a common understanding of the functional scope for identity systems building blocks** - NON PRESCRIPTIVE

   OSIA's first step has been to formalize the definitions, scope, and main functionalities of each
   building block within the identity management system.

2. **Create a set of standardized interfaces and data dictionary** - PRESCRIPTIVE

   For this core piece of work, OSIA is focused on developing the set of interfaces and standardized
   data dictionary needed to connect the multiple identity system building blocks and ensure seamless
   interactions via pre-defined services.

   It is then down to each government to define and implement the interaction processes between individual
   building blocks (which in turn determines which interfaces are associated with each building block),
   according to local laws and regulations.

With OSIA, governments are free to select the building blocks they need, from the suppliers they choose - without fear of lock in.

And because OSIA operates at the interface layer, interoperability is assured without the need to
rearchitect environments or rebuild solutions from the ground up. ID ecosystem building blocks are
simply swapped in and out as the use case demands - from best-of-breed options already available on the market.

This real-world approach dramatically reduces operational and financial risk, increases the effectiveness
of existing identity ecosystems, and rapidly moves government initiatives from proof of concept to live environments.

OSIA Benefits
-------------

The OSIA initiative offers a wide range of benefits to implementers of national ID management solutions.

1. **Unleash market innovation**

   OSIA establishes the conditions that support an equal marketplace and makes it possible for the wider
   identity community to collaborate in new ways.

    * Create a marketplace where all vendors can compete equally: OSIA operates at the interface layer
      and does not define - or therefore favor - any technology at the building block layer
      (which is typically where the differentiation among vendors takes place).

    * Support the emergence of new local market models featuring local suppliers and SMEs:
      like the Open Banking revolution, OSIA exposes high performing standardized interfaces that
      enable new use cases and market offers - from the simple to the complex.

    * Ensure product(s) compatibility after Mergers & Acquisitions: Market consolidation can often
      lead to major products being put into maintenance - leaving governments with little choice
      but to replace these. With OSIA, whatever the status of a product, it will continue to be
      interoperable with new offers.

2. **Enable identity as a service**

   OSIA empowers governments to build new inclusive eGovernment solutions that give citizens ease of
   access to public services or trusted digital ID schemes that extend the use of citizen ID into
   other online areas - such as banking and payments.

    * Driving digital ID market growth: OSIA facilitates the link between sovereign identity management
      solutions and digital identity solutions, like mobile ID, by standardizing the ad hoc interfaces
      that decouple providers of the ID management solution and the digital ID solution.

    * Reducing fraud within siloed databases/multiple ID systems: OSIA enables the secure and
      controlled flow of data and services, like ID deduplication and authentication, across multiple
      foundational and functional registries - even where these registries are run by separate
      ministries and government agencies.

   Governments are able to reduce public sector payroll fraud, leakage in social benefits, fraud associated
   with tax filing and ensure the integrity of the electoral process.

3. **Address integrator/vendor lock-in**

   OSIA enables governments to exert full control over their sovereign identity systems. So, they can
   pursue their national development agendas - without any fear of integrator/ vendor lock-in.
   Governments are no longer forced to implement a wall-to-wall solution from a single vendor and
   will not encounter compatibility difficulties when evolving their existing legacy solutions.
   They can:

    * Implement multi-vendor programs by mixing selected building blocks from different suppliers.
    * Extend legacy solutions or replace legacy building blocks(s) with a new building block(s)
      from a different supplier(s).

Diffusion, Audience, and Access
-------------------------------

This |specification| is hosted in `GitHub <https://github.com/SecureIdentityAlliance/osia>`_ and can be
downloaded from `ReadTheDocs <https://osia.readthedocs.io/en/latest/>`_.

This |specification| is licensed under `The SIA License <https://raw.githubusercontent.com/SecureIdentityAlliance/osia/master/LICENSE>`_.

Any country, technology partner or individual is free to download the functional and technical specifications to implement it in their customized foundational and sectoral ID systems or building blocks. Governments can also reference OSIA as Open Standards in tenders.Any country, technology partner or individual is free to download the functional and technical specifications to implement it in their customized foundational and sectoral ID systems or building blocks. Governments can also reference OSIA as Open Standards in tenders.

For more information on how to reference OSIA please see Section :ref:`osia-versions-ref`.

Convention and Typographical Rules
----------------------------------

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and
"OPTIONAL" in this document are to be interpreted as described in `RFC 2119 <http://www.ietf.org/rfc/rfc2119.txt>`_.

In the body of this |specification|, the words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in [IETF `RFC 2119 <http://www.ietf.org/rfc/rfc2119.txt>`_].

1. MUST: This word, or the terms "REQUIRED" or "SHALL", mean that the definition is an absolute requirement of the specification.
2. MUST NOT: This phrase, or the phrase "SHALL NOT", mean that the definition is an absolute prohibition of the specification.
3. SHOULD: This word, or the adjective "RECOMMENDED", mean that there may exist valid reasons in particular circumstances
   to ignore a particular item, but the full implications must be understood and carefully weighed before choosing a different course.
4. SHOULD NOT: This phrase, or the phrase "NOT RECOMMENDED" mean that there may exist valid reasons in particular circumstances
   when the particular behaviour is acceptable or even useful, but the full implications should be understood, and the case carefully weighed before implementing any behaviour described with this label.
5. MAY: This word, or the adjective "OPTIONAL", mean that an item is truly optional.

.. only:: itu

    A vendor may choose to include the item because a particular marketplace requires it or because the vendor feels that it enhances
    the product while another vendor may omit the same item. An implementation which does not include a particular option MUST
    be prepared to interoperate with another implementation which does include the option, though perhaps with reduced functionality.
    In the same vein, an implementation which does include a particular option MUST be prepared to interoperate with another
    implementation which does not include the option (except, of course, for the feature the option provides.)


Code samples highlighted in blocks appear like that:

.. code-block:: json

    {
        "key": "value",
        "another_key": 23
    }

