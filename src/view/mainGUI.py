#! /usr/bin/python

import wx

gameMain = wx.App(False)

gameFrame = wx.Frame(None, wx.ID_ANY, "ReaFID")

gameFrame.Show(True)
gameMain.Main(Loop)