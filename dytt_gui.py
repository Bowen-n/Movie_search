import sys
from threading import Thread

import pyperclip
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QTreeWidgetItem, QWidget

from base_gui import Ui_Form
from dytt import Dytt


class DyttGui(QWidget, Ui_Form):

    def __init__(self, parent=None):
        super(DyttGui, self).__init__(parent)
        self.setupUi(self)

        # core spider
        self.dytt = Dytt()

        # set status
        self.status = QtWidgets.QLabel(self)
        self.gridLayout.addWidget(self.status, 2, 0, 1, 3)

        self._translate = QtCore.QCoreApplication.translate
        self.status.setText(self._translate("Form", "当前状态: 未开始查找"))

        # event
        self.search_button.clicked.connect(lambda: Thread(target=self._search).start())
        self.lineEdit.returnPressed.connect(lambda: Thread(target=self._search).start())
        self.copy_link.clicked.connect(self._copy_link)

        # last search
        self.last_search = ""

    def _search(self):
        movie_name = str(self.lineEdit.text())
        if movie_name == self.last_search:
            return

        self.last_search = movie_name

        # status
        self.status.setText(self._translate("Form", "当前状态:正在查找请稍后..."))
        # search
        movie_list = self.dytt.search(movie_name)

        # display
        self.search_result.clear()
        record_len = 0
        if movie_list is not None:
            record_len = len(movie_list)
            for movie in movie_list:
                item = QTreeWidgetItem()
                item.setText(0, movie['name'])
                item.setText(1, movie['definition'])
                item.setText(2, movie['link'])
                self.search_result.addTopLevelItem(item)

        self.status.setText(self._translate("Form", "当前状态:查找结束, 共{}条记录".format(record_len)))


    def _copy_link(self):
        item = self.search_result.currentItem()
        if item is None:
            return
        pyperclip.copy(item.text(2))
        self.status.setText(self._translate("Form", "当前状态:已复制下载链接到剪贴板"))

