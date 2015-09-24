# -*- coding:utf-8 -*-
import sys
import os
import base64
from PyQt4 import QtGui, QtCore, QtWebKit


class PageShotter(QtGui.QWidget):
    def __init__(self, url, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.url = url

    def shot(self):
        webView = QtWebKit.QWebView(self)
        webView.load(QtCore.QUrl(self.url))
        self.webPage = webView.page()
        self.connect(webView, QtCore.SIGNAL("loadFinished(bool)"), self.savePage)

    def savePage(self, finished):
        # print finished
        if finished:
            size = self.webPage.mainFrame().contentsSize()

            self.webPage.setViewportSize(QtCore.QSize(size.width(), size.height()))
            img = QtGui.QImage(size, QtGui.QImage.Format_ARGB32)
            painter = QtGui.QPainter(img)
            self.webPage.mainFrame().render(painter)
            painter.end()
            mUrl = self.url
            #对url进行base64加密，作为文件名
            mUrl = base64.encodestring(mUrl)
            # mUrl.replace('\\', '_')
            path = '../cache/' + mUrl + '.png'
            print path
            img.save(path)
        else:
            print u"网页加载失败！"
        self.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    u = "http://" + sys.argv[1] + "/"
    shotter = PageShotter(u)
    shotter.shot()
    sys.exit(app.exec_())
