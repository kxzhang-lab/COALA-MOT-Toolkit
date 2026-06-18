import os
from typing import List, Dict
from .BaseAdapter import DatasetAdapter

class VisDroneAdapter(DatasetAdapter):
    """VisDrone的数据集适配器"""

    def parse_annotation_line(self, data:List[str]) -> Dict:
        return {
            'frame_idx': int(data[0]),
            'track_id': int(data[1]),
            'bbox': [int(data[2]), int(data[3]), int(data[4]), int(data[5])],
            'score': int(data[6]),
            'category': int(data[7]) if len(data) > 7 else 0,
            'truncation': int(data[8]) if len(data) > 8 else 0,
            'occlusion': int(data[9]) if len(data) > 9 else 0
        }
    
    def get_frame_offset(self):
        return 0
    
    def get_video_name_from_path(self, video_path:str) -> str:
        """通过图像序列所处文件夹的绝对路径获取视频名称
        Params: 
          video_path: 图像序列所处文件夹的绝对路径
        return:
          video_name: 视频的名称
        """
        video_name = os.path.basename(video_path)
        return video_name