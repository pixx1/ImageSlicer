import ImageSlicer

if __name__ == '__main__':
    ImageSlicer.bysize("example.jpg", 2000, 2000, output_folder="sliced_by_size", keep_end_sections=True)
    ImageSlicer.bynumber("example.jpg", 2, 2, "sliced_by_number", keep_end_sections=True)
