import sys
import os
import unittest
from unittest import TestCase
from pathlib import Path
sys.path.append("../")
from pyspw.pyServletPrintWriter import create_parser, spracuj


class Tests(TestCase):
    def setUp(self):
        parser = create_parser()
        self.parser = parser

    def test_prazdny_vstup(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args([])

    def test_vypis_do_konzoly_zly_vstup(self):
        args = self.parser.parse_args(["test2.html"])
        vysledok = spracuj(args.subor[0])
        self.assertFalse(vysledok)

    def test_vypis_do_konzoly_dobry_vstup(self):
        args = self.parser.parse_args(["test.html"])
        vysledok = spracuj(args.subor[0])
        self.assertTrue(vysledok)

    def test_zapis_do_suboru_bez_w_argumentu(self):
        with self.assertRaises(SystemExit):
            args = self.parser.parse_args(["test.html", "-w"])

    def test_zapis_do_suboru_s_argumentom(self):
        args = self.parser.parse_args(["test.html", "-w", "test2.html"])
        vysledok = spracuj(args.subor[0], args.zapis)
        self.assertTrue(vysledok)

    def test_zapis_do_rovnakeho_suboru(self):
        #vytvorí ďalší súbor na testovanie
        spracuj("test.html", "test2.html")

        args = self.parser.parse_args(["test2.html", "-w", "test2.html"])
        vysledok = spracuj(args.subor[0], args.zapis)
        self.assertTrue(vysledok)

    def tearDown(self):
        subor = Path("test2.html")
        if subor.exists():
            os.remove("test2.html")

if __name__ == "__main__":
    unittest.main(buffer=False)
