#!/bin/bash

# DeepLabV3 Water Mask Segmentation - Quick Start Script

echo "🌊 DeepLabV3 Water Mask Segmentation - Setup"
echo "============================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "❌ pip is not installed. Please install pip first."
    exit 1
fi

echo "✅ pip found"

# Install requirements
echo "📦 Installing requirements..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Requirements installed successfully!"
else
    echo "❌ Failed to install requirements"
    exit 1
fi

echo ""
echo "🚀 Setup complete! You can now:"
echo ""
echo "1. Run the Streamlit web app:"
echo "   streamlit run app.py"
echo ""
echo "2. Open the Jupyter notebook:"
echo "   jupyter notebook interactive_notebook.ipynb"
echo ""
echo "3. Or explore the sample images in the sample_images/ directory"
echo ""
echo "📚 For more information, see README.md"