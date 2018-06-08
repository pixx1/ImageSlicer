import ImageSlicer

if __name__ == '__main__':
    # ImageSlicer.bysize("example.jpg", 2000, 2000, output_folder="slice_image", keep_end_sections=True)
    ImageSlicer.bynumber("example.jpg", 10, 10)
