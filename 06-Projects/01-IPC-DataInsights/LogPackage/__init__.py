#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Edward J. C. Ashenbert'
__credits__ = ["Edward J. C. Ashenbert"]
__maintainer__ = "Edward J. C. Ashenbert"
__email__ = "nguyenquangbinh803@gmail.com"
__copyright__ = "Copyright 2021"
__status__ = "Working on deploy Analyzer Design pattern"
__version__ = "2021.06.14"


LogPackageInstanceTemplate = "#!/usr/bin/env python\n\
# -*- coding: utf-8 -*-\n\
\n\
__author__ = 'Edward J. C. Ashenbert'\n\
__credits__ = [\"Edward J. C. Ashenbert\"]\n\
__maintainer__ = \"Edward J. C. Ashenbert\"\n\
__email__ = \"nguyenquangbinh803@gmail.com\"\n\
__copyright__ =\"Copyright 2021\"\n\
__status__ = \"Working on deploy Analyzer Design pattern\"\n\
__version__ = \"2021.06.14\"\n\
\n\
from LogPackage.LogPackage import LogPackageAbstract\n\
\n\
\n\
class LogPackage_%s (LogPackageAbstract):\n\
    def __init__(self):\n\
        super().__init__()\n\
        self.log_level = \"\"\n\
        self.log_package_name = \"\"\n\
        self.log_package_data = \"\"\n\
\n\
    def LogPackageAnalyze(self):\n\
        pass"

from LogPackage.LogPackage_imgLib_expStandbyComplete import *
from LogPackage.LogPackage_imgLib_startTrace import *
from LogPackage.LogPackage_imgLib_traceComplete import *
from LogPackage.LogPackage_imgLib_imgOutMemClear import *
from LogPackage.LogPackage_TrexACL_clearImageBuffer import *
from LogPackage.LogPackage_imgLib_initLibrary import *
from LogPackage.LogPackage_imgLib_getConfig import *
from LogPackage.LogPackage_imgLib_makeDMDMirrorAdr import *
from LogPackage.LogPackage_imgLib_expStandby import *
from LogPackage.LogPackage_imgLib_expStart import *
from LogPackage.LogPackage_imgLib_expPostProc import *
