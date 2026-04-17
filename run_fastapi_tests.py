from pathlib import Path
import subprocess

root = Path(__file__).resolve().parent
req_path = root / "requirements.txt"
required = ["fastapi", "pytest", "httpx"]

if req_path.exists():
    content = req_path.read_text().splitlines()
    packages = {line.strip() for line in content if line.strip()}
else:
    packages = set()

for pkg in required:
    packages.add(pkg)

req_path.write_text("\n".join(sorted(packages)) + "\n")
print(f"Updated {req_path} with {required}")

subprocess.run(["python3", "-m", "pip", "install", *required], check=True)
subprocess.run(["pytest", "-q"], cwd=root, check=True)
