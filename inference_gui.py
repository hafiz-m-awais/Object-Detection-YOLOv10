import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from ultralytics import YOLO
from PIL import Image, ImageTk

# Load the trained YOLOv10n model
model = YOLO("D:/MS Data Science/Semester 2/Deep Learning/Assignments/Assignment 2/Inference app/yolov10n_trained.pt")
# Define function to process the frame and perform inference
def process_frame(frame):
    results = model(frame)
    annotated_frame = results[0].plot()  # Draw bounding boxes on the frame
    return annotated_frame
    

# Create a GUI application using Tkinter
class ObjectDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YOLOv10n Object Detection Inference")
        self.root.geometry("800x600")
        
        self.capture = None
        self.is_video = False

        # Create buttons
        self.start_button = tk.Button(root, text="Start Webcam", width=20, command=self.start_webcam)
        self.start_button.pack(pady=20)

        self.upload_button = tk.Button(root, text="Upload Video", width=20, command=self.upload_video)
        self.upload_button.pack(pady=20)

        self.quit_button = tk.Button(root, text="Quit", width=20, command=root.quit)
        self.quit_button.pack(pady=20)

        # Label for displaying the frame
        self.video_label = tk.Label(root)
        self.video_label.pack()

    def start_webcam(self):
        """Start webcam video stream"""
        self.is_video = False
        self.capture = cv2.VideoCapture(0)
        self.update_frame()

    def upload_video(self):
        """Upload a recorded video"""
        self.is_video = True
        video_path = filedialog.askopenfilename(title="Select Video", filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")])
        if video_path:
            self.capture = cv2.VideoCapture(video_path)
            self.update_frame()

    def update_frame(self):
        """Update frames for webcam or video"""
        ret, frame = self.capture.read()
        if ret:
            # Process the frame for object detection
            processed_frame = process_frame(frame)

            # Convert to ImageTk format to display in Tkinter
            processed_frame = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(processed_frame)
            img = ImageTk.PhotoImage(img)

            # Display the frame
            self.video_label.config(image=img)
            self.video_label.image = img

            # Loop if it's a webcam stream or if there's still video left
            if not self.is_video or (self.capture.isOpened() and ret):
                self.video_label.after(10, self.update_frame)
            else:
                messagebox.showinfo("End of Video", "Video playback finished.")
                self.capture.release()

# Main function to run the GUI
def run():
    root = tk.Tk()
    app = ObjectDetectionApp(root)
    root.mainloop()

# Run the application
if __name__ == "__main__":
    run()
