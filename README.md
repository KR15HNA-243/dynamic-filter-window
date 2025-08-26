# 🖼️ Dynamic Filter Window (CV Project)

This project is a **gesture-controlled computer vision tool** that lets users create a free-form filter window using their hands. By forming a rectangle with both hands, users can dynamically select a region of the camera feed where filters (blur, grayscale, edges, etc.) are applied in real-time.  

---

## 🚀 Features
- **Hand Gesture Recognition** – Uses MediaPipe + OpenCV to detect and track hand positions.  
- **Dynamic Region Selection** – Create and adjust a filter window with hand gestures.  
- **Real-Time Filters** – Apply filters like blur, grayscale, and edge detection to only the selected region.  
- **Interactive Controls** – Switch filters seamlessly using keypress (`f`) or gestures.  
- **Original View** – Toggle between original feed and filtered view.  

---

## 🌍 Real-World Applications
- **Privacy** – Blur sensitive areas like faces, license plates, or documents in live video.  
- **Accessibility** – Enhance visuals with high contrast or magnification for visually impaired users.  
- **Education & Presentations** – Highlight important areas during teaching or demos without physical tools.  
- **Entertainment & Media** – Add live interactive AR-style filters for streaming and creative use.  

---

## 🛠️ Tech Stack
- **Python 3.10.9**  
- **OpenCV** – For real-time image processing  
- **MediaPipe** – For robust hand gesture tracking  

---

## 📸 Current Filters 
1. **Grayscale** – Black & white view.  
2. **Blur** – Soft Gaussian blur effect.  
3. **Edges** – Edge detection with Canny filter.  

---

## 📖 Tutorial – How It Works
1. **Start the program**  
   ```bash
   python main.py
2. **Select a region with both hands**
   ```bash
   # Move your hands to create a rectangle
3. **Apply filters**
   ```bash
   # Press 'f' to switch between filters
   # Press 'Esc' to quit the program
```

---