"""
Utility module for retrieving a node's children.
"""

import inspect

# pylint: disable=C0302, W0703, C1801

from .Annotation import Annotation
from .Project import Project
from .Study import Study
from .Subject import Subject
from .Visit import Visit
from .Sample import Sample
from .WgsAssembledSeqSet import WgsAssembledSeqSet
from .WgsDnaPrep import WgsDnaPrep
from .WgsRawSeqSet import WgsRawSeqSet
from .SixteenSDnaPrep import SixteenSDnaPrep
from .SixteenSRawSeqSet import SixteenSRawSeqSet
from .SixteenSTrimmedSeqSet import SixteenSTrimmedSeqSet
from .MicrobiomeAssayPrep import MicrobiomeAssayPrep
from .HostAssayPrep import HostAssayPrep
from .HostSeqPrep import HostSeqPrep

# currently used in Base.children()
# __name__ attribute used to ensure that if the class or method name
# changes, the maintainer is forced to update it here, too.
# pylint: disable=C0330
dependency_methods = {
                  Project.__name__ : Project.studies.__name__,
               Annotation.__name__ : Annotation.clustered_seq_sets.__name__,
            HostAssayPrep.__name__ : HostAssayPrep.derivations.__name__,
              HostSeqPrep.__name__ : HostSeqPrep.derivations.__name__,
      MicrobiomeAssayPrep.__name__ : MicrobiomeAssayPrep.derivations.__name__,
                   Sample.__name__ : Sample.allChildren.__name__,
          SixteenSDnaPrep.__name__ : SixteenSDnaPrep.raw_seq_sets.__name__,
        SixteenSRawSeqSet.__name__ : SixteenSRawSeqSet.trimmed_seq_sets.__name__,
    SixteenSTrimmedSeqSet.__name__ : SixteenSTrimmedSeqSet.abundance_matrices.__name__,
                    Study.__name__ : Study.subjects.__name__,
                  Subject.__name__ : Subject.derivations.__name__,
                    Visit.__name__ : Visit.samples.__name__,
       WgsAssembledSeqSet.__name__ : WgsAssembledSeqSet.derivations.__name__,
               WgsDnaPrep.__name__ : WgsDnaPrep.child_seq_sets.__name__,
             WgsRawSeqSet.__name__ : WgsRawSeqSet.viral_seq_sets.__name__
}
# pylint: enable=C0330

def generator_flatten(gen):
    """ Flatten the result of the generator. """
    for item in gen:
        if inspect.isgenerator(item) or type(item) in (list, tuple):
            for value in generator_flatten(item):
                yield value
        else:
            yield item
