const video = document.getElementById('video');
const speakBtn = document.getElementById('speakBtn');
const recognizedText = document.getElementById('recognizedText');

let isRecording = false;
let previousWords = [];

// Access the webcam
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(err => {
        console.error('Error accessing the webcam: ' + err);
    });

// Capture image from video and send it to the server
function captureImage() {
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth || 640;
    canvas.height = video.videoHeight || 480;
    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    return canvas.toDataURL('image/jpeg');
}

// Start sending frames to the server when the button is pressed
let intervalId;
speakBtn.addEventListener('mousedown', () => {
    isRecording = true;
    previousWords = [];  // Reset previous words when the button is pressed
    recognizedText.textContent = "Listening for hand signs...";

    // Start capturing images every second
    intervalId = setInterval(() => {
        if (isRecording) {
            const imageData = captureImage();

            fetch('/process_image', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ image: imageData, previous_words: previousWords })
            })
            .then(response => response.json())
            .then(result => {
                previousWords = result.previous_words;
                recognizedText.textContent = result.generated_sentence;
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    }, 1000);
});

// Stop sending frames when the button is released
speakBtn.addEventListener('mouseup', () => {
    isRecording = false;
    clearInterval(intervalId);
});
