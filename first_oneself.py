import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from datetime import datetime

class CheckInDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("签到系统")
        self.setGeometry(300, 300, 400, 200)

        layout = QVBoxLayout()

        title_label = QLabel("签到系统", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title_label)

        reminder_label = QLabel("请确认您的签到/签退操作", self)
        reminder_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(reminder_label)

        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.time_label)
        self.update_time()

        button_layout = QVBoxLayout()
        self.checkin_btn = QPushButton("立即签到", self)
        self.checkin_btn.clicked.connect(self.check_in)
        button_layout.addWidget(self.checkin_btn)

        self.checkout_btn = QPushButton("立即签退", self)
        self.checkout_btn.clicked.connect(self.check_out)
        button_layout.addWidget(self.checkout_btn)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def update_time(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.setText(f"当前时间：{current_time}")

    def check_in(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("attendance.txt", "a", encoding="utf-8") as f:
            f.write(f"【签到】时间：{current_time}\n")
        self.close()

    def check_out(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("attendance.txt", "a", encoding="utf-8") as f:
            f.write(f"【签退】时间：{current_time}\n")
        self.close()

    def closeEvent(self, event):
        if not self.checkin_btn.isEnabled():
            return
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("attendance.txt", "a", encoding="utf-8") as f:
            f.write(f"【自动签到】时间：{current_time}（窗口关闭触发）\n")
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = CheckInDialog()
    dialog.show()
    sys.exit(app.exec_())