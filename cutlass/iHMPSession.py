#!/usr/bin/env python

from osdf import OSDF
import logging
import importlib
from Util import *

class iHMPSession(object):
    check_python_version(name="Cutlass")
    """
    The iHMP Session class. This class allows you to connect with an OSDF
    instance and begin analysis of iHMP data. It produces skeletons of all
    objects in the iHMP OSDF database. Each object contains its own save, load,
    delete feature.

    Attributes:
        _single (iHMPSession): The iHMP Session that is currently live. None
        otherwise.
    """

    _single = None

    def __init__(self, username, password, server="osdf.ihmpdcc.org", port=8123,
                 ssl=True):
        """
        The initialization of the iHMPSession for the user.

        Args:
            username (str): The username for OSDF access.
            password (str): The password for OSDF access.
            server (str): The server domain name containing the OSDF instance.
                          Defaults to 'osdf.ihmpdcc.org'.
            port (int): The port allowing access to the OSDF instance.
            ssl (bool): Whether the OSDF server is behind SSL/TLS or not.
                        Defaults to true.
        """
        self._username = username
        self._password = password
        self._server = server
        self._port = port
        self._ssl = ssl
        self._osdf = OSDF(self._server, self._username, self._password,
                          port=self._port, ssl=self._ssl)

        self.logger = logging.getLogger(self.__module__ + '.' + \
                                        self.__class__.__name__)

        if iHMPSession._single is None:
            iHMPSession._single = self

        self.logger.info("Using SSL encryption? %s" % str(self._ssl))

    def _get_cutlass_instance(self, name):
        self.logger.debug("In _get_cutlass_instance.")

        classes = {
          "16s_dna_prep"                       : "SixteenSDnaPrep",
          "16s_raw_seq_set"                    : "SixteenSRawSeqSet",
          "16s_trimmed_seq_set"                : "SixteenSTrimmedSeqSet",
          "abundance_matrix"                   : "AbundanceMatrix",
          "annotation"                         : "Annotation",
          "clustered_seq_set"                  : "ClusteredSeqSet",
          "cytokine"                           : "Cytokine",
          "host_assay_prep"                    : "HostAssayPrep",
          "host_seq_prep"                      : "HostSeqPrep",
          "host_transcriptomics_raw_seq_set"   : "HostTranscriptomicsRawSeqSet",
          "host_wgs_raw_seq_set"               : "HostWgsRawSeqSet",
          "lipidome"                           : "Lipidome",
          "metabolome"                         : "Metabolome",
          "microbiome_assay_prep"              : "MicrobiomeAssayPrep",
          "microb_transcriptomics_raw_seq_set" : "MicrobTranscriptomicsRawSeqSet",
          "project"                            : "Project",
          "proteome"                           : "Proteome",
          "sample"                             : "Sample",
          "sample_attr"                        : "SampleAttribute",
          "study"                              : "Study",
          "subject"                            : "Subject",
          "viral_seq_set"                      : "ViralSeqSet",
          "visit"                              : "Visit",
          "visit_attr"                         : "VisitAttribute",
          "wgs_assembled_seq_set"              : "WgsAssembledSeqSet",
          "wgs_raw_seq_set"                    : "WgsRawSeqSet",
          "wgs_raw_seq_set_private"            : "WgsRawSeqSetPrivate",
          "wgs_dna_prep"                       : "WgsDnaPrep" }

        className = None
        valid = False

        if name in classes:
            valid = True
            className = classes[name]

        instance = None

        if valid:
            module = importlib.import_module("cutlass", package="cutlass")

            classVar = getattr(module, className)
            instance = classVar()
        else:
            raise TypeError("%s not defined in %s" % (name, self.__class__))

        return instance

    def __getattr__(self, name):
        if name.startswith("create_"):
            classLc = name[7:]

        try:
            instance = self._get_cutlass_instance(classLc)
        except TypeError:
            raise AttributeError("%s not defined in %s" % (name, self.__class__))

        return instance

    @staticmethod
    def get_session():
        """
        Returns the current iHMP session if any is instantiated.

        Args:
            None

        Returns:
            The current iHMP session.
        """
        if iHMPSession._single is None:
            raise Exception("A session has not yet been created.")

        return iHMPSession._single

    def get_osdf(self):
        """
        Returns the OSDF object with access to the OSDF instance.

        Args:
            None

        Returns:
            An OSDF object.
        """
        self.logger.debug("In get_osdf.")
        return self._osdf

    def create_object(self, node_type):
        """
        Returns an empty object of the node_type provided. It must be a
        valid object, or else an exception is raised.

        Args:
            node_type (str): The type of object desired.

        Returns:
            A object of the specified type.
        """
        self.logger.debug("In create_object. Type: %s" % node_type)

        instance = None

        try:
            instance = self._get_cutlass_instance(node_type)
        except TypeError:
            raise ValueError("Invalid node type specified: %s" % node_type)

        return instance

    @property
    def password(self):
        """
        str: The password provided by the user for the OSDF instance.
        """
        self.logger.debug("In 'password' getter.")
        return self._password

    @password.setter
    @enforce_string
    def password(self, password):
        """
        The password setter

        Args:
            password (str): The new password for OSDF access.

        Returns:
            None
        """
        self.logger.debug("In password setter.")
        self._password = password

        # Ensure the OSDF object gets the new connection parameter
        self.logger.debug("Setting the password in the OSDF client.")
        self._osdf.password = password

    @property
    def port(self):
        """
        int: The port for access to the OSDF instance on the server.
        """
        self.logger.debug("In 'port' getter.")
        return self._port

    @port.setter
    @enforce_int
    def port(self, port):
        """
        The port setter

        Args:
            port (int): The new port for OSDF access.

        Returns:
            None
        """
        self.logger.debug("In 'port' setter.")
        self._port = port

        # Ensure the OSDF object gets the new connection parameter
        self.logger.debug("Setting the port in the OSDF client.")
        self._osdf.port = port

    @property
    def server(self):
        """
        str: The server domain name that contains the live OSDF instance.
        """
        self.logger.debug("In 'server' getter.")
        return self._server

    @server.setter
    @enforce_string
    def server(self, server):
        """
        The server setter

        Args:
            server (str): The new server for OSDF access.

        Returns:
            None
        """
        self.logger.debug("In 'server' setter.")
        self._server = server

        # Ensure the OSDF object gets the new connection parameter
        self.logger.debug("Setting the server in the OSDF client.")
        self._osdf.server = server

    @property
    def ssl(self):
        """
        str: Retrieve whether the session is using SSL or not.
        """
        self.logger.debug("In 'ssl' getter.")
        return self._ssl

    @ssl.setter
    @enforce_bool
    def ssl(self, ssl):
        """
        The ssl setter

        Args:
            ssl (bool): Whether to use encryption (SSL) or not.

        Returns:
            None
        """
        self.logger.debug("In 'ssl' setter.")
        self._ssl = ssl

        # Ensure the OSDF object gets the new connection parameter
        self.logger.debug("Setting the SSL flag in the OSDF client.")
        self._osdf.ssl = ssl

    @property
    def username(self):
        """
        str: The username for access to the OSDF server.
        """
        self.logger.debug("In 'username' getter.")
        return self._username

    @username.setter
    @enforce_string
    def username(self, username):
        """
        The username setter

        Args:
            username (str): The new username for OSDF access.

        Returns:
            None
        """
        self.logger.debug("In 'username' setter.")
        self._username = username

        # Ensure the OSDF object gets the new connection parameter
        self.logger.debug("Setting the username in the OSDF client.")
        self._osdf.username = username
