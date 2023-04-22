import pyaudio
import wave
import threading
import datetime

class AudioRecorder:
    def __init__(self):
        self._is_recording = False
        self.audio = pyaudio.PyAudio()
        self.frames = []

    @property
    def is_recording(self):
        return self._is_recording

    @is_recording.setter
    def is_recording(self, value):
        self._is_recording = value
    
    def toggle_record(self):
        if not self.is_recording:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        self.is_recording = True
        self.frames = []

        # Open audio stream
        stream = self.audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        threading.Thread(target=self.record_audio, args=(stream,)).start()

    def record_audio(self, stream):
        while self.is_recording:
            self.frames.append(stream.read(1024))

    def stop_recording(self):
        self.is_recording = False

        # Close audio stream
        stream = self.audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        stream.stop_stream()
        stream.close()

        # Save audio to file with timestamp in filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
        filename = f"recordings/recording_{timestamp}.wav"
        wf = wave.open(filename, "wb")
        wf.setnchannels(1)
        wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b"".join(self.frames))
        wf.close()
