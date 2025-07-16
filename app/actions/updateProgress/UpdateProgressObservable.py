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
    If not, see <https://www.gnu.org/licenses/>.

Author(s): Shane Scott (sscott@shanewilliamscott.com), Dmitriy Dubson (d.dubson@gmail.com)
"""
from app.actions.updateProgress.AbstractUpdateProgressObservable import AbstractUpdateProgressObservable


from PyQt6.QtCore import QObject, pyqtSignal

class UpdateProgressObservable(QObject, AbstractUpdateProgressObservable):
    progressChanged = pyqtSignal(int, str)
    started = pyqtSignal()
    finishedSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._observers = []

    def finished(self):
        self.finishedSignal.emit()  # emit signal
        for observer in self._observers:
            observer.onFinished()

    def start(self):
        self.started.emit()  # emit signal
        for observer in self._observers:
            observer.onStart()

    def updateProgress(self, progress, title=""):
        self.progressChanged.emit(progress, title)  # emit signal
        for observer in self._observers:
            observer.onProgressUpdate(progress, title)

