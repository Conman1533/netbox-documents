import base64
import binascii
import uuid

from django.core.files.base import ContentFile
from rest_framework import serializers


class UploadableBase64FileField(serializers.FileField):
    """
    Accepts a base64-encoded file string in JSON API requests.
    """

    def to_internal_value(self, data):
        if isinstance(data, str):
            if 'base64,' in data:
                _, data = data.split('base64,', 1)
            try:
                decoded_file = base64.b64decode(data)
            except (TypeError, binascii.Error):
                raise serializers.ValidationError('Invalid base64-encoded file.')
            file_name = str(uuid.uuid4())[:12]
            extension = self.get_file_extension(file_name, decoded_file)
            if extension:
                file_name = f'{file_name}.{extension}'
            data = ContentFile(decoded_file, name=file_name)
        return super().to_internal_value(data)

    def get_file_extension(self, filename, decoded_file):
        return ''
