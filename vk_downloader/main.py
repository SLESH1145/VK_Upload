import vk_api
from config import token, group_id
import os, time

session = vk_api.VkApi(token= token)
vk = session.get_api()


def import_video():
    directory = 'C:/Users/magic/Videos/Captures'
    name_videos = os.listdir(directory)
    mp4 = filter(lambda x: x.endswith('.mp4'), name_videos)
    zip_paths = list(mp4)
    for path in zip_paths:
        upload = vk_api.VkUpload(session)
        name = path.removesuffix('.mp4')
        time.sleep(3)
        download = upload.video(video_file=f'C:/Users/magic/Videos/Captures/{path}',
                                name=name,
                                group_id=group_id)
        print(path, download['video_id'])

import_video()




