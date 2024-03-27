# coding: utf-8
import os
import datetime


def get_chat_folders(root_path):
    """
    获取指定路径下所有聊天对象文件夹
    """
    chat_folders = []
    # 调用os.listdir(root_path)来获取指定路径下的所有文件和文件夹
    for folder_name in os.listdir(root_path):
        # 构建完整的文件夹路径
        folder_path = os.path.join(root_path, folder_name)
        if os.path.isdir(folder_path):
            chat_folders.append(folder_path)
    return chat_folders


def get_dat_images(chat_folder):
    """
    获取指定聊天对象文件夹中的所有DAT图片文件
    """
    dat_images = []
    # Image子文件夹的路径
    image_folder = os.path.join(chat_folder, "Image")
    for month_folder_name in os.listdir(image_folder):
        month_folder_path = os.path.join(image_folder, month_folder_name)
        if os.path.isdir(month_folder_path):
            for filename in os.listdir(month_folder_path):
                if filename.endswith('.dat'):
                    dat_images.append(os.path.join(month_folder_path, filename))
    return dat_images


def decode_dat_images(dat_files, output_folder):
    """
    解码DAT图片文件并存储到指定路径，并记录解码后图片的文件路径
    """
    decoded_img_paths = []  # 用于记录解码后图片的文件路径

    for dat_file in dat_files:
        # 根据DAT文件的格式判断异或值
        xor_value, image_format = get_xor_value(dat_file)

        if image_format == 1:
            mat = '.png'
        elif image_format == 2:
            mat = '.jpg'
        elif image_format == 3:
            mat = '.gif'
        elif image_format == 4:
            mat = '.bmp'
        elif image_format == 5 or image_format == 6:
            mat = '.tif'
        else:
            print(dat_file, "图片格式未知")
            continue

        # 获取当前文件的创建时间，并将其格式化为日期信息
        creation_time = datetime.datetime.fromtimestamp(os.path.getctime(dat_file))
        date_info = creation_time.strftime('%Y-%m-%d')

        # 生成解码后图片的文件名，格式为：日期信息_原文件名.扩展名
        decoded_filename = f"{date_info}_{os.path.splitext(os.path.basename(dat_file))[0]}{mat}"
        output_path = os.path.join(output_folder, decoded_filename)

        with open(dat_file, 'rb') as f:
            with open(output_path, 'wb') as out_file:
                for byte in f.read():
                    decoded_byte = byte ^ xor_value  # 执行异或运算
                    out_file.write(bytes([decoded_byte]))  # 写入解码后的字节

        # 记录解码后图片的文件路径
        decoded_img_paths.append(output_path)

    return decoded_img_paths


def get_xor_value(dat_file):
    """
    获取DAT文件的异或值和图片格式
    """
    # PNG 16进制文件头 89 50 4E 47 0D 0A 1A 0A
    # JPG 16进制文件头 FF D8
    # GIF 16进制文件头 47 49 46 38 39(37) 61
    # BMP 16进制文件头 42 4D
    # TIF 16进制文件头 4D 4D 或 49 49
    # 微信.bat 16进制 a1 86--->jpg  ab 8c--->jpg  dd 04--->png
    with open(dat_file, 'rb') as f:
        try:
            img_head = [(0x89, 0x50), (0xff, 0xd8), (0x47, 0x49), (0x42, 0x4D), (0X4D, 0X4D), (0X49, 0X49)]
            for now in f:
                format_num = 0
                for xor in img_head:
                    format_num = format_num + 1  # 记录格式 1:png 2:jpeg 3:gif 4:bmp 5/6:tif
                    i = 0
                    xor_value = []
                    dat_head = now[:2]  # 取前两组判断
                    for nowByte in dat_head:
                        xor_value.append(nowByte ^ xor[i])
                        i += 1
                    if xor_value[0] == xor_value[1]:
                        return xor_value[0], format_num
        except:
            pass
        finally:
            f.close()
