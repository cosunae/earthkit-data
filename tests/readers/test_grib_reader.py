#!/usr/bin/env python3

# (C) Copyright 2020 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import datetime

from emohawk import load_from
from emohawk.testing import emohawk_file


def test_grib_len():
    f = load_from("file", "tests/data/test_single.grib")
    assert len(f) == 1

    f = load_from("file", "docs/examples/tuv_pl.grib")
    assert len(f) == 18


def test_grib_create_from_list_of_paths():
    f = load_from("file", ["docs/examples/tuv_pl.grib", "tests/data/ml_data.grib"])

    assert len(f) == 54
    assert f[0].metadata("level") == 1000
    assert f[18].metadata("level") == 1
    assert f[40].metadata("level") == 85


def test_dummy_grib():
    s = load_from(
        "dummy-source",
        kind="grib",
        paramId=[129, 130],
        date=[19900101, 19900102],
        level=[1000, 500],
    )
    assert len(s) == 8


def test_datetime():

    s = load_from("file", emohawk_file("docs/examples/test.grib"))

    assert s.to_datetime() == datetime.datetime(2020, 5, 13, 12), s.to_datetime()

    assert s.to_datetime_list() == [
        datetime.datetime(2020, 5, 13, 12)
    ], s.to_datetime_list()

    s = load_from(
        "dummy-source",
        kind="grib",
        paramId=[129, 130],
        date=[19900101, 19900102],
        level=[1000, 500],
    )
    assert s.to_datetime_list() == [
        datetime.datetime(1990, 1, 1, 12, 0),
        datetime.datetime(1990, 1, 2, 12, 0),
    ], s.to_datetime_list()


def test_bbox():
    s = load_from("file", emohawk_file("docs/examples/test.grib"))
    assert s.to_bounding_box().as_tuple() == (73, -27, 33, 45), s.to_bounding_box()


if __name__ == "__main__":
    from emohawk.testing import main

    main()