# OSIA Initiative

_A digital public good, OSIA is an open standard set of interfaces (APIs) that enables seamless connectivity between building blocks of the identity management ecosystem - independent of technology, solution architecture or vendor._

[![Documentation Status](https://readthedocs.org/projects/osia/badge/?version=latest)](https://osia.readthedocs.io/en/latest/?badge=latest)

![SIA Logo](OSIA_Colour_Logo_RGB_400px.png "Secure Identity Alliance")

## Presentation

In 2019, the non-for-profit Secure Identity Alliance (SIA)[^1], launched the global OSIA initiative.

The aim of the OSIA Initiative is to develop a framework of open standards for the interoperability of foundational identity systems.
Around the globe, legal or official identity is the foundation of national security, social protection, and economic growth strategies.

As the identity market matures, technologies like digital identity, biometrics and cloud platforms are transforming the identity landscape. Making it possible to:
* enable national identity schemes that are truly inclusive and serve the needs of all stakeholders
* initiate the delivery of innovative digital public and private services.

To capture this opportunity without undue cost or time-consuming integration effort, governments need to be free to evolve, adapt, modernize, and add to their systems with confidence – and without fear of future compatibility issues.

Until recently, however, the initiation of highly functional and interoperable foundational identity systems that are easy to upgrade or change has been constrained by a siloed approach and lack of standardization that made it difficult to connect registries or exchange, consult, or update data between systems.

OSIA breaks silos and enables interoperability.

It also enables the all-important government industry collaborations needed to create the frameworks that make it possible to build truly open, innovative and future-proofed national identity systems, OSIA is transforming how governments leverage identity to deliver real-world impacts for their citizens and national economies.

[^1]: Secure Identity Alliance (SIA) is established as a non-profit association (N° 0785731573) pursuant to the Companies and Associations Code of 23 March 2019, published in the Belgian Official Gazette of 4 April 2019 with a registered office located in the Brussels-Capital Region. The disinterested goal of the non-profit association is to unify the ecosystem of identity (ID) and unlock the full power of identity so that people, economy, and society thrive. Representing ID actors and organisations active across the ID ecosystem and adjacent industries, the Association supports the development of the activities of its members across four broad pillars: Identity for Good, Outreach, Open Standards Development and Industry Services and Solutions.

See also https://secureidentityalliance.github.io/

## Building documentation

OSIA documentation is written in reStruturedText and built with Sphinx.

You can read the latest version on https://osia.readthedocs.io/en/latest/

To build it yourself, prepare your environment:

```
pip install Sphinx
pip install sphinxcontrib-httpdomain sphinxcontrib-plantuml sc-oa
```

UML diagrams are built with PlantUML and Java 8. They must be installed separately.

Build:

```
sphinx-build -b html src/doc target/html
```
