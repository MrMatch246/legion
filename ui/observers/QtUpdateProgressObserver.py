"""
LEGION (https://shanewilliamscott.com)
Copyright (c) 2024 Shane Scott

    This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
    License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
    version.

    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
    warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
    details.

    You should have received a copy of the GNU General Public License along with this program.
    If not, see <http://www.gnu.org/licenses/>.

Author(s): Shane Scott (sscott@shanewilliamscott.com), Dmitriy Dubson (d.dubson@gmail.com)
"""
from PyQt6.QtCore import QObject, pyqtSignal
from app.actions.updateProgress.AbstractUpdateProgressObserver import AbstractUpdateProgressObserver
from ui.ancillaryDialog import ProgressWidget


class QtUpdateProgressObserver(QObject, AbstractUpdateProgressObserver):
    startSignal = pyqtSignal()
    finishSignal = pyqtSignal()
    progressSignal = pyqtSignal(int, str)

    def __init__(self, progressWidget: ProgressWidget):
        super().__init__()
        self.progressWidget = progressWidget
        self.startSignal.connect(self._onStart)
        self.finishSignal.connect(self._onFinished)
        self.progressSignal.connect(self._onProgressUpdate)

    def onStart(self) -> None:
        self.startSignal.emit()

    def onFinished(self) -> None:
        self.finishSignal.emit()

    def onProgressUpdate(self, progress: int, title: str) -> None:
        self.progressSignal.emit(progress, title)

    # Slots to run in main thread
    def _onStart(self):
        self.progressWidget.show()

    def _onFinished(self):
        self.progressWidget.hide()

    def _onProgressUpdate(self, progress: int, title: str):
        self.progressWidget.setText(title)
        self.progressWidget.setProgress(progress)
        self.progressWidget.show()