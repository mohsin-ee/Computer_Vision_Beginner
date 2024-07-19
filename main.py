import cv2

# Check if webcam is detected (replace 2 with the correct webcam index if needed)
cap = cv2.VideoCapture()

if not cap.isOpened():

    print("Error: Webcam not found \n unavailable!")

    exit()

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Check if frame is read successfully
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting...")
        
        break

    # Display the frame
    cv2.imshow('frame', frame)

    # Exit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam resource
cap.release()

# Close all open windows
cv2.destroyAllWindows()
