import unittest
from unittest.mock import Mock
from notif import notify_admin as notif
# from inspect import currentframe

# def line_num():
#     cf = currentframe()
#     return cf.f_back.f_lineno

class testNotif(unittest.TestCase):

    def test_notif(self):
        mock_notif = Mock()
        notif(mock_notif,"This is a notification")

        mock_notif.notify.assert_called_once_with("admin", "This is a notification")

    def test_notif_exception(self):
        mock_notif = Mock()
        
        with self.assertRaises(ValueError):
            notif(mock_notif,"")
        
        mock_notif.notify.assert_not_called()

if __name__ == '__main__':
    unittest.main()