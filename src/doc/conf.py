
# (c) Secure Identity Alliance

import datetime

source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = []
pygments_style = 'colorful'
project = 'OSIA'
release = '3.0.0'
author = 'SIA'

numfig = True

extensions = ['sphinxcontrib.httpdomain','sphinxcontrib.plantuml','sphinxcontrib.openapi']

plantuml_output_format = 'svg'

exclude_patterns = ['_*.rst', '*/_*.rst']

rst_prolog = '''

.. meta::
  :http-equiv=X-UA-Compatible: IE=9    

.. |tick|   unicode:: U+2714 .. HEAVY CHECK MARK
.. |project| replace:: OSIA

.. role:: todo

.. raw:: html

    <style>
        .todo {background-color: #f3f375;font-style: italic;}

        /* override table width restrictions */
        .wy-table-responsive table td, .wy-table-responsive table th {
            /* !important prevents the common CSS stylesheets from
            overriding this as on RTD they are loaded after this stylesheet */
            white-space: normal !important;
        }

        .wy-table-responsive {
            overflow: visible !important;
        }
        
    </style>

'''

#
# HTML Output Configuration
#
html_static_path = ['images']
html_theme = "alabaster"
html_theme_options = {
    'logo': 'logo.svg',
    'github_user': 'SecureIdentityAlliance',
    'github_repo': 'osia',
    'github_button': True,
    'show_powered_by': False,
    'show_relbars': True,
    'fixed_sidebar': False,
}
html_show_sourcelink = False
html_context = {'project':'OSIA', 'version':release, 'copyright':'Secure Identity Alliance, '+str(datetime.date.today().year)}
html_last_updated_fmt = '%b %d, %Y'
html_extra_path = ['yaml']

#
# Latex/PDF Output Configuration
#

# use small font for source code
# XXX investigate if it is possible to customize \sphinxVerbatim environment 
from sphinx.highlighting import PygmentsBridge
from pygments.formatters.latex import LatexFormatter
 
class CustomLatexFormatter(LatexFormatter):
    def __init__(self, **options):
        super(CustomLatexFormatter, self).__init__(**options)
        self.verboptions = r"formatcom=\footnotesize"
 
PygmentsBridge.latex_formatter = CustomLatexFormatter

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
\\usepackage{attachfile}

\\attachfilesetup{author=Secure Identity Alliance,color=0 0.5 0.5,icon=paperclip,mimetype=application/json}

\\DeclareUnicodeCharacter{2714}{\\Checkmark}
\\newcommand{\\DUroletodo}[1]{\\colorbox{yellow}{#1} }

''' + ur'''

\newcommand{\companylogo}{
\includegraphics [ width=3.5cm] {logo.pdf}
}
\newcommand{\companylogobig}{
\includegraphics [ width=10cm] {logo2.pdf}
}

%% HEADER-FOOTER
%%\fancypagestyle{plain}{
%%   \fancyhead[L]{ \companylogo }
%%}
%%\fancypagestyle{normal}{
%%    \fancyhead[L]{ \companylogo }
%%}

%% TITLE
\newcommand{\osiamaketitle}{
  \begin{titlepage}
    \let\footnotesize\small
    \let\footnoterule\relax
    \begin{center}
        {\vspace{0.5cm} \companylogo }
        \vspace{1.5cm}
        \par
        {\rm\Huge\sffamily\bfseries {\textcolor[rgb]{0.678,0.325,0.537}{Specifications version '''+release+ur'''} } \par}
        \vfill
        %% Project logo
        \includegraphics[ width=12cm]{logo2.pdf} \par
        \vfill
        \small {\textcolor[rgb]{0.678,0.325,0.537}{\textcopyright Secure Identity Alliance, '''+str(datetime.date.today().year)+ur''' } }
    \end{center}    
        
    \par
  \end{titlepage}
  \cleardoublepage
  \setcounter{footnote}{0}
  \relax\let\maketitle\relax
}

''',

  'maketitle': r'\osiamaketitle',
  'atendofbody':u'''
  \\listoftables
  \\listoffigures
 ''',

'classoptions' : ',english,openany,oneside'
}

# Copy images
import os,shutil,fnmatch
def setup(app):
    try:
        os.makedirs(app.outdir)
    except:
        pass
    for root, dirs, files in os.walk(os.path.join(app.srcdir,'images')):
        for f in fnmatch.filter(files,"*.pdf"):
            shutil.copy(os.path.join(root,f),app.outdir)

# Temporary patch of sphinxcontrib.openapi (waiting for merge of PR)
import sys,os
sys.path.append(os.path.split(__file__)[0])
import _openapi30
from sphinxcontrib.openapi import openapi30

openapi30._parse_schema =     _openapi30._parse_schema
openapi30._example =          _openapi30._example
openapi30._httpresource =     _openapi30._httpresource
openapi30.openapihttpdomain = _openapi30.openapihttpdomain
