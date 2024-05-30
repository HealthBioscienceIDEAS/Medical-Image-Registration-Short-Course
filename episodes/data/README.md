# Demo data

## Data is converted using:
```
from pathlib import Path 
import dicom2nifti 
dicoms = Path("~/3_000000-CT_Lung_30_B31f-61322")
dicom2nifti.convert_directory(dicoms, ".", compression=True, reorient=True)
```


