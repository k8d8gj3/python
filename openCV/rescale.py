import cv2 as cv

# Importing image
img = cv.imread('photos/cat_large.jpg')
cv.imshow('Cat', img)

# Importing video
video = cv.VideoCapture('videos/dog.mp4')

# Playing video
def play_video(video):
    while True:
        isTrue, frame = video.read()

        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break
    video.release()

# Rescaling frame (video, image, live video)
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height )

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Rescaling live video only
def changeRes(width, height):
    video.set(3, width)
    video.set(4, height)

cv.imshow('Cat', rescaleFrame(img, .3))
play_video(video)

cv.waitKey(0)
cv.destroyAllWindows()
