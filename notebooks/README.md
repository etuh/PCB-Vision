# YOLOv8 Object Detection on Custom Dataset

This project demonstrates how to train a YOLOv8 object detection model on a custom dataset using Roboflow and Ultralytics YOLOv8. The tutorial covers everything from environment setup to performing inference with a custom-trained model.

## Features

- **GPU Acceleration Check**: Verify GPU availability for faster training
- **YOLOv8 Installation**: Step-by-step guide to install YOLOv8
- **CLI Basics**: Introduction to YOLOv8 command-line interface
- **Inference with Pre-trained COCO Model**: Perform object detection using a pre-trained YOLOv8 model
- **Roboflow Integration**: Utilize Roboflow for dataset preparation, including creating projects, uploading images, labeling, generating dataset versions, and exporting in YOLOv8 format
- **Custom Training**: Train a YOLOv8s model on a custom dataset
- **Model Validation**: Validate the performance of the custom-trained model
- **Inference with Custom Model**: Run object detection using the custom-trained YOLOv8 model
- **Model Deployment**: Deploy the trained model to Roboflow for scalable inference

## Prerequisites

- Python 3.7+
- GPU with CUDA support (recommended)
- Roboflow account (for custom dataset preparation)
- Google Colab account (if using Colab)

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd yolov8-custom-training
```

### 2. Install Dependencies
```bash
pip install ultralytics roboflow
```

### 3. Verify GPU Availability
```python
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"GPU device: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None'}")
```

## Usage

### Step 1: Basic YOLOv8 Commands
```bash
# Check YOLOv8 installation
yolo checks

# Display help
yolo --help

# Check version
yolo version
```

### Step 2: Inference with Pre-trained COCO Model
```python
from ultralytics import YOLO

# Load pre-trained model
model = YOLO('yolov8n.pt')

# Run inference
results = model('https://ultralytics.com/images/bus.jpg')

# Display results
results[0].show()
```

### Step 3: Prepare Custom Dataset with Roboflow

1. **Create a Roboflow Account** at [roboflow.com](https://roboflow.com)
2. **Create a New Project**:
   - Choose "Object Detection" as project type
   - Upload your images
   - Annotate images using Roboflow Annotate
3. **Generate Dataset Version**:
   - Apply preprocessing (resize, auto-orient)
   - Apply augmentations (flip, rotate, shear)
   - Generate dataset version
4. **Export Dataset** in YOLOv8 format

```python
from roboflow import Roboflow

rf = Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace().project("your-project")
dataset = project.version(1).download("yolov8")
```

### Step 4: Train Custom Model
```bash
# Train YOLOv8s on custom dataset
yolo task=detect mode=train model=yolov8s.pt data=data.yaml epochs=100 imgsz=640
```

### Step 5: Validate Model
```bash
# Validate trained model
yolo task=detect mode=val model=runs/detect/train/weights/best.pt data=data.yaml
```

### Step 6: Inference with Custom Model
```python
# Load custom model
model = YOLO('runs/detect/train/weights/best.pt')

# Run inference
results = model('path/to/test/image.jpg')

# Save results
results[0].save('output.jpg')
```

### Step 7: Deploy Model to Roboflow
1. Upload trained weights to Roboflow Deploy
2. Use Roboflow Inference API for scalable deployment
3. Deploy to edge devices using Roboflow Inference

## Project Structure

```
yolov8-custom-training/
├── data.yaml              # Dataset configuration file
├── train.py              # Training script
├── inference.py          # Inference script
├── requirements.txt      # Python dependencies
├── runs/
│   ├── detect/train/    # Training outputs (weights, logs, plots)
│   ├── detect/val/      # Validation results
│   └── detect/predict/  # Inference results
├── datasets/            # Downloaded datasets
└── README.md           # This file
```

## Output Directories

- **`runs/detect/train/`**: Contains training logs, weights (`best.pt`, `last.pt`), and evaluation plots
- **`runs/detect/val/`**: Contains validation results and metrics
- **`runs/detect/predict/`**: Contains inference results from pre-trained COCO model
- **`runs/detect/predict2/`**: Contains inference results from custom-trained model

## Google Colab Instructions

1. Click the 'Open in Colab' badge (if available)
2. Enable GPU: `Runtime > Change runtime type > Hardware accelerator: GPU`
3. Run cells sequentially
4. Upload your custom dataset or connect to Roboflow

## Key Files

- **`best.pt`**: Best model weights from training
- **`last.pt`**: Last model weights from training
- **`results.png`**: Training results graph
- **`confusion_matrix.png`**: Confusion matrix
- **`val_batch_pred.jpg`**: Validation predictions visualization

## Troubleshooting

1. **CUDA Out of Memory**: Reduce batch size or image size
2. **Dataset Loading Issues**: Verify `data.yaml` format and paths
3. **Poor Results**: Increase epochs, adjust hyperparameters, or improve dataset quality
4. **Roboflow API Errors**: Verify API key and project permissions

## Resources

- [Ultralytics YOLOv8 Documentation](https://docs.ultralytics.com/)
- [Roboflow Documentation](https://docs.roboflow.com/)
- [YOLOv8 GitHub Repository](https://github.com/ultralytics/ultralytics)
- [Roboflow Universe](https://universe.roboflow.com/)

## License

This project is intended for educational and research purposes. Please refer to the Ultralytics and Roboflow licenses for commercial use.

## Acknowledgments

- [Ultralytics](https://ultralytics.com/) for YOLOv8
- [Roboflow](https://roboflow.com/) for dataset management tools
- Google Colab for providing GPU resources
