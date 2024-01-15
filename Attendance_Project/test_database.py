import unittest
from unittest.mock import patch, MagicMock
from AddDataToDatabase import create_student_number, create_name, create_major, create_year, take_pic, face_recorder, data_creator
from EncodeGenerator import encode_event


class TestStudentFunctions(unittest.TestCase):

    @patch('builtins.input', return_value='12345')  
    def test1_create_student_number(self, mock_input):
        result = create_student_number()
        self.assertEqual(result, '12345')

    @patch('builtins.input', return_value='John Doe')
    def test2_create_name(self, mock_input):
        result = create_name()
        self.assertEqual(result, 'John Doe')

    @patch('builtins.input', return_value='Computer Science')
    def test3_create_major(self, mock_input):
        result = create_major()
        self.assertEqual(result, 'Computer Science')

    @patch('builtins.input', return_value='2022')
    def test4_create_year(self, mock_input):
        result = create_year()
        self.assertEqual(result, 2022)

    @patch('firebase_admin.initialize_app')
    def test_data_creator(self, mock_initialize_app):
        with patch('firebase_admin.db.reference') as mock_reference, \
            patch('firebase_admin.db.Reference.child') as mock_child, \
            patch('firebase_admin.db.Reference.set'):
            data_creator('John Doe', '12345', 'Computer Science', 2022)
            mock_reference.assert_called_once_with('Students')


if __name__ == '__main__':
    unittest.main()
