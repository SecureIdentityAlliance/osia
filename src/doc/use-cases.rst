
Use Cases
---------

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

Fœtal Death Use Case
""""""""""""""""""""

:todo:`To be completed`

Marriage Use Case
"""""""""""""""""

:todo:`To be completed`

Divorce Use Case
""""""""""""""""

:todo:`To be completed`

Annulment Use Case
""""""""""""""""""

:todo:`To be completed`

Separation Use Case
"""""""""""""""""""

:todo:`To be completed`

Adoption Use Case
"""""""""""""""""

:todo:`To be completed`

Legitimation Use Case
"""""""""""""""""""""

:todo:`To be completed`

Recognition Use Case
""""""""""""""""""""

:todo:`To be completed`

Change of Name/Gender Use Case
""""""""""""""""""""""""""""""

:todo:`To be completed`

Transcription Use Case
""""""""""""""""""""""

:todo:`To be completed`

Change of Nationality Use Case
""""""""""""""""""""""""""""""

(To be confirmed)

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

Bank account opening Use Case
"""""""""""""""""""""""""""""

.. uml::
    :caption: Bank account opening Use Case
    :scale: 50%

    !include "skin.iwsd"
    hide footbox
    actor "Citizen" as citizen
    actor "Bank attendant" as bank
    participant "USAGE" as Uuage
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
    participant "USAGE" as Uuage
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
    participant "USAGE" as Usage
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

