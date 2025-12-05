#!/bin/bash

echo "🔧 Setting up automation environment..."

python3 -m venv env
source env/bin/activate

echo "📦 Installing dependencies..."
pip install -r env_setup/requirements.txt

echo "✨ Setup complete!"
echo "To activate your environment later, run: source env/bin/activate"
