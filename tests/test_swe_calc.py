#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import swisseph as swe
import unittest

SEFLG_MOSEPH = 4


class TestSweCalc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        swe.set_ephe_path()

    def test_01(self):
        flags_requested = swe.FLG_SWIEPH | swe.FLG_SPEED

        xx, retflags, serr = swe.calc(2452275.5, swe.SUN, flags_requested)

        # ASSERTIONS FOR STRUCTURAL FIX (Bug Fix Verification)
        self.assertIsInstance(xx, tuple)
        self.assertIsInstance(retflags, int)
        self.assertIsInstance(serr, str)

        # The serr string MUST NOT be empty, and MUST contain the fallback warning
        self.assertNotEqual(
            serr, "", "The warning string was empty, but Moshier fallback should occur."
        )
        self.assertIn(
            "Moshier eph", serr, "The warning string did not indicate Moshier fallback."
        )

        self.assertEqual(retflags, 260, "Return flags must be 260 (SWIEPH + MOSEPH).")
        self.assertEqual(len(xx), 6)

        self.assertAlmostEqual(xx[0], 280.38297419443285)
        self.assertAlmostEqual(xx[1], 0.0001423784113229515)
        self.assertAlmostEqual(xx[2], 0.9832977400834059)
        self.assertAlmostEqual(xx[3], 1.0188763524817992)
        self.assertAlmostEqual(
            xx[4], 1.7077220257029015e-05
        )
        self.assertAlmostEqual(
            xx[5], -1.0217079910816932e-05
        )

    def test_exception(self):
        with self.assertRaises(swe.Error):
            swe.calc(2452275.5, -2)


if __name__ == "__main__":
    unittest.main()

# vi: sw=4 ts=4 et
