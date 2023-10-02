#!/usr/bin/python3
"""Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""

import pep8
import models
import inspect
import unittest
from models import user
from datetime import datetime
from models.base_model import BaseModel

User = user.User

class TestUserDocs(unittest.TestCase):
    """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
    @classmethod
    def setUpClass(cls):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_conformance_user(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_user(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_user_module_docstring(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        self.assertIsNot(user.__doc__, None,
                         "user.py needs a docstring")
        self.assertTrue(len(user.__doc__) >= 1,
                        "user.py needs a docstring")

    def test_user_class_docstring(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")

    def test_user_func_docstrings(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestUser(unittest.TestCase):
    """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
    def test_is_subclass(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_email_attr(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        if models.storage_t == 'db':
            self.assertEqual(user.email, None)
        else:
            self.assertEqual(user.email, "")

    def test_password_attr(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        if models.storage_t == 'db':
            self.assertEqual(user.password, None)
        else:
            self.assertEqual(user.password, "")

    def test_first_name_attr(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        if models.storage_t == 'db':
            self.assertEqual(user.first_name, None)
        else:
            self.assertEqual(user.first_name, "")

    def test_last_name_attr(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        if models.storage_t == 'db':
            self.assertEqual(user.last_name, None)
        else:
            self.assertEqual(user.last_name, "")

    def test_to_dict_creates_dict(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        u = User()
        new_d = u.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in u.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = User()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "User")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))
