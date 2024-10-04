import tarfile
import json

def generate_metdata(package_path):
    with tarfile.open(package_path, 'r') as tar:
        tar.extractall()

        metadata = {
            "name": extract_name_from_manifest(),
            "version": extract_version_from_manifest(),
            "description": extract_description_from_manifest(),
            "author" : extract_author_from_manifest(),
            "license": extract_license_from_manifest(),
            "dependencies": extract_dependencies_from_manifest(),
            "checksum" : calculate_checksum()
        }

        with open("metadata.json", "w") as f:
            json.dump(metadata, f)