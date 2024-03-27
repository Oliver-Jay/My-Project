# coding: utf-8
import os
import dlib
import cv2
import pickle
import numpy as np
import matplotlib.pyplot as plt


# 模型的路径中不能有中文，否则无法打开！
# 初始化dlib的人脸检测器和人脸特征提取器
detector = dlib.get_frontal_face_detector()
shape_predictor_path = "shape_predictor_68_face_landmarks.dat"
shape_predictor = dlib.shape_predictor(shape_predictor_path)

# 用于将检测到的人脸转换为128维特征向量的模型
facerec_path = "dlib_face_recognition_resnet_model_v1.dat"
facerec = dlib.face_recognition_model_v1(facerec_path)

# 规定人脸数据库保存路径
database_filename = r"D:\Program Files\Program\Python\Graduation Project\Face search\Face recognition search\Face Database\face_database.pkl"

# 在所有图片中检测人脸并计算特征，形参为图片保存文件夹路径
def detect_faces_and_compute_descriptor(image):
    faces = detector(image, 1)
    face_descriptors = []
    for face in faces:
        shape = shape_predictor(image, face)
        face_descriptor = np.array(facerec.compute_face_descriptor(image, shape))
        face_descriptors.append(face_descriptor)
    return faces, face_descriptors


# 在提供的待搜索图片中检测人脸并提取特征，形参为图片的绝对路径
def image_process(image_path):
    image = cv2.imread(image_path)
    _, face_descriptors = detect_faces_and_compute_descriptor(image)
    return face_descriptors


# 从文件夹中加载聊天图片，建立人脸特征数据库
def build_database(images_folder):
    database = {}
    for filename in os.listdir(images_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            filepath = os.path.join(images_folder, filename)
            image = cv2.imread(filepath)
            _, face_descriptors = detect_faces_and_compute_descriptor(image)
            if face_descriptors:
                database[filename] = (image, face_descriptors)
    return database

# 保存数据库到文件
def save_database(database, filename):
    with open(filename, 'wb') as file:
        pickle.dump(database, file)

# 从文件加载数据库
def load_database(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

# 比对人脸特征，返回匹配的图片列表
def find_matching_images(database, target_face_descriptors, mode='or'):
    matching_images = []
    for filename, (image, descriptors) in database.items():
        if mode == 'or':
            for target_descriptor in target_face_descriptors:
                for descriptor in descriptors:
                    distance = np.linalg.norm(target_descriptor - descriptor)
                    if distance < 0.6:  # 调整阈值
                        matching_images.append(filename)
                        break
        elif mode == 'and':
            all_matched = True
            for target_descriptor in target_face_descriptors:
                matched = False
                for descriptor in descriptors:
                    distance = np.linalg.norm(target_descriptor - descriptor)
                    if distance < 0.6:  # 调整阈值
                        matched = True
                        break
                if not matched:
                    all_matched = False
                    break
            if all_matched:
                matching_images.append(filename)
    return matching_images



# 聊天图片存放路径
images_folder = r"D:\Program Files\Program\Python\Graduation Project\Face search\Face recognition search\Images_decoded_all"
# 待搜索的人脸图片路径
target_image_path = r"D:\Program Files\Program\Python\Graduation Project\Face search\Face recognition search\example-mix.png"

# 检查是否存在已保存的数据库文件，如果存在则加载，否则重新建立数据库
if os.path.exists(database_filename):
    database = load_database(database_filename)
else:
    # 建立人脸特征数据库
    database = build_database(images_folder)
    # 保存数据库到文件
    save_database(database, database_filename)

# 检测并提取待搜索图片的人脸特征
target_face_descriptors = image_process(target_image_path)

# 寻找匹配的聊天图片
matching_images = find_matching_images(database, target_face_descriptors)

# 输出匹配的图片列表
print("匹配的图片：", matching_images)

# 一次性打开所有匹配的图片
plt.figure(figsize=(15, 10))
num_cols = 4
num_rows = len(matching_images) // num_cols + (len(matching_images) % num_cols > 0)
for i, filename in enumerate(matching_images):
    image_path = os.path.join(images_folder, filename)
    image = cv2.imread(image_path)
    plt.subplot(num_rows, num_cols, i + 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(filename)
    plt.axis('off')

plt.tight_layout()
plt.show()

# 追加的额外功能：逻辑“和”查找
# 如果要查找包含多张人脸的图片，提供多张人脸图片路径即可
# target_image_paths = [path1, path2, ...]
# target_face_descriptors = []
# for path in target_image_paths:
#     target_face_descriptors.extend(detect_faces_and_compute_descriptors(path))
# matching_images_and = find_matching_images(database, target_face_descriptors, mode='and')
# print("匹配的图片（逻辑“和”）：", matching_images_and)

