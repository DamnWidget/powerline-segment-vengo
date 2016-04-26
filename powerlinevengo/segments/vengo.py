from __future__ import absolute_import

import os

from powerline.theme import requires_segment_info


@requires_segment_info
def vengoenv(pl, segment_info):
    """Return back the vengo environment prompt
    """

    vengo_env = segment_info['environ'].get('VENGO_ENV')
    if vengo_env is not None:
        return os.path.basename(vengo_env)
