
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = []
pygments_style = 'colorful'
project = 'Open Source API'
release = '1.0a'
author = 'SIA'
html_context = {'project':'Open Source API', 'version':"1.0a0", 'copyright':'SIA'}
html_show_sphinx = False

html_theme = "sphinx_rtd_theme"
html_logo = 'logo-secure-identity-alliance3.png'

extensions = ['sphinxcontrib.httpdomain','sphinxcontrib.plantuml']

plantuml_output_format = 'svg'
plantuml = r'java -jar c:\ohe\bin\plantuml.jar'

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


latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
 'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
 'pointsize': '10pt',

# Keep the figure where there are defined (no floating)
'figure_align':'H',

 # no raw string can contain '\u' (this is interpreted as unicode char)
 'preamble': u'''
\\usepackage{bbding,pifont} %% two dingbat fonts

\\DeclareUnicodeCharacter{2714}{\\Checkmark}
''',

  'atendofbody':u'''
  \\listoftables
  \\listoffigures
 ''',

'classoptions' : ',english,openany,oneside'
}
