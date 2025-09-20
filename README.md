# 🌊 DeepLabV3-WaterMask-SatelliteImages

**Interactive Water Body Extraction from Satellite Images using DeepLabV3**

Fine-tuned Semantic Segmentation for Water Body Extraction from SAR Imagery, Multi Spectral Satellite Images with interactive demos and tools.

## 🚀 Interactive Features

This repository provides two main interactive components:

### 1. 🎨 Streamlit Web App
An intuitive web interface for water segmentation with real-time visualization.

**Features:**
- 📤 Drag-and-drop image upload
- 🎯 Real-time water segmentation
- 📊 Detailed segmentation statistics
- 🎨 Multiple visualization options (overlay, mask, binary)
- ⚙️ Configurable parameters and preprocessing
- 💾 Downloadable results

### 2. 📓 Jupyter Notebook
A comprehensive interactive notebook for detailed exploration and experimentation.

**Features:**
- 🔧 Complete preprocessing pipeline
- 🧠 Model architecture explanation
- 📊 Interactive parameter tuning
- 📈 Performance comparison tools
- 🖼️ Custom image upload widget
- 📋 Detailed analysis and metrics

## 🛠️ Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/thapawan/DeepLabV3-WaterMask-SatelliteImages.git
cd DeepLabV3-WaterMask-SatelliteImages

# Install requirements
pip install -r requirements.txt
```

### Running the Streamlit App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Running the Jupyter Notebook

```bash
jupyter notebook interactive_notebook.ipynb
```

## 📁 Repository Structure

```
DeepLabV3-WaterMask-SatelliteImages/
├── app.py                     # Streamlit web application
├── interactive_notebook.ipynb # Jupyter notebook for exploration
├── requirements.txt           # Python dependencies
├── sample_images/            # Sample satellite images for testing
│   ├── river_scene.jpg
│   ├── lake_scene.jpg
│   └── coastal_scene.jpg
└── README.md                 # This file
```

## 🎯 Usage Examples

### Web App Usage
1. **Launch the app**: `streamlit run app.py`
2. **Upload an image**: Use the file uploader in the sidebar
3. **Adjust parameters**: Modify preprocessing and model settings
4. **Run segmentation**: Click "Run Water Segmentation"
5. **View results**: Explore different visualization tabs
6. **Download results**: Use the download links for each result type

### Notebook Usage
1. **Open the notebook**: `jupyter notebook interactive_notebook.ipynb`
2. **Run all cells**: Execute cells sequentially to see the demo
3. **Interactive widgets**: Use sliders and controls to experiment
4. **Upload custom images**: Use the file upload widget in the last section
5. **Analyze results**: View detailed statistics and comparisons

## 🔧 Model Architecture

The implementation uses DeepLabV3 with ResNet backbone for semantic segmentation:

- **Backbone**: ResNet-50/ResNet-101
- **Architecture**: DeepLabV3 with Atrous Spatial Pyramid Pooling (ASPP)
- **Output**: Binary segmentation (water vs. non-water)
- **Input Size**: Configurable (default: 512x512)

## 📊 Features & Capabilities

### Image Processing
- ✅ Multiple format support (JPG, PNG, TIFF)
- ✅ Automatic resizing and normalization
- ✅ CLAHE enhancement for low-contrast images
- ✅ Batch processing support (notebook)

### Visualization
- ✅ Original image display
- ✅ Binary water mask
- ✅ Colored overlay visualization
- ✅ Interactive parameter adjustment
- ✅ Statistical analysis

### Analysis Tools
- ✅ Water coverage percentage
- ✅ Connected components analysis
- ✅ Water body counting
- ✅ Performance metrics comparison
- ✅ Method comparison tools

## 🎨 Sample Images

The repository includes sample satellite images for testing:
- **River Scene**: Winding river through landscape
- **Lake Scene**: Large lake with smaller ponds
- **Coastal Scene**: Coastal water with islands

## 🔬 Technical Details

### Dependencies
- **Streamlit**: Web app framework
- **PyTorch**: Deep learning framework
- **OpenCV**: Image processing
- **NumPy/Pandas**: Data manipulation
- **Matplotlib**: Visualization
- **Scikit-image**: Advanced image processing

### Model Integration
The current implementation includes a mock segmentation model for demonstration. To integrate your trained DeepLabV3 model:

1. Replace the `mock_predict()` function in `app.py`
2. Load your trained model weights
3. Update the preprocessing pipeline as needed
4. Adjust the segmentation threshold

### Customization
- **Model Parameters**: Easily configurable in the sidebar
- **Preprocessing**: Toggle CLAHE, resize options, normalization
- **Visualization**: Customizable overlay colors and transparency
- **Output Format**: Multiple download formats available

## 🚀 Getting Started with Your Own Model

1. **Train your DeepLabV3 model** on your satellite imagery dataset
2. **Save the model weights** in PyTorch format
3. **Replace the mock model** in both app.py and the notebook
4. **Update preprocessing** to match your training pipeline
5. **Test with your images** using the interactive tools

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:
- Model improvements
- Additional preprocessing options
- New visualization features
- Bug fixes and optimizations

## 📄 License

This project is open source. Please check the license file for details.

## 🙏 Acknowledgments

- DeepLabV3 architecture by Google Research
- Streamlit for the amazing web app framework
- PyTorch for deep learning capabilities

---

**🌊 Start exploring water body segmentation with our interactive tools!**
