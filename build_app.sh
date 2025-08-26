#!/bin/bash

# Build script for Project Creator macOS app

echo "🚀 Building Project Creator macOS app..."

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Create icon
echo "🎨 Creating app icon..."
python3 create_icon.py

# Build the app
echo "🔨 Building app with PyInstaller..."
pyinstaller ProjectCreator.spec

# Check if build was successful
if [ -d "dist/ProjectCreator.app" ]; then
    echo "✅ App built successfully!"
    echo "📱 App location: dist/ProjectCreator.app"
    echo ""
    echo "To install on Desktop:"
    echo "cp -r dist/ProjectCreator.app ~/Desktop/"
    echo ""
    echo "To run the app:"
    echo "open dist/ProjectCreator.app"
else
    echo "❌ Build failed!"
    exit 1
fi
