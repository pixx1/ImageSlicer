"""
Author: Jonas Schober
License GNU General Public License v3.0
"""

import os
from PIL import Image
from math import ceil
from typing import List, Dict
import ntpath


def bysize(image_path: str, width_new_image: int,
           height_new_image: int,
           output_folder: str ="sliced/",
           keep_end_sections: bool =True) -> None:
    """
    function for slicing images into smaller pieces.
    :param image_path: path to image file
    :param width_new_image: width of the new images
    :param height_new_image: height of the new images
    :param output_folder: output path, by default it's the folder sliced....
    :param keep_end_sections: the small end parts could be ignored, if you want, by default you keep them
    :return: None
    """

    def __validation_check(input_value):

        if input_value <= 0:
            print("Input below zero. Exit")
            exit()

    def __get_coordinates_for_grid(image_side, box_side) -> List[int]:
        coordinate_points = [0]
        counter = 0
        number_of_images_per_side = int(ceil(image_side / box_side))

        for adder in range(number_of_images_per_side):
            counter += box_side

            if counter <= image_side:

                coordinate_points.append(counter)
            else:
                if keep_end_sections:
                    # Use image size of the image as maximum value
                    coordinate_points.append(image_side)

        return coordinate_points

    def __create_list_of_boxes(x_coord_list, y_coord_list) -> List[Dict[str, int]]:
        list_of_boxes = []
        counter_x_min = 0
        counter_y_min = 0
        counter_x_max = 1
        counter_y_max = 1

        for number_of_box in range(int(number_of_new_boxes)):

            if counter_y_max < len(y_coord_list) and counter_x_max < len(x_coord_list):
                box = {"x_min": x_coord_list[counter_x_min],
                       "y_min": y_coord_list[counter_y_min],
                       "x_max": x_coord_list[counter_x_max],
                       "y_max": y_coord_list[counter_y_max]}

                counter_x_min += 1
                counter_x_max += 1

                if counter_x_min >= len(x_coord_list) - 1:
                    counter_x_min = 0
                    counter_y_min += 1

                if counter_x_max == len(x_coord_list):
                    counter_x_max = 1
                    counter_y_max += 1

                list_of_boxes.append(box)

        # pprint(list_of_boxes)
        return list_of_boxes

    def __crop_image(box_list: List[Dict[str, int]], output_path: str, show_image=False) -> None:
        """
        crop the input image in the manner the boxes are

        :param box_list: output of divide_image_into_boxes goes here
        :param output_path: path where the images should be stored
        :param show_image: If you want, you can see the image directly...
        :return: None
        """
        counter = 1
        for box_number in box_list:

            sliced_image = im.crop((box_number['x_min'],
                                    box_number['y_min'],
                                    box_number['x_max'],
                                    box_number['y_max']))

            original_file_name = ntpath.basename(image_path)

            if not os.path.isdir(output_path):
                os.makedirs(output_path)

            new_file_name = "{0}/{2}_{1}".format(str(output_path),
                                                 str(original_file_name),
                                                 "{0:0{width}}".format(counter, width=4))
            counter += 1
            sliced_image.save(new_file_name)

            if show_image:
                sliced_image.show()

    if not os.path.isfile(image_path):
        print("Input is not a file. Exit")
        exit()

    __validation_check(width_new_image)
    __validation_check(height_new_image)

    with Image.open(image_path) as im:
        width_of_the_image, height_of_the_image = im.size

        x_coordinates = __get_coordinates_for_grid(width_of_the_image, width_new_image)
        y_coordinates = __get_coordinates_for_grid(height_of_the_image, height_new_image)

        number_of_new_boxes = (len(x_coordinates) - 1) * (len(y_coordinates) - 1)
        print("Number of new pictures after splitting: " + str(number_of_new_boxes))

        list_of_dicts_with_boxes = __create_list_of_boxes(x_coordinates, y_coordinates)

        __crop_image(list_of_dicts_with_boxes, output_folder)
