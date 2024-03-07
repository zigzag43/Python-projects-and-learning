import cv2
import time
import mediapipe as mp
import pyautogui
import threading
cTime=0
pTime=0

# Function for hand detection and cursor movement
def detect_hands_and_move_cursor():
    global index_x, index_y
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks

        if hands:
            for hand in hands:
                landmarks = hand.landmark
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    if id == 8:
                        index_x = (screen_width / frame_width) * x
                        index_y = (screen_height / frame_height) * y

        time.sleep(0.01)  # Adjust sleep time to control processing frequency

# Initialize hand detection model
hand_detector = mp.solutions.hands.Hands(
    max_num_hands=1,
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
drawing = mp.solutions.drawing_utils
mphands = mp.solutions.hands

# Initialize variables
index_x, index_y = 0, 0
screen_width, screen_height = pyautogui.size()
cap = cv2.VideoCapture(0)

# Start a separate thread for hand detection and cursor movement
thread = threading.Thread(target=detect_hands_and_move_cursor)
thread.start()

# Main loop for displaying frames
while True:
    ret, frame = cap.read()

    if not ret:
        break
    detect_hands_and_move_cursor()

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 255), 3)

    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
