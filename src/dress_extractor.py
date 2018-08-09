import json

DRESS_FOLDER = "../data/json/"

ID_NAME = "retrieval_dresses.json"
TEST_NAME = "test_pairs_dresses.json"
TRAIN_NAME = "train_pairs_dresses.json"
PHOTO_FILE = "../data/photos/photos_dress.txt"

def read_json(file_name):
    with open(file_name) as f:
        obj = json.loads(f.readline())
    return obj


def get_photo_ids(obj, retr_dict):
    photos = set()
    for item in obj:
        photos.add(item["photo"])
        product_photos = retr_dict[item["product"]]
        photos.update(product_photos)

    return photos


if __name__ == "__main__":
    id_to_photo_dirty = read_json(DRESS_FOLDER+ID_NAME)
    id_to_photo_clean = {}
    for item in id_to_photo_dirty:
        if item["product"] in id_to_photo_clean:
            id_to_photo_clean[item["product"]].append(item["photo"])
        else:
            id_to_photo_clean[item["product"]] = [item["photo"]]
    test_dress = read_json(DRESS_FOLDER + TEST_NAME)
    train_dress = read_json(DRESS_FOLDER + TRAIN_NAME)
    test_set = get_photo_ids(test_dress, id_to_photo_clean)
    train_set = get_photo_ids(train_dress, id_to_photo_clean)
    result_set = test_set|train_set

    with open(PHOTO_FILE, "w") as new_ph_file:
        with open("../data/photos/photos.txt") as ph_file:
            for line in ph_file:
                id = int(line.split(",")[0])
                if id in result_set:
                    new_ph_file.write(line)