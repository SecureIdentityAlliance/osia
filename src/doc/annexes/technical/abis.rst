
.. _annex-interface-abis:

Biometrics
----------

This is version :oasversion:`../../yaml/abis.yaml` of this interface.

.. only:: html

    Get the OpenAPI file: `abis.yaml <../../abis.yaml>`_

.. raw:: latex

    Get the OpenAPI file: \textattachfile[]{../html/abis.yaml}{abis.yaml}

.. sidebar:: Biometrics Services

    .. hlist::
        :columns: 2

        - `createEncounterNoIds <#post--v1-persons>`_
        - `createEncounterNoId <#post--v1-persons-personId-encounters>`_
        - `readAllEncounters <#get--v1-persons-personId-encounters>`_
        - `createEncounter <#post--v1-persons-personId-encounters-encounterId>`_
        - `readEncounter <#get--v1-persons-personId-encounters-encounterId>`_
        - `updateEncounter <#put--v1-persons-personId-encounters-encounterId>`_
        - `deleteEncounter <#delete--v1-persons-personId-encounters-encounterId>`_
        - `mergeEncounter <#post--v1-persons-personIdTarget-merge-personIdSource>`_
        - `updateEncounterStatus <#put--v1-persons-personId-encounters-encounterId-status>`_
        - `updateEncounterGalleries <#put--v1-persons-personId-encounters-encounterId-galleries>`_
        - `readTemplate <#get--v1-persons-personId-encounters-encounterId-templates>`_
        - `deleteAll <#delete--v1-persons-personId>`_
        - `identify <#post--v1-identify-galleryId>`_
        - `identifyFromId <#post--v1-identify-galleryId-personId>`_
        - `verifyFromId <#post--v1-verify-galleryId-personId>`_
        - `verifyFromBio <#post--v1-verify>`_
        - `readGalleries <#get--v1-galleries>`_
        - `readGalleryContent <#get--v1-galleries-galleryId>`_

Services
""""""""
.. openapi:: ../../yaml/abis.yaml
    :examples:
    :group:

Data Model
""""""""""

:todo:`To be completed`

