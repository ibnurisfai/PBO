import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QTextEdit
from PyQt5.QtGui import QPixmap
from PIL import Image
import pytesseract

class ImageTextDisplayApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Image Text Display")
        self.setGeometry(100, 100, 800, 600)

        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap("placeholder.png"))  # Placeholder image

        self.load_button = QPushButton("Pilih Gambar", self)
        self.load_button.clicked.connect(self.load_image)

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.load_button)
        layout.addWidget(self.text_edit)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def load_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Pilih Gambar", "", "Gambar (*.png *.jpg *.jpeg *.bmp)")

        if file_path:
            try:
                # Buka gambar menggunakan Pillow (PIL)
                image = Image.open(file_path)

                # Tampilkan gambar di label
                pixmap = QPixmap(file_path)
                self.image_label.setPixmap(pixmap.scaledToWidth(400))

                # Gunakan Tesseract OCR untuk mengekstrak teks
                text = pytesseract.image_to_string(image)

                # Tampilkan teks di QTextEdit
                self.text_edit.setPlainText(text)
            except Exception as e:
                print(f"Error: {e}")

def main():
    app = QApplication(sys.argv)
    window = ImageTextDisplayApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
