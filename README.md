# 🎬 YTubeConverter

**YTubeConverter** is a web-based YouTube video converter that allows users to download and convert YouTube videos into a wide range of formats. Built with **Python Flask** and **JavaScript** on the backend, and styled using **HTML/CSS** on the frontend, this project offers a simple and responsive interface for fast and flexible conversions.

---

## 🚀 Features

- 🎧 Convert to high-quality **audio** formats like MP3, FLAC, WAV, AAC, OPUS, OGG
- 🎥 Download videos in formats such as MP4, WEBM, MKV, AVI
- 🧠 Metadata embedding and thumbnail support
- ⚙️ Backend powered by `yt-dlp` and `ffmpeg`
- 🌐 User-friendly web interface
- 🔧 Configurable for more formats if needed

---

## 🧩 Dependencies

- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) – A fast and powerful YouTube video downloader and converter
- [`ffmpeg-python`](https://github.com/kkroening/ffmpeg-python) – Pythonic wrapper for FFmpeg to handle media conversion and processing
- `Flask` – Lightweight Python web framework
---

## 🛠️ Technologies Used

**Backend:**
- Python
- Flask
- JavaScript (for async handling)

**Frontend:**
- HTML
- CSS

---

## 💾 Supported Formats

| Format | Type  | Notes                          |
|--------|-------|--------------------------------|
| MP3    | Audio | 320kbps, thumbnail + metadata  |
| FLAC   | Audio | Lossless                       |
| WAV    | Audio | High quality                   |
| AAC    | Audio | Compressed format              |
| OPUS   | Audio | Low-latency, high-quality      |
| OGG    | Audio | Vorbis codec                   |
| MP4    | Video | Best quality + thumbnail       |
| WEBM   | Video | Modern web-compatible          |
| MKV    | Video | High compatibility             |
| AVI    | Video | Legacy support                 |

---

## ⚙️ How It Works

- The user enters a YouTube URL
- Selects the desired output format
- The backend fetches and processes the video using `yt-dlp` and `ffmpeg`
- The file is returned for download

---

## 🧪 Setup & Run Locally

1. **Clone the repo:**
   ```bash
   git clone https://github.com/x6h057/YTubeConverter.git
   cd YTubeConverter
   python3 -m venv .venv
   source .venv/bin/activate
   flask run --host=0.0.0.0 --port=8080
