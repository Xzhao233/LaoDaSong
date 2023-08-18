import tkinter as tk
from tkinter import filedialog
import fleep
import ffmpeg
import os
import readchar

def speed_up_audio(file_path):
    # 获取文件名和扩展名
    file_name, file_ext = os.path.splitext(file_path)
    output_file_path = file_name + "_output" + file_ext
    audio_input = ffmpeg.input(file_path)
    # 首先将音频速度加快2倍，同时改变音调
    audio_speed_up = audio_input.filter('asetrate', '44100*2.0')
    # 然后将音频速度减半，但不改变音调
    audio_final = audio_speed_up.filter('atempo', 0.5)
    audio_final.output(output_file_path).run()
    return output_file_path


def is_audio_file(file_path):
    # 以二进制模式打开文件
    with open(file_path, "rb") as file:
        info = fleep.get(file.read(128))
        # 判断文件的类型是否是音频
        if "audio" in info.type:
            return True
        else:
            return False


try:
    # 获取选择文件路径
    # 实例化
    root = tk.Tk()
    root.withdraw()
    # 获取文件夹路径
    f_path = filedialog.askopenfilename()
    print('\n获取的文件地址：', f_path)

    if is_audio_file(f_path):
        print('输出的路径：', speed_up_audio(f_path))
        print("按任意键退出...")
        readchar.readchar()
    else:
        print("选择的好像不是一个音频文件（")
        print("按任意键退出...")
        readchar.readchar()
except Exception as e:
    print('艹，出错了。')
    print("请尝试下载ffmpeg，然后把ffmpeg添加到环境变量PATH，当前目录也可以")
    print("如果无效，请把以下错误信息提供给寄术支持人员（有没有就不到了）：", e)
    print("按任意键退出...")
    readchar.readchar()
