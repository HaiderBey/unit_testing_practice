import unittest
from auth import VALID_USERS, is_valid_user, authenticate, change_password, get_user

class testAuth(unittest.TestCase):

    def setUp(self):
        VALID_USERS.clear()
        VALID_USERS.update({
            "a": "apa",
            "b": "bpa",
            "c": "cpa"
        })
    
    def test_get_user(self):
        self.assertEqual(get_user("a"),"apa","get_user case sensitivity test fail")

        with self.assertRaises(KeyError) as context:
            get_user("notuser")
        self.assertEqual(str(context.exception), "'User does not exist'", "get_user() exception test fail")
        

    def test_is_valid_user(self):
        self.assertTrue(is_valid_user("a"))
        self.assertTrue(is_valid_user("A"))
        self.assertFalse(is_valid_user("hamadi"))
        self.assertFalse(is_valid_user(""))

    def test_authenticate(self):
        self.assertEqual(authenticate("a", "apa"), "Login successful")
        self.assertEqual(authenticate("a", "bpa"), "Incorrect password")
        self.assertEqual(authenticate("a", "kalimatoessr"), "Incorrect password")
        self.assertEqual(authenticate("c", ""), "Incorrect password")
        self.assertEqual(authenticate("mohsen", "securepass"), "User not found")
        self.assertEqual(authenticate("", "bpa"), "User not found")

    def test_change_pass(self):
        self.assertEqual(change_password("samirLousif","motdepassezeda8alet", ""), "User not found")
        self.assertEqual(change_password("c","motdepassezeda8alet", ""), "Incorrect old password")
        self.assertEqual(change_password("c","cpa", ""), "New password cannot be empty")
        self.assertEqual(change_password("c","cpa", "passjdid"), "Password changed successfully")
        self.assertEqual(authenticate("c", "passjdid"), "Login successful")


if __name__ == '__main__':
    unittest.main()