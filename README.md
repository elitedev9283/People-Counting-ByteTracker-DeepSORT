# Tracking People Counting with YoloV8 + Both ByteTrack and DeepSORT

Yolov8 object detection + deep sort | byte tracking

- Use DeepSORT 💚 when you need robust tracking in crowded environments and occlusions (e.g., pedestrian tracking in surveillance).

- Use ByteTrack 💙 when you need real-time tracking and fast performance (e.g., autonomous vehicles, sports analytics, drone tracking).

Table added 2025/03/29

| Feature               | DeepSORT        | ByteTrack      |
|----------------------|----------------|---------------|
| **Uses Deep Learning (ReID)** | ✅ Yes | ❌ No |
| **Tracking Approach** | Appearance + Motion | Motion Only |
| **Works Well in Crowded Scenes** | ✅ Yes | ❌ No |
| **Speed** | 🐢 Slower (due to ReID) | ⚡ Faster (lightweight) |
| **Handles Occlusion** | ✅ Better | ❌ Weaker |
| **Computation Cost** | High (requires feature extraction) | Low (IoU-based) |
| **Best Use Case** | Crowded scenes, re-identification | Real-time applications |


## Download Deep SORT Model

We are working from [here](https://github.com/computervisiondeveloper/deep_sort) from deep sort official implementation.

You can download deep SORT model [here](https://drive.google.com/open?id=18fKzfqnqhqW3s9zwsCbnVJ5XF2JFeqMp).