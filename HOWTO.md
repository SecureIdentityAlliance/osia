# How to Contribute

This is a small guide for the contributors, explaining how to change and build the OSIA documentation.

## Setup your build environment

This OSIA documentation is written in reStruturedText and built with Sphinx. There is no specific
tool to write it, just any text editor will do and many have a plugin to help and write reST syntax.

To build the documentation and check it before pushing it in Github, Sphinx must be installed.

1. Install Python 3.x (x>=5). Python 3.7, the latest version, is working fine.
2. Install Java 8. Java is required for PlantUML.
3. Install PlantUML version 1.2018.10 (available from http://plantuml.com/download).
   The command ``plantuml`` must be accessible.

4. (optional) Create a Python virtual environment:

   - Install virtualenv
   - Run:

     ```shell
        virtualenv -p python py4osia
        source py4osia/bin/activate
     ```
5. Install Sphinx and the required dependencies:

   ```shell
   pip install -r requirements
   ```

6. Fork the OSIA repository and clone locally your fork
7. Build the documentation running:

   ```shell
   sphinx-build -b html src/doc target/html
   ```
## Edit the documentation

The OSIA documentation is organized in text files, ech file corresponding to a chapter.

Sphinx syntax is explained here: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
You can also check http://www.sphinx-doc.org/en/master/usage/quickstart.html.

To add a new API in OSIA:

1. Isolate the functional description in a new file in directory `src/doc/functional`.
   There is already one file per API. Just copy & paste one to bootstrap a new one.
2. Reference (include) this functional description in the chapters 5 & 6.
3. Add the corresponding OpenAPI v3 YAML file in `src/doc/yaml` and add a file in `src/doc/annexes/technical/`
   referencing the yaml.
   Look for samples in the existing files.

