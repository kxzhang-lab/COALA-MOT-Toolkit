from typing import List, Dict
from pathlib import Path
from .BaseAdapter import DatasetAdapter

class DynUAVAdapter(DatasetAdapter):
    """DynUAV的数据集适配器"""

    def parse_annotation_line(self, data:List[str]) -> Dict:
        return {
            'frame_idx': int(data[0]),
            'track_id': int(data[1]),
            'bbox': [float(data[2]), float(data[3]), float(data[4]), float(data[5])],
            'score': int(data[6]),
            'category': int(data[7]) if len(data) > 7 else 0,
            'truncation': float(data[8]) if len(data) > 8 else 0,
            'occlusion': int(data[9]) if len(data) > 9 else 0
        }
    
    def get_frame_offset(self):
        """获取图像序号相对标注帧号的偏移"""
        return -1
    
    def get_video_name_from_path(self, video_path:str) -> str:
        """通过图像序列所处文件夹的绝对路径获取视频名称
        Params: 
          video_path: 图像序列所处文件夹的绝对路径
        return:
          video_name: 视频的名称
        """
        video_name = Path(video_path).parts[-2]
        return video_name