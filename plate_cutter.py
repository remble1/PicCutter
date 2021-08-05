# cut plate from pic using YOLO date

import json
import cv2
from PIL import Image
from time import sleep
path = r"./mnt/plate_immages/result.txt"

f = open(path, "r")
result = f.read()
stud_obj = json.loads(result)
long = len(stud_obj)

for i in range (0, long):
    how_many_plate = len(stud_obj[i]['objects'])
    print(f"{i} / {long}")
    try:
        if how_many_plate > 1:
            #print("wchodzi w 2")
            for c in range (0, how_many_plate):
                center_x = stud_obj[i]['objects'][0]['relative_coordinates']['center_x']
                center_y = stud_obj[i]['objects'][0]['relative_coordinates']['center_y']
                width = stud_obj[i]['objects'][0]['relative_coordinates']['width']
                height = stud_obj[i]['objects'][0]['relative_coordinates']['height']
                predict = stud_obj[i]['objects'][0]['confidence']
                pic_path = stud_obj[i]['filename']
                _lp = pic_path.split('/')
                license_plate_number = _lp[3].split(".")[0]

                correct_path = fr"D:\Workspace\miaryWagi\opencv_detect_simple\mnt\plate_immages\{_lp[-1]}"

                car_img = cv2.imread(correct_path, cv2.IMREAD_UNCHANGED)
                #cv2.imshow(f"Car plate: {license_plate_number}", car_img)
                size_car_img_Y = car_img.shape[0]  # w dół 450
                size_car_img_X = car_img.shape[1]  # w prawo 600

                of_center_x = center_x * size_car_img_X  # center pt value make from pic size
                of_center_y = center_y * size_car_img_Y

                height_pic = height * size_car_img_Y
                width_pic = width * size_car_img_X

                start_pt_x = int(of_center_x - (1 / 2 * width_pic))  # make start pkt
                start_pt_y = int(of_center_y - (1 / 2 * height_pic))

                end_pt_x = of_center_x + (1 / 2 * width_pic)
                end_pt_y = of_center_y + (1 / 2 * height_pic)


                im = Image.open(correct_path)

                area = (start_pt_x, start_pt_y, end_pt_x, end_pt_y)  # cuting area

                plate = im.crop(area)
                resized_image = plate.resize((200, 50))
                resized_image.save(fr"D:/fotyOpenCv/{license_plate_number.upper()}({c}).jpg")


        else:
            center_x = stud_obj[i]['objects'][0]['relative_coordinates']['center_x']
            center_y = stud_obj[i]['objects'][0]['relative_coordinates']['center_y']
            width = stud_obj[i]['objects'][0]['relative_coordinates']['width']
            height = stud_obj[i]['objects'][0]['relative_coordinates']['height']
            predict = stud_obj[i]['objects'][0]['confidence']
            pic_path = stud_obj[i]['filename']
            _lp = pic_path.split('/')
            license_plate_number = _lp[3].split(".")[0]
            #print(pic_path)
            correct_path = fr"D:\Workspace\miaryWagi\opencv_detect_simple\mnt\plate_immages\{_lp[-1]}"
            car_img = cv2.imread(correct_path, cv2.IMREAD_UNCHANGED)
            #cv2.imshow(f"Car plate: {license_plate_number}", car_img)
            size_car_img_Y = car_img.shape[0] # w dół 450
            size_car_img_X = car_img.shape[1] # w prawo 600

            of_center_x = center_x * size_car_img_X # center pt value make from pic size
            of_center_y = center_y * size_car_img_Y

            height_pic = height * size_car_img_Y
            width_pic = width * size_car_img_X

            start_pt_x = int(of_center_x - (1/2*width_pic))  # make start pkt
            start_pt_y = int(of_center_y - (1/2*height_pic))

            end_pt_x = of_center_x + (1/2*width_pic )
            end_pt_y = of_center_y + (1/2*height_pic)



            im = Image.open(correct_path)

            area = (start_pt_x, start_pt_y, end_pt_x, end_pt_y) # cuting area

            plate = im.crop(area)
            resized_image = plate.resize((200, 50))
            resized_image.save(fr"D:/fotyOpenCv/{license_plate_number.upper()}.jpg")




    except:
        pass


# plate.show()

# cropped_image = car_img[50:120, 150:350]
# cropped_image1 = car_img[int(start_pt_x):int(start_pt_y), int(end_pt_x):int(end_pt_y)]
# cv2.imshow("dupa", cropped_image)