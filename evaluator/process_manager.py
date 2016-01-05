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
import shutil
import shlex
import subprocess
import signal
import platform
from threading import Thread


class ProcessManager(object):
    """ Process Manager to safely handle processes. """

    _stdout = ''
    _process = None

    @classmethod
    def safe_path(cls, path):
        """ Convert path to safe path. """
        path = shutil.which(os.path.normpath(path))
        return shlex.quote(path) if path else None

    @classmethod
    def set_output(cls, stdout):
        """ Sets output value. """
        cls._stdout = stdout

    @classmethod
    def get_stdout(cls):
        """ Returns output value. """
        return cls._stdout

    @classmethod
    def set_process(cls, process):
        """ Sets process. """
        cls._process = process

    @classmethod
    def get_process(cls):
        """ Returns process value. """
        return cls._process

    @classmethod
    def build_proc_params(cls):
        """ Build args depended on OS. """

        params = {'universal_newlines': True,
                  'stderr': subprocess.STDOUT,
                  'stdout': subprocess.PIPE,
                  'shell': True}

        if platform.system() != 'Windows':
            params['preexec_fn'] = os.setsid

        return params

    @classmethod
    def _run_process(cls, command):
        """ Run process and saves it output. """
        cls.set_process(subprocess.Popen(command, **cls.build_proc_params()))
        cls.set_output(cls.get_process().communicate()[0].strip())
        return cls.get_stdout()

    @classmethod
    def force_kill_process(cls, process):
        """ Kills process and its childs. """
        if platform.system() == 'Windows':
            subprocess.Popen('TASKKILL /F /PID %s /T' % process.pid,\
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            os.killpg(process.pid, signal.SIGTERM)

    @classmethod
    def run_process(cls, command, timeout=None):
        """ Kills process after timeout. """
        cls.set_output(None)
        if not timeout:
            return cls._run_process(command)

        evaluation = Thread(target=cls._run_process, args=(command, ))
        evaluation.start()
        evaluation.join(timeout)

        if evaluation.isAlive():
            cls.force_kill_process(cls.get_process())
            cls.set_process(None)
            return None
        else:
            return cls.get_stdout()
