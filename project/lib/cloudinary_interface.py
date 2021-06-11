import cloudinary.uploader


class CloudinaryInterface:
    image_extensions = ['jpg', 'jpe', 'jpeg', 'png', 'gif', 'svg', 'webp']

    @classmethod
    def upload_image(cls, image, folder_name=''):
        img = image.name.split(".")
        img_ext = img[-1]
        if img_ext not in cls.image_extensions:
            return False
        upload_data = cloudinary.uploader.upload_large(
            image, folder=str(folder_name),
            resource_type="image")

        url = upload_data.get('url')
        return dict(url=url)
