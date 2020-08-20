# -*- coding: utf-8 -*-

# Copyright 2018 Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Ensure the expected functioning of ``memote.experimental.medium``."""

from __future__ import absolute_import

from os.path import dirname, join

import pytest
from six import iteritems

from memote.experimental.medium import Medium


DATA_PATH = join(dirname(__file__), "data")


class TestMedium(object):
    @pytest.mark.parametrize("obj", [{}, {"label": "bird"}])
    def test_init(self, obj):
        exp = Medium(identifier="that", obj=obj, filename=join(DATA_PATH, "."))
        for key, value in iteritems(obj):
            assert getattr(exp, key) == value

    def test_load(self):
        pass

    def test_validate(self):
        pass

    def test_evaluate_report(self):
        pass
