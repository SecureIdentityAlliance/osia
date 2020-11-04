
.. _osia-versions-ref:

OSIA Versions & Referencing
===========================

There will be a version for each interface.
Each interface can be referenced in tenders as follows:

    ``OSIA v. [version] - [interface name] v. [version number]``

For instance below is the string to reference the *Notification* interface:

    ``OSIA v. 2.0 - Notification v. 1.0.0``

Below is the complete list of available interfaces with related version to date:

- OSIA v. |release| - Notification - v. :oasversion:`yaml/notification.yaml`
- OSIA v. |release| - UIN Management - v. :oasversion:`yaml/uin.yaml`
- OSIA v. |release| - Data Access - v. :oasversion:`yaml/dataaccess.yaml`
- OSIA v. |release| - Enrollment - v. :oasversion:`yaml/enrollment.yaml`
- OSIA v. |release| - Population Registry Management - v. :oasversion:`yaml/pr.yaml`
- OSIA v. |release| - Biometrics - v. :oasversion:`yaml/abis.yaml`
- OSIA v. |release| - Credential Services - v. :oasversion:`yaml/cms.yaml`
- OSIA v. |release| - Third Party Services - v. :todo:`TBD`

This document proposes as well a set of interfaces that could be used by each component (non-prescriptive).

As a consequence, it is possible to reference directly that set of interfaces bundled with a given component. 
It is possible to reference the bundle of these interfaces as follows:

    ``OSIA v. [version] – [component name] v. [version number]``

For instance for Civil Registry (CR) OSIA proposes the following set of interfaces:

- OSIA v. |release| - Notification - v. :oasversion:`yaml/notification.yaml`
- OSIA v. |release| - Data Access - v. :oasversion:`yaml/dataaccess.yaml`

Below is the string to reference this set of interfaces linked to CR:

    OSIA v. |release| – CR v. |release|

