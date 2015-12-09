from .iHMPSession import iHMPSession
from .Project import Project
from .Study import Study
from .Visit import Visit
from .Sample import Sample
from .Subject import Subject
from .SixteenSDnaPrep import SixteenSDnaPrep
from .WgsDnaPrep import WgsDnaPrep
from .SixteenSRawSeqSet import SixteenSRawSeqSet
from .WgsRawSeqSet import WgsRawSeqSet
from .SixteenSTrimmedSeqSet import SixteenSTrimmedSeqSet
from .aspera import aspera
from .mixs import MIXS, MixsException
from .mims import MIMS, MimsException
from .mimarks import MIMARKS, MimarksException

_node_type_idx = {
                  Project.osdf_node_type : Project.load_project,
                    Study.osdf_node_type : Study.load_study,
                    Visit.osdf_node_type : Visit.load_visit,
                   Sample.osdf_node_type : Sample.load_sample,
                  Subject.osdf_node_type : Subject.load_subject,
          SixteenSDnaPrep.osdf_node_type : SixteenSDnaPrep.load_sixteenSDnaPrep,
               WgsDnaPrep.osdf_node_type : WgsDnaPrep.load_wgsDnaPrep,
        SixteenSRawSeqSet.osdf_node_type : SixteenSRawSeqSet.load_sixteenSRawSeqSet,
             WgsRawSeqSet.osdf_node_type : WgsRawSeqSet.load_wgsRawSeqSet,
    SixteenSTrimmedSeqSet.osdf_node_type : SixteenSTrimmedSeqSet.load_sixteenSTrimmedSeqSet,
}

def load(node_id):
    doc = iHMPSession.get_session().get_osdf().get_node(node_id)
    load_func = _node_type_idx.get(doc['node_type'], None)
    if load_func is None:
        raise ValueError("Unknown node type: "+nodetype)
    return load_func(doc)
