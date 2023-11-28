import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PIL import Image
import pytesseract

class TextExtractorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Text Extractor')
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel('Pilih gambar untuk mengekstrak teks')
        self.layout.addWidget(self.label)

        self.browse_button = QPushButton('Pilih Gambar')
        self.browse_button.clicked.connect(self.browse_image)
        self.layout.addWidget(self.browse_button)

        self.extract_button = QPushButton('Ekstrak Teks')
        self.extract_button.clicked.connect(self.extract_text)
        self.layout.addWidget(self.extract_button)

        self.result_label = QLabel()
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def browse_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Pilih Gambar", "", "Image Files (*.png *.jpg *.bmp *.jpeg);;All Files (*)", options=options)
        if file_name:
            self.label.setText(f'Gambar dipilih: {file_name}')
            self.image_path = file_name

    def extract_text(self):
        try:
            if hasattr(self, 'image_path'):
                img = Image.open(self.image_path)
                text = pytesseract.image_to_string(img)
                self.result_label.setText(f'Hasil ekstraksi teks:\n{text}')
            else:
                self.result_label.setText('Silakan pilih gambar terlebih dahulu.')
        except Exception as e:
            self.result_label.setText(f'Error: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TextExtractorApp()
    window.show()
    sys.exit(app.exec_())