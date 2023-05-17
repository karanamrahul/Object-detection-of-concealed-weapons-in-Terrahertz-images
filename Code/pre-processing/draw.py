from PIL import Image, ImageDraw

classes = ["HUMAN", "CL", "WB", "MD", "UNKNOWN", "KC", "CP", "SS", "CK", "KK", "LW", "GA"]



def yolo_to_xml_bbox(bbox, w, h ):
    # x_center, y_center width heigth
    w_half_len = (bbox[2] * w) / 2
    h_half_len = (bbox[3] * h) / 2
    xmin = int((bbox[0] * w) - w_half_len)
    ymin = int((bbox[1] * h) - h_half_len)
    xmax = int((bbox[0] * w) + w_half_len)
    ymax = int((bbox[1] * h) + h_half_len)

    return [xmin, ymin, xmax, ymax]


def draw_image(img, bboxes,classes_list):
    draw = ImageDraw.Draw(img)
    for bbox in bboxes:
        # add label to the image
        draw.text((bbox[0], bbox[1]), classes_list[bboxes.index(bbox)], fill="red")
        draw.rectangle(bbox, outline="red", width=2)
    img.save("example.jpg")
    img.show()


image_filename = "/home/jugaad/Evolv Prototype/Dataset/Object-detection-of-concealed-weapons-in-Terrahertz-images/Dataset/JPEGImages/S_P_F1_KK_F_RL_GA_V_RL_back_0907091834.jpg"
label_filename = "/home/jugaad/Evolv Prototype/Dataset/Object-detection-of-concealed-weapons-in-Terrahertz-images/Dataset/labels/S_P_F1_KK_F_RL_GA_V_RL_back_0907091834.txt"
bboxes = []

img = Image.open(image_filename)
classes_list = []
with open(label_filename, 'r', encoding='utf8') as f:
    for line in f:
        data = line.strip().split(' ')
        classes_list.append(classes[int(data[0])])
        bbox = [float(x) for x in data[1:]]
        bboxes.append(yolo_to_xml_bbox(bbox, img.width, img.height))

draw_image(img, bboxes,classes_list)