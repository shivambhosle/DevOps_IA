# pyrefly: ignore [missing-import]
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Application version - increment this (e.g., 1.0 -> 1.1) to demonstrate pipeline updates
APP_VERSION = "1.1"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps CI/CD Demo</title>
    <style>
        :root {
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --accent-green: #10b981;
            --accent-blue: #38bdf8;
            --border-color: #334155;
        }
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }
        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 40px;
            max-width: 600px;
            width: 100%;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.4), 0 10px 10px -5px rgba(0, 0, 0, 0.3);
            text-align: center;
        }
        .status-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background-color: rgba(16, 185, 129, 0.15);
            color: var(--accent-green);
            padding: 6px 16px;
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 600;
            margin-bottom: 24px;
            border: 1px solid rgba(16, 185, 129, 0.3);
        }
        .status-dot {
            width: 8px;
            height: 8px;
            background-color: var(--accent-green);
            border-radius: 50%;
            box-shadow: 0 0 10px var(--accent-green);
        }
        h1 {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 12px;
            color: var(--text-main);
        }
        p.desc {
            color: var(--text-muted);
            font-size: 1.1rem;
            line-height: 1.6;
            margin-bottom: 28px;
        }
        .version-box {
            background-color: rgba(56, 189, 248, 0.08);
            border: 1px solid rgba(56, 189, 248, 0.25);
            border-radius: 10px;
            padding: 16px;
            margin-bottom: 28px;
        }
        .version-label {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--accent-blue);
            margin-bottom: 4px;
        }
        .version-value {
            font-size: 1.75rem;
            font-weight: bold;
            color: #ffffff;
        }
        .pipeline-steps {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid var(--border-color);
        }
        .step {
            font-size: 0.78rem;
            color: var(--text-muted);
            background: #0f172a;
            padding: 10px 6px;
            border-radius: 8px;
            border: 1px solid var(--border-color);
        }
        .step strong {
            display: block;
            color: #e2e8f0;
            margin-bottom: 2px;
        }
        .health-link {
            display: inline-block;
            margin-top: 24px;
            color: var(--accent-blue);
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 500;
        }
        .health-link:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="status-badge">
            <span class="status-dot"></span>
            Pipeline Active & Healthy
        </div>
        <h1>CI/CD Pipeline Successful!</h1>
        <p class="desc">
            This application was automatically built, tested, and deployed using <strong>Jenkins</strong> and <strong>Docker</strong>.
        </p>
        <div class="version-box">
            <div class="version-label">Current Release Version</div>
            <div class="version-value">v{{ version }}</div>
        </div>
        <div class="pipeline-steps">
            <div class="step">
                <strong>1. SCM</strong>
                GitHub
            </div>
            <div class="step">
                <strong>2. CI Server</strong>
                Jenkins
            </div>
            <div class="step">
                <strong>3. Testing</strong>
                Pytest
            </div>
            <div class="step">
                <strong>4. Runtime</strong>
                Docker
            </div>
        </div>
        <a href="/health" class="health-link" target="_blank">View /health JSON Endpoint &rarr;</a>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    """Homepage showing deployment status and application version."""
    return render_template_string(HTML_TEMPLATE, version=APP_VERSION), 200

@app.route("/health")
def health():
    """Healthcheck endpoint returning JSON status with HTTP 200."""
    return jsonify({
        "status": "healthy",
        "version": APP_VERSION,
        "service": "jenkins-docker-demo"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
