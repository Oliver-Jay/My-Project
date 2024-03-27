# coding: utf-8
from utils import get_chat_folders, get_dat_images, decode_dat_images
import os
import json


# 定义输入和输出路径
input_root_path = r'D:\AppData\Tencent\WeChat\WeChat Files\wxid_lx7voay5c75q22\FileStorage\MsgAttach'
output_folder = r'D:\Program Files\Program\Python\Graduation Project\Face search\Wechat picture extraction\Images_decoded_all'
# 定义状态文件，记录上一次图片提取的状态，用于对解码图片库的自动更新
status_file = 'status.json'

# 如果状态文件存在，则执行自动更新
if os.path.exists(status_file):
    # 读取状态文件
    with open(status_file, 'r') as f:
        status = json.load(f)

    # 获取所有聊天对象文件夹
    chat_folders = get_chat_folders(input_root_path)

    # 遍历每个聊天对象文件夹
    for chat_folder in chat_folders:
        chat_folder_name = os.path.basename(chat_folder)
        if chat_folder_name not in status:
            status[chat_folder_name] = {}

        # 获取该聊天对象文件夹中的所有DAT图片文件
        dat_images = get_dat_images(chat_folder)

        # 检查状态中是否存在该聊天对象，如果不存在则新增
        if chat_folder_name not in status:
            status[chat_folder_name] = {}

        # 比较现有的dat_images和status中的DAT文件路径记录
        for img_path in dat_images:
            if img_path not in status[chat_folder_name]:
                # 如果有新增的图片文件，则解码并更新状态
                decoded_img_path = decode_dat_images([img_path], output_folder)
                status[chat_folder_name][img_path] = decoded_img_path[0]

        # 如果有被删除的图片文件，则根据status中对应的解码文件路径将其删除并更新状态
        for img_path in list(status[chat_folder_name]):
            if img_path not in dat_images:
                decoded_img_path = status[chat_folder_name][img_path]
                if os.path.exists(decoded_img_path):
                    os.remove(decoded_img_path)
                del status[chat_folder_name][img_path]

    # 将更新后的状态写入状态文件
    with open(status_file, 'w') as f:
        json.dump(status, f, indent=4)

# 如果状态文件不存在，则进行首次解码
else:
    # 获取所有聊天对象文件夹
    chat_folders = get_chat_folders(input_root_path)

    # 遍历每个聊天对象文件夹
    for chat_folder in chat_folders:
        chat_folder_name = os.path.basename(chat_folder)

        # 获取该聊天对象文件夹中的所有DAT图片文件
        dat_images = get_dat_images(chat_folder)

        # 解码并保存所有图片，并记录状态
        for img_path in dat_images:
            decoded_img_path = decode_dat_images([img_path], output_folder)
            status = {chat_folder_name: {img_path: decoded_img_path[0]}}

    # 将首次解码后的状态写入状态文件
    with open(status_file, 'w') as f:
        json.dump(status, f, indent=4)
