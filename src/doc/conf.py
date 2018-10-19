
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = []
pygments_style = 'colorful'
html_context = {'project':'Open Source API', 'version':"1.0a0", 'copyright':'SIA'}
html_show_sphinx = False

html_theme = "sphinx_rtd_theme"
html_logo = 'logo-secure-identity-alliance3.png'

extensions = ['sphinxcontrib.httpdomain','sphinxcontrib.plantuml']

plantuml_output_format = 'svg'

rst_prolog = '''

.. meta::
  :http-equiv=X-UA-Compatible: IE=9    

.. |tick|   unicode:: U+2714 .. HEAVY CHECK MARK

.. role:: todo

.. raw:: html

    <style>
        .todo {background-color: #f3f375;font-style: italic;}
    </style>

'''


