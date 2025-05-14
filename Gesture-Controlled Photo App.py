import cv2
import mediapipe as mp
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.8)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

photo_counter = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            if index_tip.y < thumb_tip.y:
                photo_counter += 1
                filename = f"photo_{photo_counter}.png"
                cv2.imwrite(filename, frame)
                time.sleep(1)

    cv2.imshow("Gesture-Controlled Photo App", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
