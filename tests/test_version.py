#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of movie-down.
# https://github.com/Akhail/movie-down

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2017, Michel Betancourt <MichelBetancourt23@gmail.com>

from preggy import expect

from movie_down import __version__
from tests.base import TestCase


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        expect(__version__).to_equal('0.2.0')
