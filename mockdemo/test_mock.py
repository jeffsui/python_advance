from mymodule import rm
import unittest
import unittest.mock as mock


class RmTestCase(unittest.TestCase):
    @mock.patch("mymodule.os.path")
    @mock.patch("mymodule.os")
    def test_rm(self,mock_os,mock_path):
        mock_path.isfile.return_value = False
        rm("any path")
        self.assertFalse(mock_os.remove.called,"Failed to not remove the file if not present")
        mock_path.isfile.return_value = True
        rm("any path")
        mock_os.remove.assert_called_with("any path")