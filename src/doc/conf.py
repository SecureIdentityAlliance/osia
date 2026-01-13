
# (c) Secure Identity Alliance

import datetime

source_suffix = {'.rst': 'restructuredtext'}
master_doc = 'index'
exclude_patterns = []
pygments_style = 'colorful'
project = 'OSIA'
release = '7.1'
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
    latex_elements['preamble'] += '\\SetWatermarkText{DRAFT}'
    rst_prolog += '''
.. raw:: html

    <style>
        body {
            background-repeat: repeat-y;
            background-image:url("data:image/svg+xml;utf8, <svg xmlns='http://www.w3.org/2000/svg' version='1.1' height='50px' width='400px'> <text x='10' y='20' fill='black' font-size='30' opacity='0.1'>DRAFT    DRAFT    DRAFT</text> </svg>");
        }
    </style>
'''
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
