import uuid
from dataclasses import field
from datetime import datetime
from marshmallow_dataclass import dataclass as mm_dataclass
from typing import Optional
from dataclasses_json import dataclass_json, Undefined
@dataclass_json(undefined=Undefined.EXCLUDE)
@mm_dataclass(frozen=True)



class SensorModel:
    #Variabel wajib dikirim ke server
    kecepatan: float #0.001
    latitude: float
    longitude: float
    
    #Autogenerate by Database
    timestamp: datetime = field(metadata={ #add timestamp
        'dataclasses_json': {
            'encoder': lambda x: datetime.timestamp(x),
        }
    }, default_factory=datetime.utcnow)
    idtransaksi: str = field(default_factory=lambda: str(uuid.uuid4())[:8]) # Generate id
