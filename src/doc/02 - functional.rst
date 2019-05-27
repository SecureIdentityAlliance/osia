
Functional View
===============

Components
----------

The components are:

- The *Enrolment* component. This component is :todo:`to do`.
- The *Population Registry* (PR) component. This component is :todo:`to do`.
- The *UIN Generator* component. This component is :todo:`to do`.
- The *ABIS* component. This component is :todo:`to do`.
- The *Civil Registry* (CR) component. This component is :todo:`to do`.
- The *Document Management System* (DMS) component. This component is :todo:`to do`.
- The *Third Parties Services* component. This component is :todo:`to do`.

.. list-table:: Components
    :header-rows: 1
    :widths: 30 30 30
    

    * - ID Ecosystem Component
      - Data
      - Functions
      
    * - Enrollment
      - - Alpha*
        - UIN*
        - History*
        - Supporting documents*
      - - Recording application
        - Collecting personal data 

    * - PR
      - - Alpha
        - UIN
        - History
        - Supporting documents
      - - Identity attributes storage
        - Identity Life cycle management
        
    * - UIN Gen
      - - Alpha
        - UIN
      - - UIN generation

    * - ABIS
      - - UIN
        - Biometric data (images and templates)
      - - Authentication (1:1)
        - Identification (1:N)
        - Quality control and adjudication

    * - CR
      - - Events
        - UIN
        - History
        - Supporting documents
      - - Events storage
        - Certificate production
        - Workflow

    * - DMS
      - - Alpha
        - UIN
        - History
        - Supporting documents
      - - Document data storage
        - Document Life cycle management
        - Document Production
        - Workflow
        - SMS and email server

    * - Third Parties Services
      - ?
      - KYC/auth

The components are represented on the following diagram:

.. figure:: images/components.*
    :width: 100%

    Components
    

Interfaces
----------

:todo:`To do`

This chapter describes the following interfaces.

- UIN management. This interface can be implemented by PR, by CR or by another system. We will consider it is provided
  by a system called *UIN Generator*.
- Notifications. When data is changed, a notification is sent and received by systems that registered for
  this type of events. For instance, PR can register for the events *birth* emitted by CR.
- Data access. A set of services to access data.

  The design is based on the following assumptions:

  #. All persons recorded in a registry have a :term:`UIN`. The UIN can be used as a key to access person data for all records.
  #. The registries (civil and population) are both considered as centralized systems that are connected. If the civil registry
     is architectured in a decentralized way, and it is often the case, one of its component must be centralized, connected to
     the network, and in charge of the exchanges with the population registry.
  #. Since theregistries are customized for each business needs, dictionaries must be explicitly
     defined to describe the attributes, the event types, and the document types. See :ref:`annex-interface-dataaccess`
     for the mandatory elements of those dictionaries.
  #. The relationship parent/child is not mandatory in the population registry. A population registry implementation may
     manage this relationship or may ignore it and rely on the civil registry to manage it.
  #. All persons are stored in the population registry. There is no record in the civil registry that is not also in
     the population registry.
  #. The interface does not expose biometric services. Usage of biometrics is optional and is described in other
     standards already defined.

- Biometrics.
- Third party. Identity based services implemented on top of Identity system mainly *Identity Verification* and
  *Identity Attribute* sharing.

Components vs Interfaces Mapping
--------------------------------

The interfaces described in this chapter are summarized in the following table:

.. table:: Components vs Interfaces Mapping
    :class: longtable
    :widths: 30 10 10 10 10 10 10 10 10
    
    =========================== ======= ======= =========== ======= ======= =========== =========== =======
    ..                          **Components**
    --------------------------- ---------------------------------------------------------------------------
    **Interfaces**              Enroll  PR      UIN gen.    ABIS    CR      ID Card     Funct. Reg  Third Parties
    =========================== ======= ======= =========== ======= ======= =========== =========== =======
    Notifications
    -------------------------------------------------------------------------------------------------------
    Notify event                        U                           U
    Subscribe                           U                   U       U       U           U
    Unsubscribe                         U                   U       U       U           U
    Event callback                      I                   I       I       I           I
    --------------------------- ------- ------- ----------- ------- ------- ----------- ----------- -------
    UIN Management
    -------------------------------------------------------------------------------------------------------
    Generate UIN                        U       I                   U       U
    --------------------------- ------- ------- ----------- ------- ------- ----------- ----------- -------
    Data Access
    -------------------------------------------------------------------------------------------------------
    Get Person Attributes       U       IU                  U       IU      U           U           U
    Match Person Attributes             IU                          IU      U           U           U
    Verify Person Attributes            IU                          IU      U           U           U
    Get Person UIN              U       IU                          IU      U           U
    Get document                        IU                          IU
    --------------------------- ------- ------- ----------- ------- ------- ----------- ----------- -------
    Biometrics
    -------------------------------------------------------------------------------------------------------
    Verify                      U                           I               U           U           U
    Identify                    U                           I               U           U           U
    Insert                              U                   I               U
    Read                                U                   I               U           U           U
    Update                              U                   I               U
    Delete                              U                   I               U
    Get Gallery                         U                   I               U           U
    Get Gallery content                 U                   I               U           U
    --------------------------- ------- ------- ----------- ------- ------- ----------- ----------- -------
    Third Party Services
    -------------------------------------------------------------------------------------------------------
    Verify ID                                                                                       I
    Identify ID                                                                                     I
    Get Attributes                                                                                  I
    Get Attributes set                                                                              I
    =========================== ======= ======= =========== ======= ======= =========== =========== =======

where:

- ``I`` is used when a service is implemented (provided) by a component
- ``U`` is used when a service is used (consumed) by a component

Use Cases - How to Use |project|
--------------------------------

:todo:`Introduction to be done`

Birth Use Case
""""""""""""""

.. uml::
    :caption: Birth Use Case
    :scale: 50%

    !include "skin.iwsd"
    hide footbox
    actor "Mother or Father" as parent
    participant "CR" as CR
    participant "PR" as PR
    participant "UIN Generator" as UINGen
    
    parent -> CR
    activate parent
    activate CR
    
    group 1. Checks
        CR -> PR: matchPersonAttributes(mother attributes)
        CR -> PR: matchPersonAttributes(father attributes)
        CR -> PR: getPersonAttributes(mother)
        CR -> PR: getPersonAttributes(father)
        CR -> PR: getPersonUIN(new born attributes)
        CR -> CR: Additional checks
    end
    
    group 2. Creation
        CR -> UINGen: createUIN()
        CR -> CR
        note right: register the birth

        CR -->> parent: certificate
        destroy parent
    end
    
    group 3. Notification
        CR ->> PR: notify(birth,UIN)
        deactivate CR

        ...
        
        PR -> CR: getPersonAttributes(new born)
        activate PR
        PR -> CR: getPersonAttributes(mother)
        PR -> CR: getPersonAttributes(father)
        PR -> PR
        note right: create/update identities
        deactivate PR
    end
  
1. Checks

   When a request is submitted, the CR may run checks against the data available in the PR using:

   - ``matchPersonAttributes``: to check the exactitude of the parents' attributes as known in the PR
   - ``getPersonAttributes``: to get missing data about the parents's identity
   - ``getPersonUIN``: to check if the new born is already known to PR or not

   How the CR will process the request in case of data discrepancy is specific to each CR implementation
   and not in the scope of this document.

2. Creation

   The birth is registered in the CR. The first step after the checks is to generate a new UIN
   a call to ``createUIN``.
    
3. Notification

   As part of the birth registration, it is the responsibility of the CR to notify other systems, including the PR,
   of this event using:
   
   - ``notify``: to send a *birth* along with the new ``UIN``.
   
   The PR, upon reception of the birth event, will update the identity registry with this new identity using:
    
   - ``getPersonAttributes``: to get the attributes of interest to the PR for the parents and the new child.

Death Use Case
""""""""""""""

:todo:`To be completed`

Marriage Use Case
"""""""""""""""""

:todo:`To be completed`

Deduplication
"""""""""""""

During the lifetime of a registry, it is possible that duplicates are detected. This can happen for instance
after the addition of biometrics in the system. When a registry considers that two records are actually the same
and decides to merge them, a notification must be sent.

.. uml::
    :caption: Deduplication Use Case
    :scale: 50%

    !include "skin.iwsd"
    hide footbox
    participant "PR" as PR
    participant "CR" as CR

    PR -> PR: deduplicate()
    activate PR

    PR ->> CR: notify(duplicate,[UIN])
    deactivate PR

    ...

    CR -> PR: getPersonAttributes(UIN)
    activate CR
    activate PR
    CR -> CR: merge()
    deactivate PR
    note right: merge/register duplicate
    deactivate CR
  
How the target of the notification should react is specific to each subsystem.

ID Card Request
"""""""""""""""

:todo:`To be completed`


Bank account opening Use Case
"""""""""""""""""""""""""""""

.. uml::
    :caption: Bank account opening Use Case
    :scale: 50%

    !include "skin.iwsd"
    hide footbox
    actor "Citizen" as citizen
    actor "Bank attendant" as bank
    participant "Third Party" as usage
    participant "PR" as PR
    
    citizen -> bank : Go to agency
    activate citizen
    activate bank
    
    group 1. Verify Identity
        citizen -> bank : UIN + Biometrics
        deactivate citizen
        activate usage
        bank -> usage : verifyIdentity(UIN, biometric or civil data or credential)
        usage -> bank : Y/N
        bank -> bank  : create account for UIN
    end
    group 2. Get certified Attributes
        bank -> usage : getAttributeSet (UIN, attribute set name)
        usage -> PR : getPersonAttributes(UIN)
        usage -> bank : List of attributes values
        note right: fill-in attributes in bank account
    end
    deactivate citizen
    deactivate bank

 
Police identity control Use Cases
"""""""""""""""""""""""""""""""""

.. uml::
    :caption: Collaborative identity control
    :scale: 50%

    !include "skin.iwsd"
    hide footbox
    actor "Citizen" as citizen
    actor "Policeman" as police
    participant "Third Party" as usage
    participant "ABIS" as ABIS
    participant "PR" as PR

    citizen -> police : Show ID card
    citizen -> police : Capture fingerprint
    activate citizen
    activate police

    group 1. Verify Identity
        citizen -> police : UIN + Biometrics
        deactivate citizen
        activate usage
        police -> usage : verifyIdentity(UIN, biometric or civil data or credential)
        usage -> police : Y/N
    end
    group 2. Show corresponding attributes
        police -> usage : getAttributeSet (UIN1, attribute set name)
        usage -> PR : getPersonAttributes(UIN1)
        usage -> police : List of attributes values
        police -> usage : getAttributeSet (UIN2, attribute set name)
        usage -> PR : getPersonAttributes(UIN2)
        usage -> police : List of attributes values
        police -> usage : getAttributeSet (UIN3, attribute set name)
        usage -> PR : getPersonAttributes(UIN3)
        usage -> police : List of attributes values
        note right: display attributes for each candidates
    end

.. uml::
    :caption: Non collaborative identity control
    :scale: 50%

    !include "skin.iwsd"
    hide footbox
    actor "Citizen" as citizen
    actor "Policeman" as police
    participant "Third Party" as usage
    participant "ABIS" as ABIS
    participant "PR" as PR

    citizen -> police : Show ID card
    citizen -> police : Capture fingerprint
    activate citizen
    activate police

    group 1. Verify Identity
        citizen -> police : UIN + Biometrics
        deactivate citizen
        activate usage
        police -> usage : verifyIdentity(UIN, biometric or civil data or credential)
        usage -> police : Y/N
    end
    group 2. Show corresponding attributes
        police -> usage : getAttributeSet (UIN1, attribute set name)
        usage -> PR : getPersonAttributes(UIN1)
        usage -> police : List of attributes values
        police -> usage : getAttributeSet (UIN2, attribute set name)
        usage -> PR : getPersonAttributes(UIN2)
        usage -> police : List of attributes values
        police -> usage : getAttributeSet (UIN3, attribute set name)
        usage -> PR : getPersonAttributes(UIN3)
        usage -> police : List of attributes values
        note right: display attributes for each candidates
    end



