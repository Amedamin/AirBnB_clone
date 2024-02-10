#!/usr/bin/python3
"""Defines unittests for console.py"""

import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_create(unittest.TestCase):

    def test_crmissing_cla(self):
        MSG = "** class name missing **"
        CO = ["create"]
        for C in CO:
            with patch("sys.stdout", new=StringIO()) as OUT:
                self.assertFalse(HBNBCommand().onecmd(C))
                self.assertEqual(MSG, OUT.getvalue().strip())

    def test_smissing_cla(self):
        MSG = "** class name missing **"
        CO = ["show", ".show()", ]
        for C in CO:
            with patch("sys.stdout", new=StringIO()) as OUT:
                self.assertFalse(HBNBCommand().onecmd(C))
                self.assertEqual(MSG, OUT.getvalue().strip())

    def test_desmissing_cla(self):
        MSG = "** class name missing **"
        CO = ["destroy", ".destroy()"]
        for C in CO:
            with patch("sys.stdout", new=StringIO()) as OUT:
                self.assertFalse(HBNBCommand().onecmd(C))
                self.assertEqual(MSG, OUT.getvalue().strip())

