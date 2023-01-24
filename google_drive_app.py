import argparse

from GoogleDriveManager import GoogleDriveManager
        
def parser() -> None:
    """
    Parses arguments
    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u", "--upload-file", help="Pass a file to be uploaded to GDrive", type=str
    )
    parser.add_argument(
        "-i",
        "--drive_id",
        help="Requested drive id",
        type=str
    )
    parser.add_argument(
        "-d", "--download-file", help="Download the requested file", type=str
    )
    args = parser.parse_args()
    client = GoogleDriveManager()
    if args.upload_file:
        client.upload(args.upload_file, args.drive_id)
    elif args.download_file:
            client.download_file(args.download_file, args.drive_id)
    else:
        print("No valid options provided!")


if __name__ == "__main__":
    parser()