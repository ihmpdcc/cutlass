import os
import ConfigParser
from cutlass import iHMPSession

class CutlassTestConfig(object):
    @staticmethod
    def get_session():
        config_paths = [".cutlass_test.ini", os.path.expanduser('~/.cutlass_test.ini')]

        parser = ConfigParser.ConfigParser()
        successfullyReadFiles = parser.read(config_paths);

        if len(successfullyReadFiles) == 0:
            raise Exception("Unable to find .cutlass_test.ini in cwd or in home directory")

        section = 'cutlass'
        host = parser.get(section, 'host')
        port = parser.get(section, 'port')
        username = parser.get(section, 'username')
        password = parser.get(section, 'password')
        ssl = parser.getboolean(section, 'ssl')

        #print("{} - {} - {} - {} - {}".format(host, port, username, password, ssl))

        if (host is None or port is None or username is None or password is None):
            raise Exception("Missing configuration parameters in .cutlass_test.ini.")

        session = iHMPSession(username, password, server=host, port=port, ssl=ssl)

        return session
