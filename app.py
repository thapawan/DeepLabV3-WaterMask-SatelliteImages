import streamlit as st
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import io
import base64

def load_css():
    """Load custom CSS for better styling"""
    st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

def mock_water_segmentation(image):
    """
    Mock water segmentation function using basic image processing.
    This should be replaced with actual DeepLabV3 model inference.
    """
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Use Otsu's thresholding to create a binary mask
    # This is a simple approximation - replace with actual model
    _, binary_mask = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Create a colored mask (blue for water areas)
    colored_mask = np.zeros_like(image)
    colored_mask[binary_mask == 0] = [0, 100, 255]  # Blue for "water"
    
    # Create overlay
    overlay = cv2.addWeighted(image, 0.7, colored_mask, 0.3, 0)
    
    return binary_mask, colored_mask, overlay

def get_download_link(img_array, filename):
    """Generate download link for images"""
    img = Image.fromarray(img_array)
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    
    b64 = base64.b64encode(buffer.getvalue()).decode()
    href = f'<a href="data:image/png;base64,{b64}" download="{filename}">📥 Download {filename}</a>'
    return href

def main():
    # Page configuration
    st.set_page_config(
        page_title="DeepLabV3 Water Mask Segmentation",
        page_icon="🌊",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    load_css()
    
    # Main header
    st.markdown('<h1 class="main-header">🌊 DeepLabV3 Water Mask Segmentation</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #7f8c8d;">Interactive Water Body Extraction from Satellite Images</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 🛠️ Configuration")
        
        # Model selection (placeholder)
        model_type = st.selectbox(
            "Model Type",
            ["DeepLabV3-ResNet50", "DeepLabV3-ResNet101", "Mock Model (Demo)"],
            index=2
        )
        
        # Confidence threshold
        confidence_threshold = st.slider(
            "Confidence Threshold",
            min_value=0.1,
            max_value=1.0,
            value=0.5,
            step=0.1
        )
        
        # Image preprocessing options
        st.markdown("### 🔧 Preprocessing")
        resize_image = st.checkbox("Resize Image", value=True)
        if resize_image:
            image_size = st.slider("Image Size", 256, 1024, 512, 32)
        
        apply_clahe = st.checkbox("Apply CLAHE Enhancement", value=False)
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<h2 class="sub-header">📤 Input Image</h2>', unsafe_allow_html=True)
        
        # File uploader
        uploaded_file = st.file_uploader(
            "Choose a satellite image...",
            type=['png', 'jpg', 'jpeg', 'tiff', 'tif'],
            help="Upload a satellite image for water body segmentation"
        )
        
        if uploaded_file is not None:
            # Display uploaded image
            image = Image.open(uploaded_file)
            image_array = np.array(image)
            
            # Resize if needed
            if resize_image and image.size != (image_size, image_size):
                image = image.resize((image_size, image_size))
                image_array = np.array(image)
            
            st.image(image, caption="Uploaded Satellite Image", use_container_width=True)
            
            # Image info
            st.markdown(f"""
            <div class="info-box">
                <strong>Image Information:</strong><br>
                📏 Dimensions: {image_array.shape[1]} × {image_array.shape[0]}<br>
                🎨 Channels: {image_array.shape[2] if len(image_array.shape) == 3 else 1}<br>
                📊 Data Type: {image_array.dtype}
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<h2 class="sub-header">🎯 Segmentation Results</h2>', unsafe_allow_html=True)
        
        if uploaded_file is not None:
            # Process button
            if st.button("🚀 Run Water Segmentation", type="primary"):
                with st.spinner("Processing image... This may take a moment."):
                    # Convert PIL to cv2 format
                    if image_array.shape[2] == 4:  # RGBA
                        image_array = cv2.cvtColor(image_array, cv2.COLOR_RGBA2RGB)
                    
                    # Apply preprocessing if selected
                    processed_image = image_array.copy()
                    if apply_clahe:
                        lab = cv2.cvtColor(processed_image, cv2.COLOR_RGB2LAB)
                        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
                        lab[:,:,0] = clahe.apply(lab[:,:,0])
                        processed_image = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
                    
                    # Run segmentation (mock function)
                    binary_mask, colored_mask, overlay = mock_water_segmentation(processed_image)
                    
                    # Display results in tabs
                    tab1, tab2, tab3 = st.tabs(["🎨 Overlay", "🗺️ Mask", "📊 Binary"])
                    
                    with tab1:
                        st.image(overlay, caption="Water Segmentation Overlay", use_container_width=True)
                        st.markdown(get_download_link(overlay, "water_overlay.png"), unsafe_allow_html=True)
                    
                    with tab2:
                        st.image(colored_mask, caption="Colored Water Mask", use_container_width=True)
                        st.markdown(get_download_link(colored_mask, "water_mask.png"), unsafe_allow_html=True)
                    
                    with tab3:
                        st.image(binary_mask, caption="Binary Water Mask", use_container_width=True, channels="GRAY")
                        st.markdown(get_download_link(binary_mask, "binary_mask.png"), unsafe_allow_html=True)
                    
                    # Statistics
                    water_pixels = np.sum(binary_mask == 0)
                    total_pixels = binary_mask.size
                    water_percentage = (water_pixels / total_pixels) * 100
                    
                    st.markdown(f"""
                    <div class="info-box">
                        <strong>Segmentation Statistics:</strong><br>
                        💧 Water Area: {water_percentage:.2f}% of image<br>
                        📊 Water Pixels: {water_pixels:,}<br>
                        🔢 Total Pixels: {total_pixels:,}
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("👆 Please upload an image to see segmentation results")
    
    # Information section
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🎯 About This Tool
        This interactive tool demonstrates water body segmentation from satellite imagery using DeepLabV3 architecture. 
        Upload your satellite images to extract water masks automatically.
        """)
    
    with col2:
        st.markdown("""
        ### 🔧 Features
        - 📤 Easy image upload interface
        - 🎨 Multiple visualization options
        - 📊 Detailed segmentation statistics
        - 💾 Downloadable results
        - ⚙️ Configurable parameters
        """)
    
    with col3:
        st.markdown("""
        ### 🚀 Getting Started
        1. Upload a satellite image
        2. Adjust parameters in sidebar
        3. Click "Run Water Segmentation"
        4. View and download results
        5. Experiment with different settings
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #7f8c8d;">
        🌊 DeepLabV3 Water Mask Segmentation Tool | Built with Streamlit
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()