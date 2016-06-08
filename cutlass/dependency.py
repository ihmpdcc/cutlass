import inspect

from .Annotation import Annotation
from .Project import Project
from .Study import Study
from .Subject import Subject
from .Visit import Visit
from .Sample import Sample
from .WgsDnaPrep import WgsDnaPrep
from .SixteenSDnaPrep import SixteenSDnaPrep
from .SixteenSRawSeqSet import SixteenSRawSeqSet
from .MicrobiomeAssayPrep import MicrobiomeAssayPrep
from .HostAssayPrep import HostAssayPrep

# currently used in Base.children()
# __name__ attribute used to ensure that if the class or method name
# changes, the maintainer is forced to update it here, too.
dependency_methods = {
                  Project.__name__  : Project.studies.__name__,
               Annotation.__name__  : Annotation.clustered_seq_sets.__name__,
                    Study.__name__  : Study.subjects.__name__,
                  Subject.__name__  : Subject.visits.__name__,
                    Visit.__name__  : Visit.samples.__name__,
                   Sample.__name__  : Sample.dnaPreps.__name__,
               WgsDnaPrep.__name__  : WgsDnaPrep.raw_seq_sets.__name__,
          SixteenSDnaPrep.__name__  : SixteenSDnaPrep.raw_seq_sets.__name__,
        SixteenSRawSeqSet.__name__  : SixteenSRawSeqSet.trimmed_seq_sets.__name__,
            HostAssayPrep.__name__  : HostAssayPrep.cytokines.__name__,
      MicrobiomeAssayPrep.__name__  : MicrobiomeAssayPrep.cytokines.__name__
}

def generator_flatten(gen):
    for item in gen:
        if inspect.isgenerator(item) or type(item) in (list, tuple):
            for value in generator_flatten(item):
                yield value
        else:
            yield item
