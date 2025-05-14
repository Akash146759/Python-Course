import cv2
import numpy as np
import mediapipe as mp
import screen_brightness_control as sbc
import pycaw.pycaw as pyaudio

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            thumb_x, thumb_y = int(thumb_tip.x * frame.shape[1]), int(thumb_tip.y * frame.shape[0])
            index_x, index_y = int(index_tip.x * frame.shape[1]), int(index_tip.y * frame.shape[0])

            distance = np.linalg.norm(np.array([thumb_x, thumb_y]) - np.array([index_x, index_y]))
            
            volume = int(np.interp(distance, [50, 250], [0, 100]))
            brightness = int(np.interp(distance, [50, 250], [0, 100]))

            sbc.set_brightness(brightness)
            sessions = pyaudio.AudioUtilities.GetAllSessions()
            for session in sessions:
                volume_control = session.SimpleAudioVolume
                volume_control.SetMasterVolume(volume / 100, None)

            cv2.putText(frame, f'Volume: {volume}%', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, f'Brightness: {brightness}%', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    cv2.imshow("Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
