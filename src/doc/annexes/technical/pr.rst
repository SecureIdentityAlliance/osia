
.. _annex-interface-pr:

Population Registry Management
------------------------------

.. only:: html

    Get the OpenAPI file for this interface: `pr.yaml <../../pr.yaml>`_

.. raw:: latex

    Get the OpenAPI file for this interface: \textattachfile[]{../html/pr.yaml}{pr.yaml}

.. sidebar:: Population Registry Services

    .. hlist::
        :columns: 2

        - `findPersons <#post--v1-persons>`_
        - `createPerson <#post--v1-persons-personId>`_
        - `readPerson <#get--v1-persons-personId>`_
        - `updatePerson <#put--v1-persons-personId>`_
        - `deletePerson <#delete--v1-persons-personId>`_
        - `mergePerson <#post--v1-persons-personIdTarget-merge-personIdSource>`_
        - `readIdentities <#get--v1-persons-personId-identities>`_
        - `createIdentity <#post--v1-persons-personId-identities>`_
        - `createIdentityWithId <#post--v1-persons-personId-identities-identityId>`_
        - `readIdentity <#get--v1-persons-personId-identities-identityId>`_
        - `updateIdentity <#put--v1-persons-personId-identities-identityId>`_
        - `partialUpdateIdentity <#patch--v1-persons-personId-identities-identityId>`_
        - `deleteIdentity <#delete--v1-persons-personId-identities-identityId>`_
        - `setIdentityStatus <#put--v1-persons-personId-identities-identityId-status>`_
        - `defineReference <#put--v1-persons-personId-identities-identityId-reference>`_
        - `readReference <#get--v1-persons-personId-reference>`_
        - `readGalleries <#get--v1-galleries>`_
        - `readGalleryContent <#get--v1-galleries-galleryId>`_

Services
""""""""
.. openapi:: ../../yaml/pr.yaml
    :examples:
    :group:

Data Model
""""""""""

:todo:`To be completed`

