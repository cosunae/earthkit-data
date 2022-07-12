# (C) Copyright 2022 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.


from teal import Data


class NumpyArrayWrapper(Data):
    pass


def wrapper(data, *args, **kwargs):
    import numpy as np

    if isinstance(data, np.ndarray):
        return NumpyArrayWrapper(data, *args, **kwargs)
    return None
