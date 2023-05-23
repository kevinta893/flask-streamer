# Flask Streamer

Streams a webcam to a webpage.

## Setup

Install Python dependencies:

```bash
cd server
pip install -r requirements.txt
```

Install Node dependencies:

```bash
cd web-ui
npm install
```

## Running the project

Start the webcam server

```bash
cd server
flask --app server run
```

Start the web server (development)

```bash
cd web-ui
npm run dev
```

Visit http://localhost:5100 for main website
