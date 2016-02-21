#!/usr/bin/env python

from osdf import OSDF
import logging

class iHMPSession(object):
    """
    The iHMP Session class. This class allows you to connect with an OSDF instance and
    begin analysis of iHMP data. It produces skeletons of all objects in the iHMP OSDF
    database. Each object contains its own save, load, delete feature

    Attributes:
        _single (iHMPSession): The iHMP Session that is currently live. None otherwise.
    """

    _single = None

    def __init__(self, username, password, server="osdf.ihmpdcc.org", port=8123):
        """
        The initialization of the iHMPSession for the user.

        Args:
            username (str): The username for OSDF access
            password (str): The password for OSDF access
            server (str): The server domain name containing the OSDF instance. Defaults
                to 'osdf.ihmpdcc.org'.
            port (int): The port allowing access to the OSDF instance.
        """
        self._username = username
        self._password = password
        self._server = server
        self._port = port
        self._osdf = OSDF(self._server, self._username,
                          self._password, self._port)

        self.logger = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)

        if iHMPSession._single is None:
            iHMPSession._single = self

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

    def create_project(self):
        """
        Returns an empty Project object.

        Args:
            None

        Returns:
            A Project object.
        """
        self.logger.debug("In create_project.")
        from Project import Project
        project = Project()
        return project

    def create_proteome(self):
        """
        Returns an empty Proteome object.

        Args:
            None

        Returns:
            A Proteome object.
        """
        self.logger.debug("In create_proteome.")
        from Proteome import Proteome
        proteome = Proteome()
        return proteome

    def create_sample(self):
        """
        Returns an empty Sample object.

        Args:
            None

        Returns:
            A Sample object.
        """
        self.logger.debug("In create_sample.")
        from Sample import Sample
        sample = Sample()
        return sample

    def create_subject(self):
        """
        Returns an empty Subject object.

        Args:
            None

        Returns:
            A Subject object.
        """
        self.logger.debug("In create_subject.")
        from Subject import Subject
        subject = Subject()
        return subject

    def create_study(self):
        """
        Returns an empty Study object.

        Args:
            None

        Returns:
            A Study object.
        """
        self.logger.debug("In create_study.")
        from Study import Study
        study = Study()
        return study

    def create_visit(self):
        """
        Returns an empty Visit object.

        Args:
            None

        Returns:
            A Visit object.
        """
        self.logger.debug("In create_visit.")
        from Visit import Visit
        visit = Visit()
        return visit

    def create_microbiome_assay_prep(self):
        """
        Returns an empty microbiome assay prep object.

        Args:
            None

        Returns:
            A MicrobiomeAssayPrep object.
        """
        self.logger.debug("In create_microbiome_assay_prep.")
        from MicrobiomeAssayPrep import MicrobiomeAssayPrep
        prep = MicrobiomeAssayPrep()
        return prep

    def create_host_assay_prep(self):
        """
        Returns an empty host assay prep object.

        Args:
            None

        Returns:
            A HostAssayPrep object.
        """
        self.logger.debug("In create_host_assay_prep.")
        from HostAssayPrep import HostAssayPrep
        prep = HostAssayPrep()
        return prep


    def create_16s_dna_prep(self):
        """
        Returns an empty 16S DNA Prep object.

        Args:
            None

        Returns:
            A 16S DNA Prep object.
        """
        self.logger.debug("In create_16s_dna_prep.")
        from SixteenSDnaPrep import SixteenSDnaPrep
        prep = SixteenSDnaPrep()
        return prep

    def create_16s_raw_seq_set(self):
        """
        Returns an empty 16S Raw Sequence Set object.

        Args:
            None

        Returns:
            A 16S Raw Sequence Set object.
        """
        self.logger.debug("In create_16s_raw_seq_set.")
        from SixteenSRawSeqSet import SixteenSRawSeqSet
        seq_set = SixteenSRawSeqSet()
        return seq_set

    def create_16s_trimmed_seq_set(self):
        """
        Returns an empty 16S Trimmed Sequence Set object.

        Args:
            None

        Returns:
            A 16S Trimmed Sequence Set object.
        """
        self.logger.debug("In create_16s_trimmed_seq_set.")
        from SixteenSTrimmedSeqSet import SixteenSTrimmedSeqSet
        seq_set = SixteenSTrimmedSeqSet()
        return seq_set

    def create_wgs_raw_seq_set(self):
        """
        Returns an empty WGS Raw Seq Set object.

        Args:
            None

        Returns:
            A WGS Raw Sequence Set object.
        """
        self.logger.debug("In create_wgs_raw_seq_set.")
        from WgsRawSeqSet import WgsRawSeqSet
        wgs_raw_seq_set = WgsRawSeqSet()
        return wgs_raw_seq_set

    def create_wgs_dna_prep(self):
        """
        Returns an empty WGS DNA Prep object.

        Args:
            None

        Returns:
            A WGS Dna Prep object.
        """
        self.logger.debug("In create_16s_trimmed_seq_set.")
        from WgsDnaPrep import WgsDnaPrep
        wgs_dna_prep = WgsDnaPrep()
        return wgs_dna_prep

    def create_object(self, node_type):
        """
        Returns an empty object of the node_type provided. It must be a valid object,
        or else an exception is raised.

        Args:
            node_type (str): The type of object desired.

        Returns:
            A object of the specified type.
        """
        self.logger.debug("In create_object. Type: %s" % node_type)

        node = None
        if node_type == "project":
            from Project import Project
            self.logger.debug("Creating a Project.")
            node = Project()
        elif node_type == "proteome":
            from Proteome import Proteome
            self.logger.debug("Creating a Proteome.")
            node = Proteome()
        elif node_type == "visit":
            from Visit import Visit
            self.logger.debug("Creating a Visit.")
            node = Visit()
        elif node_type == "subject":
            from Subject import Subject
            self.logger.debug("Creating a Subject.")
            node = Subject()
        elif node_type == "sample":
            from Sample import Sample
            self.logger.debug("Creating a Sample.")
            node = Sample()
        elif node_type == "study":
            from Study import Study
            self.logger.debug("Creating a Study.")
            node = Study()
        elif node_type == "wgs_dna_prep":
            from WgsDnaPrep import WgsDnaPrep
            self.logger.debug("Creating a WgsDnaPrep.")
            node = WgsDnaPrep()
        elif node_type == "16s_dna_prep":
            from SixteenSDnaPrep import SixteenSDnaPrep
            self.logger.debug("Creating a SixteenSDnaPrep.")
            node = SixteenSDnaPrep()
        elif node_type == "16s_raw_seq_set":
            from SixteenSRawSeqSet import SixteenSRawSeqSet
            self.logger.debug("Creating a SixteenSRawSeqSet.")
            node = SixteenSRawSeqSet()
        elif node_type == "wgs_raw_seq_set":
            from WgsRawSeqSet import WgsRawSeqSet
            self.logger.debug("Creating a WgsRawSeqSet.")
            node = WgsRawSeqSet()
        elif node_type == "16s_trimmed_seq_set":
            from SixteenSTrimmedSeqSet import SixteenSTrimmedSeqSet
            self.logger.debug("Creating a SixteenSTrimmedSeqSet.")
            node = SixteenSTrimmedSeqSet()
        elif node_type == "microb_assay_prep":
            from MicrobiomeAssayPrep import MicrobiomeAssayPrep
            self.logger.debug("Creating a MicrobiomeAssayPrep.")
            node = MicrobiomeAssayPrep()
        elif node_type == "host_assay_prep":
            from HostAssayPrep import HostAssayPrep
            self.logger.debug("Creating a HostAssayPrep.")
            node = HostAssayPrep()
        else:
            raise ValueError("Invalid node type specified: %" % node_type)

        return node

    @property
    def password(self):
        """ str: The password provided by the user for the OSDF instance. """
        self.logger.debug("In password getter.")
        return self._password

    @password.setter
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
        """ int: The port for access to the OSDF instance on the server. """
        self.logger.debug("In port getter.")
        return self._port

    @port.setter
    def port(self, port):
        """
        The port setter

        Args:
            port (int): The new port for OSDF access.

        Returns:
            None
        """
        self.logger.debug("In port setter.")
        self._port = port
        # Ensure the OSDF object gets the new connection parameter
        self.logger.debug("Setting the port in the OSDF client.")
        self._osdf.port = port

    @property
    def server(self):
        """ str: The server domain name that contains the live OSDF instance. """
        self.logger.debug("In server getter.")
        return self._server

    @server.setter
    def server(self, server):
        """
        The server setter

        Args:
            server (str): The new server for OSDF access.

        Returns:
            None
        """
        self.logger.debug("In server setter.")
        self._server = server
        # Ensure the OSDF object gets the new connection parameter
        self.logger.debug("Setting the server in the OSDF client.")
        self._osdf.server = server

    @property
    def username(self):
        """ str: The username for acces to the OSDF server. """
        self.logger.debug("In username getter.")
        return self._username

    @username.setter
    def username(self, username):
        """
        The username setter

        Args:
            username (str): The new username for OSDF access.

        Returns:
            None
        """
        self.logger.debug("In username setter.")
        self._username = username
        # Ensure the OSDF object gets the new connection parameter
        self.logger.debug("Setting the username in the OSDF client.")
        self._osdf.username = username
