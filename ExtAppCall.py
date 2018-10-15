##############################################################################
#  Copyright (c) 2018 by Paul Scherrer Institute, Switzerland
#  All rights reserved.
#  Authors: Oliver Bruendler
##############################################################################
import time
import sys
from subprocess import Popen, PIPE, TimeoutExpired
import os
from .TempWorkDir import TempWorkDir
import uuid

class ExtAppCall:

    def __init__(self, work_dir : str, command : str, ignore_stdout : bool = False, ignore_stderr : bool = False):
        """
        Constructor

        .. warning:: Note that ignore_stderr resp. ignore_stdout must be set if the programm executed does not output anything on the
                     given I/O channel. Otherwise the execution may block completely.

        :param work_dir: The application call is executed from this directory.
        :type work_dir: str
        :param command: This is the command to be executed.
        :type command: str
        :param ignore_stdout: Does not have any effect anymore, only here for backward compatibility.
        :param ignore_stderr: Does not have any effect anymore, only here for backward compatibility.

        :return: Created object
        :rtype: ExtAppCall
        """

        self.work_dir = work_dir
        """ Working directory of this Application call (Read-Only) """

        self.command = command
        """ Command of this Application Call (Read-Only) """

        self._stderr = ""
        self._stdout = ""
        self._errFile = None
        self._outFile = None
        self._outPath = None
        self._errPath = None
        self._proc = None

    def run_async(self):
        """
        Run application call asynchronously (i.e. do not wait until the application call completed).

        :return: Object the method was called on
        :rtype: ExtAppCall
        """
        with TempWorkDir(self.work_dir):
            self._stderr = ""
            self._stdout = ""

            #Create files for stdout/stderr since files are the only relieable way of communication for all OS
            self._outPath = os.path.abspath(".") + "/ExtAppCall-OUT-" + str(uuid.uuid4())
            self._errPath = os.path.abspath(".") + "/ExtAppCall-ERR-" + str(uuid.uuid4())
            self._errFile = open(self._errPath, "w+")
            self._outFile = open(self._outPath, "w+")

            #Shell must be used for linux but not for windoes
            shellParam = True
            if sys.platform.startswith("win"):
                shellParam = False
            self._proc = Popen(self.command, stdout=self._outFile, stderr=self._errFile, stdin=PIPE, shell=shellParam)

        return self

    def wait(self, timeout_sec : int = 0):
        """
        Wait until the application call completed. An exception is raised if the timeout elapses before
        the application call completes.

        :param timeout_sec: Timeout in milliseconds (optional). If no timeout is given, the timeout is set to infinity.
        :type timeout_sec: int

        :return: Object the method was called on
        :rtype: ExtAppCall
        """
        timed_out = False
        try:
            if timeout_sec > 0:
                self._proc.wait(timeout_sec)
            else:
                self._proc.wait()
        except TimeoutExpired:
            self._proc.terminate()
            timed_out = True

        #close the file since the subprocess has exited now
        self._errFile.close()
        self._outFile.close()

        #Read stdout and stderr
        with open(self._outPath, "r") as fo, open(self._errPath, "r") as fe:
            self._stdout = fo.read()
            self._stderr = fe.read()

        # remove temporary files. If it fails, wait for 5 seconds and retry (maybe the application blocking the file
        #  closed by then).
        # 28.07.2018 - known problem of the Popen library on Windows
        # When Popen is called it passes all handles of open files to the subprocess. It cannot be disabled
        # on Windows when stdout and stderr is redirected to files. Even the subprocess is closed the Windows OS
        # keeps somewhere handles to the temporary files even for several minutes.
        # The work around is to try 5 times to delete the temporary files. Otherwise they are left.
        for path in [self._outPath, self._errPath]:
            count = 0
            while count < 5:
              try:
                  os.remove(path)
                  break
              except:
                  time.sleep(15)  
                  count += 1

        #Raise exception if required
        if timed_out:
            raise TimeoutExpired("Error: Timeout expired", timeout_sec)
        return self

    def run_sync(self, timeout_sec : int = 0):
        """
        Run application call synchronously (i.e. the function blocks until the application call completed). An
        exception is raised if the timeout elapses before the application call completes.


        :param timeout_sec: Timeout in milliseconds (optional). If no timeout is given, the timeout is set to infinity.
        :type timeout_sec: int

        :return: Object the method was called on
        :rtype: ExtAppCall
        """
        self.run_async()
        self.wait(timeout_sec)
        time.sleep(0.1)
        return self

    def get_stdout(self):
        """
        Get stdout of the application call.

        :return: stdout content
        :rtype: str
        """
        return self._stdout

    def get_stderr(self):
        """
        Get stderr of the application call.

        :return: stdout content
        :rtype: str
        """
        return self._stderr

    def get_exit_code(self):
        """
        Get return code of application call

        :return: Return code
        :rtype: int
        """
        return self._proc.returncode

