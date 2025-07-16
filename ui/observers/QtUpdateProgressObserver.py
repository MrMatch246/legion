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
from PyQt6 import QtCore

from app.actions.updateProgress.AbstractUpdateProgressObserver import AbstractUpdateProgressObserver
from ui.ancillaryDialog import ProgressWidget

from PyQt6.QtCore import QMetaObject, Qt

class QtUpdateProgressObserver(AbstractUpdateProgressObserver):
    def __init__(self, progressWidget: ProgressWidget):
        self.progressWidget = progressWidget

    def onStart(self) -> None:
        QMetaObject.invokeMethod(self.progressWidget, "show", Qt.ConnectionType.QueuedConnection)

    def onFinished(self) -> None:
        QMetaObject.invokeMethod(self.progressWidget, "hide", Qt.ConnectionType.QueuedConnection)

    def onProgressUpdate(self, progress: int, title: str) -> None:
        QMetaObject.invokeMethod(self.progressWidget, "setText", Qt.ConnectionType.QueuedConnection,
                                 QtCore.Q_ARG(str, title))
        QMetaObject.invokeMethod(self.progressWidget, "setProgress", Qt.ConnectionType.QueuedConnection,
                                 QtCore.Q_ARG(int, progress))
        QMetaObject.invokeMethod(self.progressWidget, "show", Qt.ConnectionType.QueuedConnection)
