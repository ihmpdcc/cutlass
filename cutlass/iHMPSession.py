#!/usr/bin/env python

from osdf import OSDF
import logging

class iHMPSession(object):
    _single = None

    def __init__(self, username, password, server="osdf.ihmpdcc.org", port=8123):
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
        if iHMPSession._single is None:
            raise Exception("A session has not yet been created.")

        return iHMPSession._single

    def get_osdf(self):
        self.logger.debug("In get_osdf.")
        return self._osdf

    def create_project(self):
        self.logger.debug("In create_project.")
        from Project import Project
        project = Project()
        return project

    def create_sample(self):
        self.logger.debug("In create_sample.")
        from Sample import Sample
        sample = Sample()
        return sample

    def create_subject(self):
        self.logger.debug("In create_subject.")
        from Subject import Subject
        subject = Subject()
        return subject

    def create_study(self):
        self.logger.debug("In create_study.")
        from Study import Study
        study = Study()
        return study

    def create_16s_dna_prep(self):
        self.logger.debug("In create_16s_dna_prep.")
        from SixteenSDnaPrep import SixteenSDnaPrep
        prep = SixteenSDnaPrep()
        return prep

    def create_16s_raw_seq_set(self):
        self.logger.debug("In create_16s_raw_seq_set.")
        from SixteenSRawSeqSet import SixteenSRawSeqSet
        seq_set = SixteenRawSeqSet()
        return seq_set

    def create_16s_trimmed_seq_set(self):
        self.logger.debug("In create_16s_trimmed_seq_set.")
        from SixteenSTrimmedSeqSet import SixteenSTrimmedSeqSet
        seq_set = SixteenTrimmedSeqSet()
        return seq_set

    def create_object(self, node_type):
        self.logger.debug("In create_object. Type: %s" % node_type)

        node = None
        if node_type == "project":
            from Project import Project
            self.logger.debug("Creating a Project.")
            node = Project()
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
        else:
            raise ValueError("Invalid node type specified: %" % node_type)

        return node

    @property
    def password(self):
        self.logger.debug("In password getter.")
        return self._password

    @password.setter
    def password(self, password):
        self.logger.debug("In password setter.")
        self._password = password
        # Ensure the OSDF object gets the new connection parameter
        self.logger.debug("Setting the password in the OSDF client.")
        self._osdf.password = password

    @property
    def port(self):
        self.logger.debug("In port getter.")
        return self._port

    @port.setter
    def port(self, port):
        self.logger.debug("In port setter.")
        self._port = port
        # Ensure the OSDF object gets the new connection parameter
        self.logger.debug("Setting the port in the OSDF client.")
        self._osdf.port = port

    @property
    def server(self):
        self.logger.debug("In server getter.")
        return self._server

    @server.setter
    def server(self, server):
        self.logger.debug("In server setter.")
        self._server = server
        # Ensure the OSDF object gets the new connection parameter
        self.logger.debug("Setting the server in the OSDF client.")
        self._osdf.server = server

    @property
    def username(self):
        self.logger.debug("In username getter.")
        return self._username

    @username.setter
    def username(self, username):
        self.logger.debug("In username setter.")
        self._username = username
        # Ensure the OSDF object gets the new connection parameter
        self.logger.debug("Setting the username in the OSDF client.")
        self._osdf.username = username
