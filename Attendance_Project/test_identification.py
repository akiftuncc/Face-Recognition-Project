import unittest
from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
import cv2
import numpy as np
from main import run_detection_coroutine
import asyncio


class TestRunDetectionCoroutine(TestCase):

    @patch('main.faceDetection.process')
    @patch('main.faceMesh.process')
    def test_run_detection_coroutine(self, mock_face_detection_process, mock_face_mesh_process):
        img = np.zeros((480, 640, 3), dtype=np.uint8)  # Create a sample image
        mock_face_detection_process.return_value.detections = [
            MagicMock(score=[0.95], location_data=MagicMock(relative_bounding_box=MagicMock(ymin=0.1, xmin=0.2, width=0.3, height=0.4), relative_keypoints=[]))
        ]
        mock_face_mesh_process.return_value.multi_face_landmarks = [MagicMock(landmark=[MagicMock(x=0.1, y=0.2, z=0.3)])]

        result = asyncio.run(run_detection_coroutine(img))

        # Your assertions based on the expected result

if __name__ == '__main__':
    unittest.main()
