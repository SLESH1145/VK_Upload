import vk_api
from config import token, group_id
import os, time

session = vk_api.VkApi(token=token)
vk = session.get_api()


def import_video(file_folder):
    print('Please wait...')
    name_videos = os.listdir(file_folder)
    mp4 = filter(lambda x: x.endswith('.mp4'), name_videos)
    zip_paths = list(mp4)
    for path in zip_paths:
        upload = vk_api.VkUpload(session)
        name = path.removesuffix('.mp4')
        time.sleep(3)
        download = upload.video(video_file=f'{file_folder}/{path}',
                                name=name,
                                group_id=group_id)
        print(f"[+] Video: {path}\n"
              f"id: {download['video_id']} is loaded")

def main():
    path = "C:/Users/magic/Videos/Captures"
    import_video(path)
    print('Download finished')

if __name__ == '__main__':
    main()
