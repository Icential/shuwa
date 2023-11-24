# object detection thingy
# 24/11/23

# import dump
import cv2
import uuid
import os
import time


# define image collects
labels = ["thumbs_up", "thumbs_down"]
img_count = len(labels)


# create directories for images if it doesnt exist
IMG_PATH = os.path.join("images")

if os.path.exists(IMG_PATH):
    for label in labels:
        possible_path = os.path.join(IMG_PATH, label)
        if not os.path.exists(possible_path):
            os.mkdir(possible_path)


# capturing images
for label in labels:
    cap = cv2.VideoCapture(0) # capture video
    print(f"Collecting images for {label}.")
    time.sleep(3)

    for img_num in range(img_count):
        print(f"Collecting image no.{img_num}")
        r, frame = cap.read() # capture specific frame
        img_name = os.path.join(IMG_PATH, label, label + "-{}.jpg".format(str(uuid.uuid1()))) # create img label with uuid
        cv2.imwrite(img_name, frame) # write img file
        cv2.imshow("frame", frame) # show screen
        time.sleep(2)

        # exit key
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()

# use anaconda prompt, use labelimg directoey, "py labelimg.py"
# press w for selecting images