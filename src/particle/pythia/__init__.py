# Copyright (c) 2018-2022, Eduardo Rodrigues and Henry Schreiner.
#
# Distributed under the 3-clause BSD license, see accompanying file LICENSE
# or https://github.com/scikit-hep/particle for details.


from typing import Tuple

from .pythiaid import PythiaID

__all__ = ("PythiaID",)


def __dir__() -> Tuple[str, ...]:
    return __all__
