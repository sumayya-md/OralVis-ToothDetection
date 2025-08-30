# 🦷 OralVis Tooth Detection using YOLO

This repository contains my submission for the **OralVis AI Research Intern Task**.  
The project involves training a YOLO-based model to detect and classify teeth using the **FDI numbering system**.

---

## 📂 Dataset
- Dataset: ~500 dental panoramic images with YOLO-format labels.  
- Each image has bounding boxes for teeth using the **FDI numbering system** (32 classes).  
- Data was split into:
  - Train: 80%
  - Validation: 10%
  - Test: 10%  



## ⚙️ Setup

Clone the repo and install dependencies:

```bash
git clone https://github.com/<your-username>/OralVis-ToothDetection.git
cd OralVis-ToothDetection
pip install -r requirements.txt
🚀 Training
Model trained using YOLO (v5/v8/v11) with pretrained weights (yolov8s.pt), input size 640x640.

bash
Copy code
yolo detect train data=data.yaml model=yolov8s.pt imgsz=640 epochs=100
📊 Results
Metric	Value
Precision:	0.20277
Recall:	0.45656
mAP@50:	1.18766
mAP@50-95:	1.11874
 predictions are available in /runs/predictions/

📝 Submission
📄 Report: OralVis_Submission_Report.pdf





