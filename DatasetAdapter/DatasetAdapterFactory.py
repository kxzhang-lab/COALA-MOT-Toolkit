from .DynUAVAdapter import DynUAVAdapter
from .UAVDTAdapter import UAVDTAdapter
from .VisDroneAdapter import VisDroneAdapter
from .BaseAdapter import DatasetAdapter

class DatasetAdapterFactory:
    """数据集适配器工厂，根据数据集名称返回对应的适配器实例"""
    
    _adapters = {
        'VisDrone': VisDroneAdapter,
        'UAVDT': UAVDTAdapter,
        'DynUAV': DynUAVAdapter,
        # 可以继续添加新的数据集
    }
    
    @classmethod
    def get_adapter(cls, dataset_name: str) -> DatasetAdapter:
        adapter_class = cls._adapters.get(dataset_name)
        if adapter_class is None:
            raise ValueError(f"不支持的数据集: {dataset_name}")
        return adapter_class()