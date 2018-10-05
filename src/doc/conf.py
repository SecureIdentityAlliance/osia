
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = []
pygments_style = 'colorful'
html_context = {'project':'SIA CR-CI Interface', 'version':"Interface Specification<br/>1.0a0", 'copyright':'SIA'}
html_show_sphinx = False

html_theme = "sphinx_rtd_theme"
html_logo = 'logo-secure-identity-alliance3.png'

extensions = ['sphinxcontrib.httpdomain','sphinxcontrib.plantuml']

plantuml_output_format = 'svg'

