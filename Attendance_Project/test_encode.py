import unittest
from unittest.mock import patch, MagicMock
from EncodeGenerator import encode_event
import os

class TestEncodeEvent(unittest.TestCase):

    @patch('cv2.imread')
    @patch('cv2.cvtColor')
    @patch('face_recognition.face_encodings')
    @patch('os.listdir', return_value=["1.png", "7.png"])
    def test_encode_event(self, mock_listdir, mock_cvtColor, mock_face_encodings, mock_imread):
        mock_cvtColor.return_value = MagicMock()
        mock_imread.return_value = MagicMock()
        mock_face_encodings.return_value = [MagicMock()]

        # Ensure that the mocked listdir returns the actual file names for the Images folder
        with patch('os.path.join', side_effect=os.path.join) as mock_path_join:
            encode_event()

        mock_listdir.assert_called_once_with('Images')
        mock_cvtColor.assert_called()
        mock_imread.assert_called()
        mock_face_encodings.assert_called()

        # Ensure that os.path.join is called with the correct arguments
        mock_path_join.assert_any_call('Images', '1.png')
        mock_path_join.assert_any_call('Images', '7.png')

if __name__ == '__main__':
    unittest.main()
