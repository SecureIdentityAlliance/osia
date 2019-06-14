# Open Source API for Sovereign ID Programs

_Accelerating the development of national identity schemes across the world_

[![Documentation Status](https://readthedocs.org/projects/osia/badge/?version=latest)](https://osia.readthedocs.io/en/latest/?badge=latest)

## Presentation

Official identification (ID) is more than a convenience; it is a fundamental human right that gives people access to education, financial services, employment, health and social welfare – and more. 

But creating a robust national ID system is no easy task. Members of the ID4Africa Movement, responsible for initiating modern ID systems to drive socio-economic development in the region, have highlighted how propriety ID technologies and a lack of technical standardization represent major challenges to those tasked with delivering national ID schemes. 

In response, the Secure Identity Alliance (SIA), a not-for-profit association supported by the world’s leading identity providers, has launched a landmark initiative to eliminate the interoperability challenges that currently hamper the evolution of national ID systems. 
By allowing multiple identity registries and systems to ‘talk’ to one another – independent of technology, solution architecture or vendor – the Open Source API makes it easier for governments to rollout national ID ecosystems in which multiple identity registries and systems operate together as a cohesive whole. 

Representing an industry-wide commitment to breaking down the technical barriers that, until now, have stood in the way of achieving the United Nations goal of establishing free and legal identity for every citizen by 2030, the Open Source API project makes it possible for governments to accelerate and advance their national ID programs. 

Programs that will empower citizens to assert their unique ID, facilitate the innovative delivery of public services, and usher in a new era of robust governance arrangements for all stakeholders.

See also https://secureidentityalliance.github.io/

## Building documentation

API documentation is written in reStruturedText and built with Sphinx.

You can read the latest version on https://osia.readthedocs.io/en/latest/

To build it yourself, prepare your environment:
```
pip install "Sphinx<2.0"
pip install sphinxcontrib-httpdomain sphinxcontrib-plantuml
pip install sphinx_rtd_theme
```

UML diagrams are built with PlantUML and Java 8. They must be installed separately.

Build:
```
sphinx-build -b html src/doc target/html
```
