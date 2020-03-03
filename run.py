import sys

from PyQt5.QtWidgets import QApplication

from dytt_gui import DyttGui

app = QApplication(sys.argv)
dytt_gui = DyttGui()
dytt_gui.show()
sys.exit(app.exec_())
