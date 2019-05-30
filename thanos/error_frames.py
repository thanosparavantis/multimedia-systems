import cv2

if __name__ == '__main__':
    video = cv2.VideoCapture('video2.mp4')
    prev_frame = None

    while video.isOpened():
        success, cur_frame = video.read()

        if not success:
            break

        if prev_frame is None:
            prev_frame = cur_frame.copy()
            continue

        error_frame = cv2.absdiff(cur_frame, prev_frame)
        cv2.imshow('Error Frame', error_frame)

        if cv2.waitKey(60) & 0xFF == ord('q'):
            break

        prev_frame = cur_frame.copy()

    video.release()
    cv2.destroyAllWindows()