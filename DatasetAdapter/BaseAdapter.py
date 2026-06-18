from abc import ABC, abstractmethod
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple

class DatasetAdapter(ABC):
    """ 数据集适配器的基类，定义了所有需要适配的接口 """
    @abstractmethod
    def parse_annotation_line(self, data : List[str]) -> Dict:
        """解析标注文件的每一行，返回标准化字典。
        Params:
          data: 从文件读取并分割后得到的字符串列表
        return:{
            'frame_idx': int,
            'track_id': int,
            'bbox': [x, y, w, h],
            'score': int,
            'category': int,
            'truncation': int,
            'occlusion': int
        }
        """
        pass

    @abstractmethod
    def get_frame_offset(self) -> int:
        """返回标注帧号和图形帧号的偏移量
        例如：DynUAV 标注从1开始，图像从0开始，偏移量为 -1
        """
        pass

    @abstractmethod
    def get_video_name_from_path(self, video_path:str) -> str:
        """通过图像序列所处文件夹的绝对路径获取视频名称
        Params: 
          video_path: 图像序列所处文件夹的绝对路径
        return:
          video_name: 视频的名称
        """
        pass