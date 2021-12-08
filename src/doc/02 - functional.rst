
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

  This component interfaces with external systems to leverage the identity databases
  for the benefits of individuals.
  It provides services to authenticate, identify, and access identity attributes for use cases such
  as KYC.
  
- The *Digital Credential Issuance & Distribution System*.

  This component is in charge of the issuance and delivery of the digital credentials built from
  the identity databases under the control of the CMS.
  

.. list-table:: Components
    :header-rows: 1
    :widths: 30 30 30
    

    * - ID Ecosystem Component
      - Data
      - Functions
      
    * - Enrollment
      - - Biographic data
        - UIN
        - History
        - Supporting documents
      - - Recording application
        - Collecting personal data

    * - PR
      - - Biographic data
        - UIN
        - History
        - Supporting documents
      - - Identity attributes storage
        - Identity Life cycle management
        
    * - UIN Gen
      - - Biographic data
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
      - - Biographic data
        - UIN
        - Biometric data
        - Credential event history
      - - Credential data storage
        - Credential Life cycle management
        - Credential Production
        - Workflow

    * - Third Party Services
      - - Biographic data/Identity attributes
        - Biometric data
      - - Authentication (1:1)
        - Identification (1:N)
        - Access to identity attributes
        
    * - Digital Credential Issuance & Distribution System
      -
      - - Issuance of a digital credential
        - Delivery of a digital credential

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

The following table describes in detail the interfaces and associated services.

.. table:: Interfaces List
    :class: longtable
    :widths: 30 70
    
    ================================= ===================================================================================
    **Services**                       **Description**
    ================================= ===================================================================================
    **Notification**
    ---------------------------------------------------------------------------------------------------------------------
    Subscribe                          Subscribe a URL to receive notifications sent to one topic
    List Subscription                  Get the list of all the subscriptions registered in the server
    Unsubscribe                        Unsubscribe a URL from the list of receiver for one topic
    Confirm                            Confirm that the URL used during the subscription is valid
    Create Topic                       Create a new topic
    List Topics                        List all the existing topics
    Delete Topic                       Delete a topic
    Publish                            Publish an event to all systems that have subscribed to this topic
    Notify                             Callback registered during subscription and called when an event is published
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
    Read Enrollment Processing Status  Retrieve the status of the processing done after finalization
    Read Enrollment Processing Data    Retrieve the data generated by the processing of the enrollment done after finalization
    Send Buffer                        Send a buffer (image, etc.)
    Get Buffer                         Get a buffer
    --------------------------------- -----------------------------------------------------------------------------------
    **Population Registry Services**
    ---------------------------------------------------------------------------------------------------------------------
    Find Persons                       Query for persons, using all the available identities
    Create Person                      Create a new person
    Read Person                        Read the attributes of a person
    Update Person                      Update a person
    Delete Person                      Delete a person and all its identities
    Merge Persons                      Merge two persons
    Move Identity                      Move one identity from one person to another one
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
    Merge Encounters                   Merge two sets of encounters
    Move Encounter                     Move one encounter from one person to another one
    Update Encounter Status            Set an encounter status
    Update Encounter Galleries         Set the galleries of an encounter
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
    Find Credentials                   Retrieve a list of credentials that match the passed in search criteria
    Read Credential                    Retrieve the attributes/status of an issued credential (smart card, mobile, passport, etc.)
    Suspend Credential                 Suspend an issued credential. For electronic credentials this will suspend any PKI certificates that are present
    Unsuspend Credential               Unsuspend an issued credential. For electronic credentials this will unsuspend any PKI certificates that are present
    Revoke Credential                  Revoke an issued credential. For electronic credentials this will revoke any PKI certificates that are present
    Set Credential Status              Change the credential status
    Find Credential Profiles           Retrieve a list of credential profils that match the passed in search criteria
    --------------------------------- -----------------------------------------------------------------------------------
    **ID Usage**
    ---------------------------------------------------------------------------------------------------------------------
    Verify ID                          Verify Identity based on UIN and set of attributes (biometric data, demographics, credential)
    Identify                           Identify a person based on a set of attributes (biometric data, demographics, credential)
    Read Attributes                    Read person attributes
    Read Attributes set                Read person attributes corresponding to a predefined set name
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
    **Interfaces**                     Enroll  Enroll    PR    UIN Gen  ABIS     CR      CMS    ID Usage
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
     Notify                                              I                I       I       I
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
    Read Enrollment Processing Status     U      I
    Read Enrollment Processing Data       U      I
    Send Buffer                           U      I
    Get Buffer                            U      I
    ---------------------------------  ------- ------- ------- ------- ------- ------- ------- -------
    **Population Registry Services**
    --------------------------------------------------------------------------------------------------
    Find Persons                                         I
    Create Person                                        I               U                U
    Read Person                                          I               U                U       U
    Update Person                                        I               U                U
    Delete Person                                        I               U                U
    Merge Persons                                        I               U
    Move Identity                                        I               U
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
    Merge Encounters                                     U                I
    Move Encounters                                      U                I
    Update Encounter Status                      U       U                I
    Update Encounter Galleries                   U       U                I
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
    Find Credentials                                                                      I
    Read Credential                                                                       I
    Suspend Credential                                                                    I
    Unsuspend Credential                                                                  I
    Revoke Credential                                                                     I
    Set Credential Status                                                                 I
    Find Credential Profiles                                                              I
    ---------------------------------  ------- ------- ------- ------- ------- ------- ------- -------
    **ID Usage**
    --------------------------------------------------------------------------------------------------
    Verify ID                                                                                     I
    Identify ID                                                                                   I
    Read Attributes                                                                               I
    Read Attributes set                                                                           I
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

.. uml::
    :caption: Death Use Case
    :scale: 50%

    hide footbox
    
    actor "Authorized Notifier" as notifier
    participant "CR" as CR
    participant "PR" as PR

    notifier -> CR
    activate notifier
    activate CR
    activate PR

    group 1. Identify
        CR -> PR: queryPersonUIN
        CR -> PR: matchPersonAttributes(subject attributes)
        CR -> PR: readPersonAttributes(subject)
        CR -> CR: Additional checks
    end

    group 2. Notify Death
        CR -> CR
        note right: report notification of the death
        CR -> notifier: Ask to confirm notification
        CR -> PR: updateIdentity
        CR -->> notifier: provisional certificate
    end

    group 3. Registration
        CR ->> PR: publish(death,UIN)      
        PR -> CR: readPersonAttributes(subject)
        PR -> PR
        note right: update identity
    end

    CR -> notifier: full death certificate available
    deactivate PR
    deactivate CR
    destroy notifier

1. Subject identification checks

   When a death notification is submitted by an authorized party, the CR shall run checks against the data available in the PR using:

   - ``matchPersonAttributes``: to check the exactitude of the subject's attributes as known in the PR
   - ``readPersonAttributes``: to get missing data about the subject's identity that 
   - ``queryPersonUIN``: to check if the person is already known to PR or not

   How the CR will process the request in case of data discrepancy is specific to each CR implementation
   and not in the scope of this document. The CR may implement an internal procedure to create a valid PR record retrospectively.

2. Notification creation

   The first step after the identity checks is to notify the life event status to the PR based on an identified record.
   At this point the death notification is recorded by not finally registered. Most states implement a waiting period.
   How the CR will process the death notification is specific to each CR implementation - a provisional certificate is possible.

3. Final registration

   When the PR finalizes the status of the subject's person record then the CR may publish this information at its discretion.
   The PR may maintain a list of interested parties who shall be informed of any finalized death status.
   A final certificate of death including the context of this event is typically issued by the CR to the notifier for distribution.

Deduplication Use Case
""""""""""""""""""""""

During the lifetime of a registry, it is possible that duplicates are detected. This can happen for instance
after the addition of biometrics in the system. When a registry considers that two records are actually the same
and decides to merge them, a notification must be sent.

.. uml::
    :caption: Deduplication Use Case
    :scale: 50%

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

ID Card Request Use Case (1)
""""""""""""""""""""""""""""

An ID card is one type of credential. The procedures surrounding credential issuance may involve
several sub-systems that contribute to the establishment of the applicant identity and the required data for the type of credential.

This use case assumes a simple starting scenario where the identity is known and can be validated,
mostly with data available from a Civil or Population Registry based Identity Provider.
These use cases also assume the use of a Credentials Management System (CMS) responsible for the
technical personalization and lifecycle management of a credential such as an ID card.

The use case aims to show how a selection of the CMS API calls can support a typical, use case in relation to CMS usage.

.. uml::
    :caption: ID Card Request Use Case (1)
    :scale: 50%

    hide footbox
    actor "Citizen" as citizen
    participant "Credential Provider" as CR
    participant "PR" as PR
    participant "CMS" as CMS
     
    citizen -> CR: Lost my ID - please replace
    activate citizen
    activate CR
   
    
    group 1. ID Card Check
        note left: if credential is a card
        activate PR
        CR -> PR: queryPersonUIN
        CR -> PR: matchPersonAttributes(subject attributes)
        CR -> PR: readPersonAttributes(subject)
        deactivate PR
        CR -> citizen: other transactions
        CR -> CR 
        note right: ID validation rules
    end
    
    group 2. Alt Suspend Credential
        CR -> CMS: SuspendCredentialRequest(CredentialID)
        activate CMS
        CMS -> CMS
        note right: e.g. suspend PKI certs
        CMS -->> CR: confirmation returned (e.g. code204, asynch)
        CR -> CMS: ReadCredentialRequest(RequestID get status)
    end
    
    group 3. Request Credential
        CR -> CR
        note right: build perso data payload
        CR -> CMS: CreateCredentialRequest(payload)
        CMS -->> CR: CredentialRequestID returned
    end
    
    citizen -> CR: "I just found my lost card"
    CR -> CMS: ReadCredentialRequest(RequestID get status)
    CMS -> CMS
    note right: CMS card lifecycle actions\ne.g. auto cancel old card if new issued
    CMS -> CR: card distribution
    deactivate CMS
    CR -> citizen: "Old Card cancelled. Collect new in 1 week"
    note right: message to citizen by Service Provider
    
    citizen -> CR: card collection
    deactivate CR
    destroy citizen

1. Identity Checks

   The example scenario assumes a credential provider service such as an ID card provider (National ID, Voter, &c).
   Such as service may access several OSIA API based components to establish an ID check. In this example the Population Register is used.
   This example case also assumes that the credential provider holds its own register of credentials issued to its subscribers.

2. Suspend Credential

   In the example above the citizen has lost a card and requests a replacement. The credential provider service
   first establishes the legitimacy of the citizen identity and the identity of the lost document within its own register.
   The next likely step in such a use case is to suspend the current credential. This is done using a CMS API call.
   The CMS confirms this step with a reference. In some use cases the reported lost credential may be cancelled immediately,
   but this is typically a decision made by the policy of the credential provider. There is an OSIA API call to both either or both requirements to the CMS.

3. Requesting a New Credential

   The credential provider is in this example case responsible for preparing the core document data for the CMS.
   The CMS itself may further process this data appropriate to the credential type: for example the CMS may be
   the service that signs this document data electronically.
   The CMS returns a new request ID to the credential provider service which will enable the provider to query credential production status within the CMS domain.
  
   Such a business process might be interrupted by an new event such as the citizen finding her lost card and
   wishing to cancel the replacement order, perhaps to avoid a replacement fee. Depending on the status returned
   by the CMS to the credential provider then the credential provider service will act accordingly in informing
   the citizen whether this is possible. In this case the citizen's card was already replaced by the CMS so the
   original card is now cancelled. 
  
   The CMS on its side is responsible for maintaining a credential profile which can be accessed by the CR at a later point.
   This use case stops for CMS when the card is distributed to the CR for collection by the citizen.


ID Card Request Use Case (2)
""""""""""""""""""""""""""""

A second ID Request use case shows how the CMS might expose more decisions to the credential providing service.
In this case it is the citizen facing provider that controls the cancellation of the lost document,
and this is not automated within the CMS component.

.. uml::
    :caption: ID Card Request Use Case (2)
    :scale: 50%

    hide footbox
    actor "Citizen" as citizen
    participant "Credential Provider" as CR
    participant "PR" as PR
    participant "CMS" as CMS
     
    citizen -> CR: Lost my ID - please replace
    activate citizen
    activate CR
    
    group 1. ID Card Check
        note left: if credential is a card
        activate PR
        CR -> PR: queryPersonUIN
        CR -> PR: matchPersonAttributes(subject attributes)
        CR -> PR: readPersonAttributes(subject)
        deactivate PR
        CR -> citizen: other transactions
        CR -> CR 
        note right: ID validation rules
    end
    
    group 2. Alt Suspend Credential
        CR -> CMS: SuspendCredentialRequest(CredentialID)
        activate CMS
        CMS -> CMS
        note right: e.g. suspend PKI certs
        CMS -->> CR: confirmation returned (e.g. code204, asynch)
        CR -> CMS: ReadCredentialRequest(RequestID get status)
    end
    
    group 3. Request Credential
        CR -> CR
        note right: build perso data payload
        CR -> CMS: CreateCredentialRequest(payload)
        CMS -->> CR: CredentialRequestID returned
    end

    citizen -> CR: "I just found my lost card"
    CR -> CMS: ReadCredentialRequest(RequestID get status)
        
    group 4. Alt Cancel Credential
        CR -> CMS: CancelCredentialRequest(CredentialID)
        note right: request for lost credential ID
        CMS -> CMS
        note right: CMS card lifecycle actions
        CMS -->> CR: confirmation returned (e.g. code204, asynch)
        CR -> CMS: ReadCredentialRequest(RequestID get status)
    end

    note right: option if cancellation \nnot automatic
    CMS -> CR: card distribution
    deactivate CMS
    CR -> citizen: "Old Card cancelled. Collect new in 1 week"
    note right: message to citizen by Service Provider

    citizen -> CR: card collection
    deactivate CR
    destroy citizen

This second example shows how APIs may be used to flex the control over functions such as credential
lifecycle management. This example first makes use of the API to suspend a credential pending
production of a replacement; then a second API call is made to the CMS to instruct cancellation of the lost document.

Credentials Issuance Use Case
"""""""""""""""""""""""""""""

This use case describes an example of interaction between the different OSIA components
to capture identity data, generate a UIN, process the identity data and issue both a 
physical and digital credential.

This use case also demonstrates what a middleware could do when connected to multiple OSIA compatible systems.
In this example the middleware is acting as an enrollment server, scheduling all the processing when
the data collection is finalized.

This use case was implemented for demonstrating OSIA and is presented in this `video <https://www.youtube.com/watch?v=U8mWKxIOiaE>`_.

.. uml::
    :caption: Credentials Issuance Use Case
    :scale: 50%

    hide footbox
    actor "Citizen" as citizen
    participant "Enrollment Station" as ENR
    participant "Middleware" as MW
    participant "PR" as PR
    participant "ABIS" as ABIS
    participant "CMS1" as CMS1
    participant "CMS2" as CMS2
     
    citizen -> ENR: biographics
    activate citizen
    activate ENR
    citizen -> ENR: documents
    citizen -> ENR: face
    citizen -> ENR: fingerprints
    citizen -> ENR: ok
    deactivate citizen

    ENR -> MW: createEnrollment(collected data)
    activate MW
    MW --> ENR: 201
    deactivate ENR

    MW -> MW: generate identity id

    MW -> PR++: generateUIN()
    return UIN

    MW -> PR++: createPerson(UIN)
    return 201
    MW -> PR++: createIdentityWithId(UIN, identityId, biographics, documents)
    return 201

    MW -> ABIS++: createEncounter(UIN, identityId, face, fingerprints)
    return 200

    MW -> CMS1: createCredentialRequest(UIN, identityId, biographics, face, fingerprints, type=Physical)
    activate CMS1
    CMS1 --> MW: 201

    MW -> CMS2: createCredentialRequest(UIN, identityId, biographics, face, fingerprints, type=Digital)
    activate CMS2
    CMS2 --> MW: 201
    deactivate MW

    ... Later ...

    CMS1 -> citizen: physical credential
    activate citizen
    deactivate CMS1

    CMS2 -> citizen: digital credential
    deactivate CMS2
    deactivate citizen

The main steps are:

#. The citizen interacts with the enrollment station to provide the biographic data, the supporting document
   images, a portrait and a set of fingerprints.
#. When all the data is collected, the full data set if pushed to the middleware using the OSIA ``createEnrollment`` service.
#. Backend processing includes:

   - interactions with the population registry to generate a UIN and insert the collected data,
   - interaction with the ABIS to insert the face and fingerprints,
   - interactions with multiple Credential Management System to request the issuance of different types of credentials.

Bank account opening Use Case
"""""""""""""""""""""""""""""

.. uml::
    :caption: Bank account opening Use Case
    :scale: 50%

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

Telco Customer Enrollment with ID document
""""""""""""""""""""""""""""""""""""""""""

.. uml::
    :caption: Telco Customer Enrollment with ID document
    :scale: 30%

    hide footbox
    
    actor "Customer" as user
    actor "Agent" as agent
    participant "Telco Enrollment Client" as TC
    participant "Telco Server" as TS
    participant "Third Party Services" as TPS


    activate user
    activate agent

    user -> agent: ask for SIM card and present ID doc
    agent -> TC: UIN, Identity info, live facial portrait, scan & ID of doc
    activate TC
        

    TC -> TS: UIN, Identity info, live facial portrait, scan & ID of doc
    activate TS

    TS -> TPS: checkCredentialDocument(UIN, Doc ID, Name, 1st name, DOB)
    note right: ID doc authenticity and\nvalidity verification
    activate TPS


    TPS --> TS: ok(proof of verification)
    deactivate TPS

    TS -> TPS: readCredentialAttributes(Id document ID)
    note right: Get the credential attributes\nsuch as expiration date
    activate TPS

    TPS --> TS: (issuing agency, issuing date, expiration date)
    deactivate TPS

    TS -> TPS: Authenticate Holder of ID doc(Live portrait, UIN, doc ID)
    note right: Compare person's live face\nagainst credential portrait

    TPS --> TS: ok(proof of verification)
    deactivate TPS

    TS -> TPS: readAttributes(UIN)
    activate TPS
    TPS -> TS: (Name, 1st name, DOC, Place of Birth, &c)
    note right: Get citizen attributes\nfor easier, error free\nenrollment
    deactivate TPS

    TS -> TS: new customer registration(identity info and proof of verification)

    TS -> TS: New customer registration (attributes, ID doc scan storage, proofs of verification)
    TS -> TC: Okfor SIM card(customerID)
    deactivate TS

    TC -> agent: continue SIM order
    deactivate TC

    agent -> user: continue SIM order
    destroy agent

    destroy user

1. Use case objective

   This use case allows a telco operator to check a citizen’s ID document and identity.
   
   The use case relies on an IDMS to check the authenticity and validity of the ID document
   presented by the citizen, then to check that he actually is the holder of the document.

2. Pre-conditions

   The citizen is registered in the IDMS and has a UIN.
   
   The citizen has a valid ID document.
   
   The citizen presents as a customer to the agent.
   
   The IDMS should support authentication token generation to protect against misusage of UIN.

3. Use case description

   The customer shows his ID document to the Agent. The Agent inputs (possibly by reading an MRZ on the document)
   the UIN, document ID, name, given name, DOB, and a live facial portrait taken of the citizen.
   
   The telco server calls an IDMS API to check if the information of the ID document is coherent and if the document is still valid.
   
   The telco server calls an IDMS API to get meta data of the document such as the issuing agency, the issuing date, expiration date, etc.
   
   The telco server calls an IDMS API to check if the customer is actually the holder of the document using his live biometric portrait.
   
   The telco server calls an IDMS API to get some reliable data of the customer in order to register him.

4. Result

   The citizen is now identified, authenticated and registered in a customer database and becomes eligible to buy a SIM card.
   
   The telco operator can prove regulatory controls have been applied for 'Know Your Customer' compliance.


Telco Customer Enrollment with no ID document
"""""""""""""""""""""""""""""""""""""""""""""

A customer applying for a new network SIM card may not be able to present an ID document as part of her application.

.. uml::
    :caption: Telco Customer Enrollment with no ID document
    :scale: 50%

    hide footbox
    actor "Customer" as user
    actor "Agent" as agent
    participant "Telco Enrollment Client" as TC
    participant "Telco Server" as TS
    participant "Third Party Services" as TPS

    activate user
    activate agent
    user -> agent: in person request for a SIM card
    agent -> TC: UIN, Identity info, live facial portrait
    activate TC

    TC -> TS: UIN, Identity info, live facial portrait
    activate TS

    TS -> TPS: verifyIdentity(UIN, Name, 1st name, DOB, portrait with liveness)
    note right: Thanks to his UIN\nthe citizen is identifed,\nand thanks to biometrics\nhe is authenticated
    activate TPS

    TPS --> TS: ok(proof of verification)

    TS -> TPS: readAttributes(UIN)
    note right: Get the identified and\nauthenticated citizen\nattributes
    activate TPS

    TPS --> TS: ok(Name, 1st name, DOC, Place of Birth, &c)
    deactivate TPS

    TS -> TS: new customer registration(identity info and proof of verification)

    TS -> TC: ok for SIM card(customer ID)
    deactivate TS

    TC -> agent: continue SIM order
    agent -> user: continue SIM order
    deactivate TC

    destroy agent
    destroy user


1. Use case objective

   This use case allows a telco operator to check a citizen’s identity and get his attributes
   relying on IDMS to check that the biometrics of the citizen matches with his UIN.

2. Pre-conditions

   The citizen is registered in the IDMS and has a UIN.
   
   The citizen biometrics are registered and associated to his UIN.
   
   The citizen presents as a customer to the agent.
   
   The IDMS should support authentication token generation to protect against misusage of UIN.

3. Use case description

   The Agent inputs the citizen’s UIN, Name, 1st Name, DOB and takes a live photo portrait of the customer.
   
   The telco server calls an IDMS API to check if the customer is actually the citizen corresponding to
   the given UIN thanks to his live portrait (face biometric matching).
   
   The telco server calls an IDMS API to get some reliable data of the customer in order to register him.

4. Result

   The citizen is now identified, authenticated and registered in a customer database and becomes eligible to buy a SIM card.
   
   The telco operator can prove regulatory controls have been applied for 'Know Your Customer' compliance.


.. rubric:: Footnotes

.. [#] *Handbook on Civil Registration and Vital Statistics Systems: Management, Operation and Maintenance,
   Revision 1, United Nations, New York, 2018, available at:*
   https://unstats.un.org/unsd/demographic-social/Standards-and-Methods/files/Handbooks/crvs/crvs-mgt-E.pdf *, para 65.*

.. [#] *Principles and Recommendations for a Vital Statistics System, United Nations publication
   Sales Number E.13.XVII.10, New York, 2014, paragraph 279*

