# -*- coding: utf-8 -*-
"""
Programming Languages Benchmark Script.
Copyright (C) 2014-2016 Stefan Smihla

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import os
import platform
import subprocess
import re


def get_processor_name():
    """ Returns processor info. """

    if platform.system() == 'Windows':
        return platform.processor()

    elif platform.system() == 'Darwin':
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
        command = 'sysctl -n machdep.cpu.brand_string'
        return subprocess.check_output(command).strip()

    elif platform.system() == 'Linux':
        command = 'cat /proc/cpuinfo'
        all_info = subprocess.check_output(command, shell=True).strip()
        for line in all_info.decode('UTF-8').split('\n'):
            if 'model name' in line:
                return re.sub('.*model name.*:', '', line, 1).strip()

    return ''
