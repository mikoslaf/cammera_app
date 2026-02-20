"""
gesture_tracker – moduł do śledzenia dłoni, twarzy i pozy ciała
za pomocą MediaPipe.

Przykład użycia:
    from gesture_tracker import GestureTracker

    with GestureTracker() as tracker:
        for frame, results in tracker.stream():
            if results.hands:
                for hand in results.hands:
                    print("Pięść:", hand.is_fist)
                    print("Pozycja dłoni:", hand.palm_center)
"""

from .detector import GestureTracker, DetectionResults, HandResult, FaceResult, PoseResult
from .camera import Camera
from .analysis import HandAnalyzer
from .models import ensure_model

__all__ = [
    "GestureTracker",
    "DetectionResults",
    "HandResult",
    "FaceResult",
    "PoseResult",
    "Camera",
    "HandAnalyzer",
    "ensure_model",
]