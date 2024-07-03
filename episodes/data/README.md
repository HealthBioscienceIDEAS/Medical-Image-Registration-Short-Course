# Medical Data Imaging 

## CT-vs-PET-Ventilation-Imaging
CT Ventilation as a Functional Imaging Modality for Lung Cancer Radiotherapy from [TCIA](https://www.cancerimagingarchive.net/collection/ct-vs-pet-ventilation-imaging/).
We recomend to focus on exhale/inhale breath hold CT (BHCT) Dicoms which belog to: 
* The BHCT scans for CT-PET-VI-02 & CT-PET-VI-03 show very little motion between inhale and exhale
* The BHCT scans for CT-PET-VI-05 have a different number of slices between the inhale and exhale

Data paths look like these:
```
/CT-PET-VI-02$ tree -d
.
├── 1000.000000-PET SUV Factors-26496 [1 item, with size 42.1 kB]
├── 3.000000-CT Lung  3.0  B31f-61322  [175 items, totalling 92.4 MB]
├── 4.000000-Galligas Lung-03537 [159 items, totalling 51.5 MB]
├── 5.000000-Thorax Insp  2.0  B70f-29873 [167 items, totalling 88.1 MB]
├── 7.000000-Thorax Exp  2.0  B70f-73355 [167 items, totalling 88.1 MB]
└── 8.000000-RespLow  2.0  B30s  80  Ex - 100  In-44317 [810 items, totalling 426.9 MB]

/CT-PET-VI-03$ tree -d
.
├── 06-25-1996-RTRTRespLowBreathRateRNS Adult-43080
│   ├── 1000.000000-PET SUV Factors-06580
│   ├── 3.000000-CT Lung  3.0  B31f-08354
│   └── 4.000000-Galligas Lung-15379
└── 06-25-1996-RTRTRespLowBreathRateRNS Adult-87093
    ├── 5.000000-Thorax Insp  2.0  B70f-42000
    ├── 7.000000-Thorax Exp  2.0  B70f-45310
    └── 8.000000-RespLow  2.0  B30s  80  Ex - 100  In-54790

/CT-PET-VI-05$ tree -d
└── 12-10-1996-RTRTRespLowBreathRateRNS Adult-37585
    ├── 1000.000000-PET SUV Factors-63910
    ├── 3.000000-CT Lung  3.0  B31f-90638
    ├── 4.000000-Galligas Lung-26361
    ├── 5.000000-Thorax Insp  2.0  B70f-45546
    ├── 7.000000-Thorax Exp  2.0  B70f-31579
    └── 8.000000-RespLow  2.0  B30s  80  Ex - 100  In-16454
```


### Citations & Data Usage Policy
Data Citation Required: Users must abide by [the TCIA Data Usage Policy and Restrictions](https://www.cancerimagingarchive.net/data-usage-policies-and-restrictions/). 
Attribution must include the following citation, including the Digital Object Identifier:
> Eslick, E. M., Kipritidis, J., Gradinscak, D., Stevens, M. J., Bailey, D. L., Harris, B., Booth, J. T., & Keall, P. J. (2022). CT Ventilation as a functional imaging modality for lung cancer radiotherapy (CT-vs-PET-Ventilation-Imaging) (Version 1) [Data set]. The Cancer Imaging Archive. https://doi.org/10.7937/3ppx-7s22

### Data is converted from DICOM to nifti using `dicom2nifti`:
```
from pathlib import Path 
import dicom2nifti 
dicoms = Path("~/3_000000-CT_Lung_30_B31f-61322")
dicom2nifti.convert_directory(dicoms, ".", compression=True, reorient=True)
```


## Demons Image Registration Exercise Data

Please check [`data`](https://github.com/HealthBioscienceIDEAS/Medical-Image-Registration-Short-Course/tree/main/episodes/data) folder inside `episodes` for accessing `cine_MR_img_1.png`, `cine_MR_img_2.png`, and `cine_MR_img_3.png` that are used for [`demonReg.py`](https://github.com/HealthBioscienceIDEAS/Medical-Image-Registration-Short-Course/blob/main/src/mirc/utils/demonsReg.py) and [`exampleSolution3.py`](https://github.com/HealthBioscienceIDEAS/Medical-Image-Registration-Short-Course/blob/main/src/mirc/examples/exampleSolution3.py).

