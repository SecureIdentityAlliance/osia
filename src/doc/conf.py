
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = []
pygments_style = 'colorful'
project = 'OSIA'
release = '2.0'
author = 'SIA'
html_context = {'project':'OSIA', 'version':"2.0", 'copyright':'SIA'}

numfig = True

extensions = ['sphinx.ext.extlinks','sphinxcontrib.httpdomain','sphinxcontrib.plantuml']

extlinks = {'openapi': ('https://github.com/SecureIdentityAlliance/osia/tree/master/src/doc/yaml/%s',
                      '')}

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

# Copy images
import os,shutil,fnmatch
try:
    os.makedirs('../../target/pdf')
except:
    pass
for root, dirs, files in os.walk('images'):
    for f in fnmatch.filter(files,"*.pdf"):
        shutil.copy(os.path.join(root,f),"../../target/pdf")

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
        {\rm\Huge\sffamily\bfseries {\textcolor[rgb]{0.678,0.325,0.537}{Specifications version 2.0} } \par}
        \vfill
        %% Project logo
        \includegraphics[ width=12cm]{logo2.pdf} \par
        \vfill
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
