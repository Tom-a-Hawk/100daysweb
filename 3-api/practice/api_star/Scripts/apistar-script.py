#!c:\users\571226\documents\github\100daysweb\3-api\practice\api_star\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'apistar==0.5.41','console_scripts','apistar'
__requires__ = 'apistar==0.5.41'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('apistar==0.5.41', 'console_scripts', 'apistar')()
    )
