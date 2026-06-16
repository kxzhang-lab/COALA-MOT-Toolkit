#### introduction
**COALA-MOT-Toolkit** is a modular annotation and dataset unification framework for UAV-based Multi-Object Tracking (MOT) with language-conditioned grounding support.

It provides a unified interface for heterogeneous aerial tracking datasets (e.g., UAVDT, VisDrone, DynUAV, and custom datasets), enabling consistent annotation, visualization, and language-based trajectory querying through a dataset adapter architecture.

The system is built around an interactive annotation tool (COALA Stage-2 from [AerialMind](https://github.com/shawnliang420/AerialMind/blob/main/Annotation%20/COALA(Stage2).md)) and a canonical data representation layer that decouples dataset-specific formats from downstream annotation and grounding workflows.

#### Key Features
* **Multi-dataset support via adapter layer**
  Unified handling of UAVDT / VisDrone / custom UAV datasets
* **Interactive MOT annotation tool (COALA Stage-2)**
  Language-guided trajectory selection and visualization
* **Canonical data representation**
  Standardized bbox, frame indexing, and trajectory formats
* **Extensible architecture**
  Easy integration of new UAV datasets and annotation pipelines
* **Designed for language-conditional MOT research**
  Supports referring expression-based trajectory selection workflows

#### Goal
This toolkit aims to bridge the gap between:
* heterogeneous UAV tracking datasets
* interactive annotation systems
* emerging language-conditioned MOT research

by providing a scalable and unified annotation infrastructure.

#### Current Modules
* COALA_Stage2/ — interactive annotation GUI and core logic
* datasets/ — dataset-specific adapters (UAVDT, VisDrone, DynUAV, etc.)

#### Status
This project is under active development and will be continuously extended to support additional aerial tracking datasets and language-grounded annotation workflows.