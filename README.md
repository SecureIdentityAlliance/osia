# OSIA Initiative

_Putting government back in control: how the pioneering OSIA Initiative eliminates vendor lock-in and assures interoperability for sovereign identity programs today_

[![Documentation Status](https://readthedocs.org/projects/osia/badge/?version=latest)](https://osia.readthedocs.io/en/latest/?badge=latest)

![SIA Logo](OSIA_Colour_Logo_RGB_400px.png "Secure Identity Alliance")

## Presentation

Official identification (ID) is more than a convenience; it is a fundamental human right that gives people access to education, financial services, employment, health and social welfare – and more.

In this context, designing and deploying a national identity system that is resilient, flexible and sustainable is key. All too often, however, governments come to depend heavily on their technology partner(s). Their ability to transition to new suppliers or technologies, or to evolve and upgrade their systems, is hampered by contractual arrangements, a raft of technical issues and considerable operational risk.

Vendor lock-in in the identity domain is therefore a common problem and poses a real challenge – especially for countries across Africa, where multiple identity systems often proliferate.

In response, the Secure Identity Alliance (SIA), a not-for-profit association supported by the world’s leading identity providers, has launched OSIA, a landmark initiative to eliminate eliminates lock-in and assures interoperability for sovereign identity programs today. By allowing multiple identity registries and systems to ‘talk’ to one another – independent of technology, solution architecture or vendor – OSIA makes it easier for governments to rollout national ID ecosystems in which multiple identity registries and systems operate together as a cohesive whole.

Representing an industry-wide commitment to breaking down the technical barriers that, until now, have stood in the way of achieving the United Nations goal of establishing free and legal identity for every citizen by 2030, OSIA project makes it possible for governments to accelerate and advance their national ID programs.

See also https://secureidentityalliance.github.io/

## Building documentation

API documentation is written in reStruturedText and built with Sphinx.

You can read the latest version on https://osia.readthedocs.io/en/latest/

To build it yourself, prepare your environment:
```
pip install "Sphinx<2.0"
pip install sphinxcontrib-httpdomain sphinxcontrib-plantuml
```

UML diagrams are built with PlantUML and Java 8. They must be installed separately.

Build:
```
sphinx-build -b html src/doc target/html
```
