from pathlib import Path
from dataclasses import dataclass 


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path 
    source_url: str
    local_data_file: Path
    unzip_dir: Path 

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    unzip_data: Path
    STATUS_FILE: str
    all_schema: dict
    