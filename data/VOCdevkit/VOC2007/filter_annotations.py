import xml.etree.ElementTree as ET
import os


classes = ["person", "mobile"]
path = "./Annotations"
image_path = "./JPEGImages"


def clean_lables():
    for i, file_name in enumerate(os.listdir(path)):

        tree = ET.parse(os.path.join(path, file_name))

        root = tree.getroot()
        objects = [object_ for object_ in root.findall("object")]

        for object_ in objects:
            obj_name = object_.find("name").text

            if obj_name == "cell phone":
                object_.find("name").text = "mobile"

            elif obj_name not in classes:
                root.remove(object_)

        tree.write(os.path.join(path, file_name))


def clean_empty_images():
    for i, file_name in enumerate(os.listdir(path)):

        tree = ET.parse(os.path.join(path, file_name))
        fname = file_name.split(".")[0]

        root = tree.getroot()
        objects = [object_ for object_ in root.findall("object")]

        if not objects:
            os.remove(os.path.join(path, file_name))
            os.remove(os.path.join(image_path, f"{fname}.jpg"))


clean_lables()
clean_empty_images()
