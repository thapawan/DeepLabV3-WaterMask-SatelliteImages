# DeepLabV3-WaterMask-SatelliteImages

This repository contains code and documentation for extracting water masks from Sentinel-1A SAR imagery using DeepLabV3, a state-of-the-art semantic segmentation model. The project leverages a pre-trained Water Body Extraction model provided by Esri and fine-tunes it for specific river systems in the Southeastern U.S.

## 📌 Overview

- **Model**: DeepLabV3 with atrous convolution
- **Imagery**: Sentinel-1A C-band SAR, Sentinel 2A/2B, Landsat
- **Pretrained Source**: Esri Water Body Extraction (SAR) Model, Manual Training Samples
- **Target Rivers**: Sipsey, Coosa, Tennessee, Mississippi, Black Warrior, Cahaba
- **Patch Size**: 256x256 pixels
- **Resolution**: 10 meters, 30 meters

## 🧠 Methodology

1. **Model Architecture**  
   Utilizes atrous convolution to preserve spatial resolution and capture multi-scale context.

2. **Pretrained Model**  
   - Precision: 0.945  
   - Recall: 0.920  
   - F1 Score: 0.933

3. **Fine-Tuning**  
   - 400 manually annotated patches  
   - Data augmentation: rotation, flipping, speckle noise  
   - Optimizer: Adam  
   - Learning rate: 0.0001  
   - Epochs: 150 with early stopping  
   - Validation F1 Score: 0.970

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/DeepLabV3-WaterMask-Sentinel1A.git
cd DeepLabV3-WaterMask-Sentinel1A
pip install -r requirements.txt

# Load model
model = load_pretrained_model()

# Preprocess image
image = preprocess_sentinel1(image_path)

# Predict water mask
mask = model.predict(image)

# Post-process and visualize
visualize_mask(mask)

water maskmask = model.predict(image)# Post-process and visualizevisualize_mask(mask)Show more lines

📁 Data

Sentinel-1A SAR patches (256x256)
Annotated masks for water bodies
Augmented training and validation sets

📚 References

Askevold & Vågen (2022)
Zhang et al. (2024)
Heryadi et al. (2020)
Liu et al. (2024)
Chen et al. (2017)
Esri (2022)

📌 License
MIT License

🙌 Acknowledgments
Thanks to Esri for providing the pretrained model and to the University of Alabama for supporting this research.

