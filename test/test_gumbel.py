# -*- coding: utf-8 -*-
"""
Module for testing gumbel class
"""

import unittest

from qats.gumbel import Gumbel, pwm, mle, msm, lse


# todo: more test cases for weibull class and functions


class GumbelTestCases(unittest.TestCase):
    def setUp(self):
        self.loc = 1000.
        self.scale = 150.

        gd = Gumbel(loc=self.loc, scale=self.scale)
        self.x = gd.rnd(size=50, seed=13)

    def test_pwm(self):
        a, b = pwm(self.x)
        self.assertLessEqual((self.loc-a)/self.loc, 0.1)
        self.assertLessEqual((self.scale - b) / self.scale, 0.1)

    def test_msm(self):
        a, b = msm(self.x)
        self.assertLessEqual((self.loc-a)/self.loc, 0.1)
        self.assertLessEqual((self.scale - b) / self.scale, 0.1)

    def test_lse(self):
        a, b = lse(self.x)
        self.assertLessEqual((self.loc-a)/self.loc, 0.1)
        self.assertLessEqual((self.scale - b) / self.scale, 0.1)

    def test_mle(self):
        a, b = mle(self.x)
        self.assertLessEqual((self.loc-a)/self.loc, 0.1)
        self.assertLessEqual((self.scale - b) / self.scale, 0.1)

    def test_fit(self):
        gumb = Gumbel.fit(self.x, method="msm")
        a, b = msm(self.x)
        self.assertEqual(gumb.loc, a)
        self.assertEqual(gumb.scale, b)


if __name__ == '__main__':
    unittest.main()