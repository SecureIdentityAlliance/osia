
Functional View
===============

Components: Standardized Definition and Scope
---------------------------------------------

OSIA provides seamless interconnection between multiple components part of the identity ecosystem.

The components are defined as follows:

- The *Enrollment* component.

  Enrollment is defined as a system to register biographic and
  biometric data of individuals.

- The *Population Registry* (PR) component.

  Population registry is defined as "an individualized data system, that is, a mechanism of continuous recording,
  or of coordinated linkage, of selected information pertaining to each member of the resident population
  of a country in such a way to provide the possibility of determining up-to-date information concerning
  the size and characteristics of that population at selected time intervals. The population register is
  the product of a continuous process, in which notifications of certain events, which may have been
  recorded originally in different administrative systems, are automatically linked on a current basis.
  A. method and sources of updating should cover all changes so that the characteristics of individuals in the
  register remain current. Because of the nature of a population register, its organization, and also
  its operation, must have a legal basis." [#]_

- The *UIN Generator* component.

  UIN generator is defined as a system to generate and manage unique identifiers.

- The *Automated Biometric Identification System* (ABIS) component.

  An ABIS is defined as a *system to detect
  the identity of an individual when it is unknown, or to verify the individual's identity when it is
  provided, through biometrics*.

- The *Civil Registry* (CR) component.

  Civil registration is defined as "the continuous, permanent, compulsory and universal recording of the occurrence
  and characteristics of vital events pertaining to the population, as provided through decree or regulation
  is accordance with the legal requirement in each country.
  Civil registration is carried out primarily for the purpose of establishing the documents provided by the law." [#]_

- The *Credential Management System* (CMS) component.

  CMS is defined as a system to manage the production and
  issuance of credentials such as ID Cards, passports, driving licenses, digital ID, etc.

- The *Third Party Services* component.

  :todo:`TBD`

.. list-table:: Components
    :header-rows: 1
    :widths: 30 30 30
    

    * - ID Ecosystem Component
      - Data
      - Functions
      
    * - Enrollment
      - - Alpha
        - UIN
        - History
        - Supporting documents
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

    * - CMS
      - - Alpha
        - UIN
        - History
        - Supporting documents
      - - Credential data storage
        - Credential Life cycle management
        - Credential Production
        - Workflow
        - SMS and email server

    * - Third Party Services
      - :todo:`TBD`
      - KYC/auth

The components are represented on the following diagram:

.. figure:: images/components.*
    :width: 100%

    Components identified as part of the identity ecosystem
    

Interfaces
----------

This chapter describes the following interfaces:

- Notification

  A set of services to manage notifications for different types of events as for instance birth and death.

- Data access

  A set of services to access data.

  The design is based on the following assumptions:

  #. All persons recorded in a registry have a UIN. The UIN can be used as a key to access person data for all records.
     Please note that the UIN is the same throughout all registries (see Chapter 3 - Security & Privacy).
  #. The registries (civil, population, or other) are considered as centralized systems that are connected.
     If one registry is architectured in a decentralized way, one of its component must be centralized, connected to the network, 
     and in charge of the exchanges with the other registries.
  #. Since the registries are customized for each business needs, dictionaries must be explicitly defined to describe the attributes, 
     the event types, and the document types. See Data Access for samples of those dictionaries.
  #. The relationship parent/child is not mandatory in the population registry. A population registry implementation may manage this 
     relationship or may ignore it and rely on the civil registry to manage it.
  #. All persons are stored in the population registry. There is no record in the civil registry that is not also in the population registry.

- UIN Management

  A set of services to manage the unique identifier.

-  Enrollment Services

  A set of services to manage biographic and biometric data upon collection.

- Population Registry Services

  A set of services to manage a registry of the population.

- Biometrics

  A set of services to manage biometric data and databases.

- Credential Services

  A set of services to manage credentials, physical and digital.

- ID Usage

  A set of services implemented on top of identity systems to favour third parties consumption of identity data.

- Under discussion

  A set of services under discussion and not yet linked to any specific tag.

The following table describes in detail the interfaces and associated services.

.. table:: Interfaces List
    :class: longtable
    :widths: 30 70
    
    ================================= ===================================================================================
    **Services**                       **Description**
    --------------------------------- -----------------------------------------------------------------------------------
    **Notification**
    ---------------------------------------------------------------------------------------------------------------------
    Subscribe                          Subscribe a URL to receive notifications sent to one topic
    List Subscription                  Get the list of all the subscriptions registered in the server
    Unsubscribe                        Unsubscribe a URL from the list of receiver for one topic
    Confirm                            Confirm that the URL used during the subscription is valid
    Create Topic                       Create a new topic
    List Topics                        List all the existing topics
    Delete Topic                       Delete a topic
    Publish                            Notify of a new event all systems that subscribed to this topic
    --------------------------------- -----------------------------------------------------------------------------------
    **Data Access**
    ---------------------------------------------------------------------------------------------------------------------
    Read Person Attributes             Read person attributes
    Match Person Attributes            Check the value of attributes without exposing private data
    Verify Person Attributes           Evaluate simple expressions on person’s attributes without exposing private data
    Query Person UIN                   Query the persons by a set of attributes, used when the UIN is unknown
    Query Person List                  Query the persons by a list of attributes and their values
    Read document                      Read in a selected format (PDF, image, etc.) a document such as a marriage certificate
    --------------------------------- -----------------------------------------------------------------------------------
    **UIN Management**
    ---------------------------------------------------------------------------------------------------------------------
    Generate UIN                       Generate a new UIN
    --------------------------------- -----------------------------------------------------------------------------------
    **Enrollment Services**
    ---------------------------------------------------------------------------------------------------------------------
    Create Enrollment                  Insert a new enrollment
    Read Enrollment                    Retrieve an enrollment
    Update Enrollment                  Update an enrollment
    Partial Update Enrollment          Update part of an enrollment
    Finalize Enrollment                Finalize an enrollment (mark it as completed)
    Delete Enrollment                  Delete an enrollment
    Find Enrollments                   Retrieve a list of enrollments which match passed in search criteria
    Send Buffer                        Send a buffer (image, etc.)
    Get Buffer                         Get a buffer
    --------------------------------- -----------------------------------------------------------------------------------
    **Population Registry Services**
    ---------------------------------------------------------------------------------------------------------------------
    Create Person                      Create a new person
    Read Person                        Read the attributes of a person
    Update Person                      Update a person
    Delete Person                      Delete a person and all its identities
    Merge Persons                      Merge two persons
    Create Identity                    Create a new identity in a person
    Read Identity                      Read one or all the identities of one person
    Update Identity                    Update an identity. An identity can be updated only in the status claimed
    Partial Update Identity            Update part of an identity. Not all attributes are mandatory. 
    Delete Identity                    Delete an identity
    Set Identity Status                Set an identity status
    Define Reference                   Define the reference identity of one person
    Read Reference                     Read the reference identity of one person
    Read Galleries                     Read the ID of all the galleries
    Read Gallery Content               Read the content of one gallery, i.e. the IDs of all the records linked to this gallery
    --------------------------------- -----------------------------------------------------------------------------------
    **Biometrics**
    ---------------------------------------------------------------------------------------------------------------------
    Create Encounter                   Create a new encounter. No identify is performed
    Read Encounter                     Read the data of an encounter
    Update Encounter                   Update an encounter
    Delete Encounter                   Delete an encounter
    Merge Encounter                    Merge two sets of encounters
    Set Encounter Status               Set an encounter status
    Read Template                      Read the generated template
    Read Galleries                     Read the ID of all the galleries
    Read Gallery content               Read the content of one gallery, i.e. the IDs of all the records linked to this gallery
    Identify                           Identify a person using biometrics data and filters on biographic or contextual data
    Verify                             Verify an identity using biometrics data
    --------------------------------- -----------------------------------------------------------------------------------
    **Credential Services**
    ---------------------------------------------------------------------------------------------------------------------
    Create Credential Request          Request issuance of a secure credential
    Read Credential Request            Retrieve the data/status of a credential request
    Update Credential Request          Update the requested issuance of a secure credential
    Delete Credential Request          Delete/cancel the requested issuance of a secure document / credential
    Read Credential                    Retrieve the attributes/status of an issued credential (smart card, mobile, passport, etc.)
    Suspend Credential                 Suspend an issued credential. For electronic credentials this will suspend any PKI certificates that are present
    Unsuspend Credential               Unsuspend an issued credential. For electronic credentials this will unsuspend any PKI certificates that are present
    Cancel Credential                  Cancel an issued credential. For electronic credentials this will revoke any PKI certificates that are present  
    --------------------------------- -----------------------------------------------------------------------------------
    **ID Usage**
    ---------------------------------------------------------------------------------------------------------------------
    Verify ID                          Verify Identity based on UIN and set of attributes (biometric data, demographics, credential)
    Identify                           Identify a person based on a set of attributes (biometric data, demographics, credential)
    Read Attributes                    Read person attributes
    Read Attributes set                Read person attributes corresponding to a predefined set name
    --------------------------------- -----------------------------------------------------------------------------------
    **Under discussion**
    ---------------------------------------------------------------------------------------------------------------------
    List Credential Profiles           Retrieve the list of credential profiles
    Read Credential Profiles           Retrieve the credential profile
    Update Document Val Status         Updates the status of a document validation
    Read Document Val Status           Retrieve the status of a document validation
    Update Biometric Val Status        Updates the status of a biometric validation
    Read Biometric Val Status          Retrieve the status of a biometric validation
    Update Biographic Val Status       Updates the status of a biographic validation
    Read Biographic Val Status         Retrieve the status of a biographic validation   
    ================================= ===================================================================================   

Components vs Interfaces Mapping
--------------------------------

The interfaces described in the following chapter can be mapped against ID ecosystem components as per the table below:

.. table:: Components vs Interfaces Mapping
    :class: longtable
    :widths: 30 10 10 10 10 10 10 10 10
    

    =================================  ======= ======= ======= ======= ======= ======= ======= =======
       ..                              **Components**
    ---------------------------------  ---------------------------------------------------------------
    **Interfaces**                     Enroll  Enroll    PR    UIN Gen  ABIS     CR      CMS    3rd PS
                                       Clt     Srv
    =================================  ======= ======= ======= ======= ======= ======= ======= =======
    **Notification**
    --------------------------------------------------------------------------------------------------
     Subscribe                                           U                U       U       U
     List Subscription                                   U                U       U       U
     Unsubscribe                                         U                U       U       U
     Confirm                                             U                U       U       U
     Create Topic                                        U                U       U       U
     List Topics                                         U                U       U       U
     Delete Topic                                        U                U       U       U
     Publish                                             U                U       U       U
    ---------------------------------  ------- ------- ------- ------- ------- ------- ------- -------
    **Data Access**
    --------------------------------------------------------------------------------------------------
     Read Person Attributes                       U      IU               U       IU              U
     Match Person Attributes                      U      IU                       IU              U
     Verify Person Attributes                     U      IU                       IU              U
     Query Person UIN                             U      IU                       IU              U
     Query Person List                                                            U               U
     Read Document                                U      IU                       IU              U
    ---------------------------------  ------- ------- ------- ------- ------- ------- ------- -------
    **UIN Management**
    --------------------------------------------------------------------------------------------------
     Generate UIN                                         U       I               U
    ---------------------------------  ------- ------- ------- ------- ------- ------- ------- -------
    **Enrollment Services**
    --------------------------------------------------------------------------------------------------
    Create Enrollment                     U      I
    Read Enrollment                       U      I
    Update Enrollment                     U      I
    Partial Update Enrollment             U      I
    Finalize Enrollment                   U      I
    Delete Enrollment                     U      I
    Find Enrollments                      U      I
    Send Buffer                           U      I
    Get Buffer                            U      I
    ---------------------------------  ------- ------- ------- ------- ------- ------- ------- -------
    **Population Registry Services**
    --------------------------------------------------------------------------------------------------
    Create Person                                        I               U                U
    Read Person                                          I               U                U       U
    Update Person                                        I               U                U
    Delete Person                                        I               U                U
    Merge Person                                         I               U
    Create Identity                                      I
    Read Identity                                        I
    Update Identity                                      I
    Partial Update Identity                              I
    Delete Identity                                      I
    Set Identity Status                                  I
    Define Reference                                     I
    Read Reference                                       I
    Read Galleries                                       I
    Read Gallery Content                                 I
    ---------------------------------  ------- ------- ------- ------- ------- ------- ------- -------
    **Biometrics**
    --------------------------------------------------------------------------------------------------
    Create Encounter                             U       U                I
    Read Encounter                               U       U                I                      U
    Update Encounter                             U       U                I
    Delete Encounter                             U       U                I
    Merge Encounter                                      U                I
    Set Encounter Status                         U       U                I
    Read Template                                U       U                I
    Read Galleries
    Read Gallery Content                         U       U                I
    Identify                                     U                        I                      U
    Verify                                       U                        I                      U
    ---------------------------------  ------- ------- ------- ------- ------- ------- ------- -------
    **Credential Services**
    --------------------------------------------------------------------------------------------------
    Create Credential Request                                                             I
    Read Credential Request                                                               I
    Update Credential Request                                                             I
    Delete Credential Request                                                             I
    Read Credential                                                                       I
    Suspend Credential                                                                    I
    Unsuspend Credential                                                                  I
    Cancel Credential                                                                     I
    ---------------------------------  ------- ------- ------- ------- ------- ------- ------- -------
    **ID Usage**
    --------------------------------------------------------------------------------------------------
    Verify ID                                                                                     I
    Identify ID                                                                                   I
    Read Attributes                                                                               I
    Read Attributes set                                                                           I
    ---------------------------------  ------- ------- ------- ------- ------- ------- ------- -------
    **Under discussion**
    --------------------------------------------------------------------------------------------------
    List Cred Profiles
    Read Cred Profiles
    Update Document Val Status
    Read Document Val Status
    Update Biometric Val Status
    Read Biometric Val Status
    Update Biographic Val Status
    Read Biographic Val Status
    =================================  ======= ======= ======= ======= ======= ======= ======= =======

where:

- ``I`` is used when a service is implemented (provided) by a component
- ``U`` is used when a service is used (consumed) by a component

Use Cases - How to Use |project|
--------------------------------

Below are a set of examples of how OSIA interfaces could be implemented in various use cases.

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
        CR -> PR: readPersonAttributes(mother)
        CR -> PR: readPersonAttributes(father)
        CR -> PR: queryPersonUIN(new born attributes)
        CR -> CR: Additional checks
    end
    
    group 2. Creation
        CR -> UINGen: generateUIN()
        CR -> CR
        note right: register the birth

        CR -->> parent: certificate
        destroy parent
    end
    
    group 3. Notification
        CR ->> PR: publish(birth,UIN)
        deactivate CR

        ...
        
        PR -> CR: readPersonAttributes(new born)
        activate PR
        PR -> CR: readPersonAttributes(mother)
        PR -> CR: readPersonAttributes(father)
        PR -> PR
        note right: create/update identities
        deactivate PR
    end
  
1. Checks

   When a request is submitted, the CR may run checks against the data available in the PR using:

   - ``matchPersonAttributes``: to check the exactitude of the parents' attributes as known in the PR
   - ``readPersonAttributes``: to get missing data about the parents's identity
   - ``qureyPersonUIN``: to check if the new born is already known to PR or not

   How the CR will process the request in case of data discrepancy is specific to each CR implementation
   and not in the scope of this document.

2. Creation

   The first step after the checks is to generate a new UIN. To do so, the CR requests a new UIN to the PR using generateUIN service.
   At this point the birth registration takes place.
   How the CR will process the birth registration is specific to each CR implementation and not in the scope of this document.
    
3. Notification

   As part of the birth registration, it is the responsibility of the CR to notify other systems, including the PR,
   of this event using:
   
   - ``publish``: to send a *birth* along with the new ``UIN``.
   
   The PR, upon reception of the birth event, will update the identity registry with this new identity using:
    
   - ``readPersonAttributes``: to get the attributes of interest to the PR for the parents if relevant and the new child.

Death Use Case
""""""""""""""

:todo:`To be completed`

Marriage Use Case
"""""""""""""""""

:todo:`To be completed`

Deduplication Use Case
""""""""""""""""""""""

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

    CR -> PR: readPersonAttributes(UIN)
    activate CR
    activate PR
    CR -> CR: merge()
    deactivate PR
    note right: merge/register duplicate
    deactivate CR
  
How the target of the notification should react is specific to each subsystem.

ID Card Request Use Case
""""""""""""""""""""""""

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
    participant "Third Party Services" as usage
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
        bank -> usage : readAttributeSet (UIN, attribute set name)
        usage -> PR : readPersonAttributes(UIN)
        usage -> bank : List of attributes values
        note right: fill-in attributes in bank account
    end
    deactivate citizen
    deactivate bank

 
Police identity control Use Case
""""""""""""""""""""""""""""""""

.. uml::
    :caption: Collaborative identity control
    :scale: 50%

    !include "skin.iwsd"
    hide footbox
    actor "Citizen" as citizen
    actor "Policeman" as police
    participant "Third Party Services" as usage
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
        police -> usage : readAttributeSet (UIN1, attribute set name)
        usage -> PR : readPersonAttributes(UIN1)
        usage -> police : List of attributes values
        police -> usage : readAttributeSet (UIN2, attribute set name)
        usage -> PR : readtPersonAttributes(UIN2)
        usage -> police : List of attributes values
        police -> usage : readAttributeSet (UIN3, attribute set name)
        usage -> PR : readPersonAttributes(UIN3)
        usage -> police : List of attributes values
        note right: display attributes for each candidate
    end

.. rubric:: Footnotes

.. [#] *Handbook on Civil Registration and Vital Statistics Systems: Management, Operation and Maintenance,
   Revision 1, United Nations, New York, 2018, available at:*
   https://unstats.un.org/unsd/demographic-social/Standards-and-Methods/files/Handbooks/crvs/crvs-mgt-E.pdf *, para 65.*

.. [#] *Principles and Recommendations for a Vital Statistics System, United Nations publication
   Sales Number E.13.XVII.10, New York, 2014, paragraph 279*

