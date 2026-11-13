
# (c) Secure Identity Alliance

import datetime

source_suffix = {'.rst': 'restructuredtext'}
master_doc = 'index'
exclude_patterns = []
pygments_style = 'colorful'
project = 'OSIA'
release = '7.3-DRAFT'
html_title = f"{project} {release}"
author = 'SIA'

numfig = True

extensions = ['sphinxcontrib.httpdomain','sphinxcontrib.plantuml','sphinxcontrib.openapi', 'sphinx_copybutton']
# PlantUML command. By default the `plantuml` command must be on PATH (this is
# the case on Read the Docs, where it is installed via apt). For a local build
# with a jar, set the PLANTUML environment variable instead, e.g. (PowerShell):
#   $env:PLANTUML = "java -jar C:/path/to/plantuml.jar"
import os as _os
plantuml = _os.environ.get("PLANTUML", "plantuml")
plantuml_output_format = 'svg'
templates_path = ['_templates']
html_js_files = [
    "osia-sidebar.js",
]

exclude_patterns = ['_*.rst', '*/_*.rst']

rst_prolog = '''

.. meta::
  :http-equiv=X-UA-Compatible: IE=9    

.. |tick|   unicode:: U+2714 .. HEAVY CHECK MARK
.. |project| replace:: OSIA
.. |release| replace:: '''+release+'''

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
        
        tr th.head {background-color: #AD5389; color: white}

        li p {
            margin-top: 3px;
        }

        dl.py.function {
            margin-top: 20px;
        }

        dl dd p {
            margin: 0px;
        }

        figcaption p {
            text-align: center !important;
        }

    </style>

'''

#
# HTML Output Configuration
#
html_static_path = ['_static', 'images']
html_css_files = [
    #'custom.css',
    'osia-furo.css',
]
html_theme = "furo"
html_theme_options = {
    "sidebar_hide_name": False,
}
html_logo = "images/logo.svg"
html_show_sourcelink = False
copyright = 'Secure Identity Alliance, '+str(datetime.date.today().year)
html_context = {'project':'OSIA', 'version':release, 'copyright':copyright}
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

\\attachfilesetup{author=Secure Identity Alliance,color=0 0.5 0.5}

\\DeclareUnicodeCharacter{2714}{\\Checkmark}
\\newcommand{\\DUroletodo}[1]{\\colorbox{yellow}{#1} }
\\usepackage{color}
\\usepackage{colortbl}
\\definecolor{tableheader}{rgb}{0.678,0.325,0.537}

\\usepackage{makeidx}
\\usepackage[columns=1]{idxlayout}

\\usepackage{draftwatermark}
\\SetWatermarkScale{0.5}

''' + r'''

\renewcommand*{\sphinxstyletheadfamily}{\cellcolor{tableheader}\sffamily\color{white}}

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
        {\rm\Huge\sffamily\bfseries {\textcolor[rgb]{0.678,0.325,0.537}{Specifications version '''+release+r'''} } \par}
        \vfill
        %% Project logo
        \includegraphics[ width=12cm]{logo2.pdf} \par
        \vfill
        \small {\textcolor[rgb]{0.678,0.325,0.537}{\textcopyright Secure Identity Alliance, '''+str(datetime.date.today().year)+r''' } }
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

if 'DRAFT' in release:
    # The PDF keeps its DRAFT watermark. The HTML background watermark was
    # dropped with the move to the Furo-based template (it showed through the
    # page layout); the DRAFT status is carried by the release in the title.
    latex_elements['preamble'] += '\\SetWatermarkText{DRAFT}'
else:
    latex_elements['preamble'] += '\\SetWatermarkText{}'


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


if 'itu' in tags:
    rst_prolog += '''
.. |osia| replace:: ITU-T X.1281
.. |specification| replace:: recommendation
.. |chapter| replace:: clause
    '''
else:
    rst_prolog += '''
.. |osia| replace:: OSIA
.. |specification| replace:: specification
.. |chapter| replace:: chapter
    '''
