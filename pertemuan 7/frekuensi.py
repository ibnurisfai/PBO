import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import numpy as np
import pyaudio
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class VoiceFrequencyAnalyzer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

        # Inisialisasi variabel untuk merekam suara
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100

        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=self.FORMAT,
                                      channels=self.CHANNELS,
                                      rate=self.RATE,
                                      input=True,
                                      frames_per_buffer=self.CHUNK)

        # Inisialisasi plot gelombang frekuensi
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.ax.set_xlim(0, self.CHUNK / 2)
        self.ax.set_ylim(0, 10000)
        self.ax.set_xlabel('Frekuensi (Hz)')
        self.ax.set_ylabel('Amplitudo')

        # Menambahkan plot ke tata letak
        self.layout.addWidget(self.canvas)

        # Menggunakan timer untuk memperbarui plot secara berkala
        self.timer = self.startTimer(100)

    def init_ui(self):
        self.setWindowTitle("Voice Frequency Analyzer")
        self.setGeometry(100, 100, 800, 600)

        # Menambahkan plot ke tata letak
        self.layout = QVBoxLayout()

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    def timerEvent(self, event):
        self.record_audio()

    def record_audio(self):
        try:
            data = self.stream.read(self.CHUNK)
            audio_data = np.frombuffer(data, dtype=np.int16)

           
            # Menghitung dan memplot gelombang frekuensi
            fft_data = np.fft.fft(audio_data)
            frequencies = np.fft.fftfreq(len(fft_data), 1 / self.RATE)
            magnitude_spectrum = np.abs(fft_data)[:len(frequencies) // 2]

            self.ax.clear()
            self.ax.plot(frequencies[:len(frequencies) // 2], magnitude_spectrum)
            self.ax.set_xlim(0, self.RATE / 2)
            self.ax.set_ylim(0, 10000)
            self.ax.set_xlabel('Frekuensi (Hz)')
            self.ax.set_ylabel('Amplitudo')

            # Memperbarui plot
            self.canvas.draw()

        except Exception as e:
            print(f"Error: {e}")

    def closeEvent(self, event):
        # Memberhentikan stream dan audio ketika aplikasi ditutup
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

        # Menghentikan timer
        self.killTimer(self.timer)

        event.accept()

def main():
    app = QApplication(sys.argv)
    window = VoiceFrequencyAnalyzer()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
