import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)

filters = {
    1: ("Grayscale", lambda frame: cv2.cvtColor(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)),
    2: ("Blur", lambda frame: cv2.GaussianBlur(frame, (35, 35), 0)),
    3: ("Edges", lambda frame: cv2.cvtColor(cv2.Canny(frame, 100, 200), cv2.COLOR_GRAY2BGR))
}

filter_ids = list(filters.keys())
current_idx = 0


def apply_filter(frame, mode):
    if mode not in filters:
        return frame, "Original"
    name, func = filters[mode]
    return func(frame), name

with mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.4, min_tracking_confidence=0.4) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        output_frame = frame.copy()

        if results.multi_hand_landmarks and len(results.multi_hand_landmarks) == 2:
            points = []
            for hand_landmarks in results.multi_hand_landmarks:
                index_tip = hand_landmarks.landmark[8]
                thumb_tip = hand_landmarks.landmark[4]
                points.append((int(index_tip.x * w), int(index_tip.y * h)))
                points.append((int(thumb_tip.x * w), int(thumb_tip.y * h)))

            for (x, y) in points:
                cv2.circle(output_frame, (x, y), 4, (0, 0, 255), -1) #Tips of index and thumb

            #Create the polygon mask
            pts = np.array(points, dtype=np.int32)
            rect = cv2.convexHull(pts)
            mask = np.zeros(frame.shape[:2], dtype=np.uint8)
            cv2.fillPoly(mask, [rect], 255)

            #Apply the current filter ONLY to the polygon region
            filter_mode = filter_ids[current_idx]
            filtered_region, filter_name = apply_filter(frame.copy(), filter_mode)

            #Blending the frame and the mask
            output_frame = np.where(mask[:, :, None] == 255, filtered_region, frame)

            #Outline of the polygon mask
            cv2.polylines(output_frame, [rect], True, (255, 255, 255), 3)

        else:
            filter_name = filters[filter_ids[current_idx]][0] 

        #Show all posssible filters and underline the current one
        x, y = 10, 30
        menu_text = "   ".join([filters[i][0] for i in filter_ids])
        cv2.putText(output_frame, menu_text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (255, 0, 0), 2, cv2.LINE_AA)

        start_x = x
        for i, fid in enumerate(filter_ids):
            fname = filters[fid][0]
            (fw, fh), _ = cv2.getTextSize(fname, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)
            if i == current_idx:
                cv2.line(output_frame, (start_x, y + 10), (start_x + fw, y + 10), (0, 0, 255), 2)
            start_x += fw + 35

        cv2.imshow("Dynamic Filter Window", output_frame)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break
        elif key == ord('f'):
            current_idx = (current_idx + 1) % len(filter_ids)

cap.release()
cv2.destroyAllWindows()
