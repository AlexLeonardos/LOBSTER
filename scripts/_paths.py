"""Put this directory on sys.path and resolve input FASTAs from the command line.

Every script in this directory imports `run_lobster` from beside itself, so
this module inserts its own directory onto sys.path when imported.  Input
alignments are always passed explicitly on the command line -- there are no
baked-in default paths, so the scripts run unchanged wherever the repository is
checked out.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)          # so `import run_lobster` works


def inputs_from_argv(argv):
    """Return [(label, path), ...] from explicit command-line paths.

    A core-alignment FASTA must be given; there are no default locations.
    """
    if len(argv) > 1:
        return [(os.path.basename(a), a) for a in argv[1:]]
    sys.exit("no input alignment given; pass one or more paths, e.g.\n"
             "  python %s path/to/cores.aln.fasta" % os.path.basename(argv[0]))
