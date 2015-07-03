#!/usr/bin/python

import os
import re
import subprocess
import logging

# Test wrapper code for ascp

# download example command(s):
#
# only getting ~ 10Mb/s (on 20-30Mb connection): with defaults:
#   ascp -T -v -L . testuser@aspera.ihmpdcc.org:test2.fsa ./
#   ascp -T -v -L . testuser@aspera.ihmpdcc.org:50MB ./
# closer to 20Mb/s with this option:
#   ascp -T -v -l 200M -L . testuser@aspera.ihmpdcc.org:50MB ./
#
# upload example command(s):
#   ascp -T -v -L . testuser@aspera.ihmpdcc.org:
#
logger = logging.getLogger(__name__)

ASCP_COMMAND = "ascp"
ASCP_MIN_VERSION = '3.5'

# compare version numbers
def version_cmp(v1, v2):
    logger.debug("In version_cmp.")
    def normalize(v):
        return [int(x) for x in re.sub(r'(\.0+)*$','', v).split(".")]
    return cmp(normalize(v1), normalize(v2))

# Return version number of ascp executable referenced by ascp_command.
# May raise an exception if the path is invalid.
def get_ascp_version(ascp_command):
    logger.debug("In get_ascp_version.")

    version = None
    retval = subprocess.check_output([ascp_command, "--version"],
                                     universal_newlines = True)
    cre = re.compile(r"^.*ascp version (\d[\d\.]+)", re.MULTILINE)
    for match in cre.finditer(retval):
        version = match.groups()[0]
    # raise an exception if the expected string couldn't be matched
    if version == None:
        raise Exception("Output from ascp command ('" + ascp_command +
                        " --version') did not contain a recognizable version number.")
    return version

def check_ascp_version(ascp_command):
    logger.debug("In check_ascp_version.")

    # check ascp version, raise error if too low
    ascp_ver = get_ascp_version(ascp_command)

    if ascp_ver == None:
        raise Exception("Unable to determine ascp version")
    if version_cmp(ascp_ver, ASCP_MIN_VERSION) < 0:
        raise Exception("Found ascp version " + ascp_ver + " but " +
                        ASCP_MIN_VERSION + " required")
    return True

def get_ascp_env(password):
    logger.debug("In get_ascp_env.")

    e = os.environ.copy()
    if password != None:
        logger.info("Setting ASPERA_SCP_PASS environment variable.")
        e['ASPERA_SCP_PASS'] = password

    return e

# run ascp command, returning True for success or False for failure
def run_ascp(ascp_cmd, password):
    logger.debug("In run_ascp.")

    try:
        p = subprocess.Popen(ascp_cmd, stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             universal_newlines = True,
                             env = get_ascp_env(password))
        (s_out, s_err) = p.communicate()

        if not re.match(r"Completed: \S+ bytes transferred in", s_out):
            if re.match(r"^.*failed to authenticate", s_err):
                logger.error("Aspera authentication failure.")
            else:
                if s_err != None:
                    logger.error("Unexpected STDERR from ascp: %s" % s_err)
                if s_out != None:
                    logger.error("Unexpected STDOUT from ascp: %s" % s_out)
            return False
    except subprocess.CalledProcessError as cpe:
        logger.error("Encountered an error when running ascp: ", cpe)
        return False

    return True

# download a single file via Aspera. return True if successful, False if not
def download_file(server, username, password, remote_path, local_path):
    logger.debug("In download_file.")

    check_ascp_version(ASCP_COMMAND)
    ascp_cmd = [ ASCP_COMMAND, "-T", "-v", "-l", "300M", username + "@" +
                 server + ":" + remote_path, local_path ]
    return run_ascp(ascp_cmd, password)

# upload a single file via Aspera. return True if successful, False if not
def upload_file(server, username, password, local_file, remote_path):
    logger.debug("In upload_file.")
    check_ascp_version(ASCP_COMMAND)

    # check that local file exists
    if not os.path.isfile(local_file):
        logger.warn("local file " + local_file + " does not exist")
        return False

    ascp_cmd = [ ASCP_COMMAND, "-T", "-v", "-l", "300M", local_file,
                 username + "@" + server + ":" + remote_path ]

    return run_ascp(ascp_cmd, password)
