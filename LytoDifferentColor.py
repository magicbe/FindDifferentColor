# // ******************************************************* //
# // Lyto Different Color - Python - 魔幻小鱉 Ngô Khải Phong //
# // ********************************************************//
import pyautogui, time
# 自訂函數 FindDifferentColor(左上角座標x1, 左上角座標y1, 右下角座標x2, 右下角座標y2, 階層n, 執行次數ts, 延遲時間dl)
def FindDifferentColor(x1, y1, x2, y2, n, ts, dl):
    c = []
    # 遊戲範圍長度
    w = x2 - x1
    if n == 2:
        # 2x2階
        d = w // 3
        # 左上角第一個圓形中心點座標
        x = x1 + d
        y = y1 + d
    else:
        # 3x3階以上
    	# 兩個圓形中心距離d，半徑r
        d = w // n
        r = d // 2
        # 左上角第一個圓形中心點座標
        x = x1 + r
        y = y1 + r
    for t in range(1, ts + 1):
        im = pyautogui.screenshot()
        del c[:]
        c = [(0, 0, 0)] * n * n
        c[0] = im.getpixel((x, y))
        c[1] = im.getpixel((x + d, y))
        if n == 2:
            c[2] = im.getpixel((x, y + d))
        else:
            c[2] = im.getpixel((x + 2 * d, y))
        # print(c)
        if c[0] != c[1]:
            if c[0] != c[2]:
                pyautogui.click(x, y)
                time.sleep(dl)
            else:
                pyautogui.click(x + d, y)
                time.sleep(dl)
        else:
            for i in range(2, n * n):
                cx = x + (i % n) * d
                cy = y + (i // n) * d
                c[i] = im.getpixel((cx, cy))
                if c[0] != c[i]:
                    pyautogui.click(cx, cy)
                    time.sleep(dl)
                    # print(c)
                    break


#  Nox 模擬器(全螢幕)
# wx1 = 720 : wy1 = 470
# wx2 = 1190 : wy2 = 950
# 電腦網頁(全螢幕)，自行抓取3x3遊戲範圍的左上角座標和右下角座標
wx1 = 720; wy1 = 440
wx2 = 1190; wy2 = 910
# Start -> click(x, y)
pyautogui.click(950, 920)
time.sleep(3.1)
FindDifferentColor(wx1, wy1, wx2, wy2, 2, 3, 0.1)
FindDifferentColor(wx1, wy1, wx2, wy2, 3, 7, 0.1)
FindDifferentColor(wx1, wy1, wx2, wy2, 4, 10, 0.1)
FindDifferentColor(wx1, wy1, wx2, wy2, 5, 14, 0.1)
FindDifferentColor(wx1, wy1, wx2, wy2, 6, 13, 0.1)
FindDifferentColor(wx1, wy1, wx2, wy2, 7, 300, 0.1)
