#!/bin/bash

# Build script for Project Creator Light macOS app

echo "🚀 Building Project Creator Light macOS app..."

# Create icon
echo "🎨 Creating app icon..."
python3 create_icon.py

# Build the light app
echo "🔨 Building light app with PyInstaller..."
python3 -m PyInstaller ProjectCreatorLight.spec

# Check if build was successful
if [ -d "dist/ProjectCreatorLight.app" ]; then
    echo "✅ Light app built successfully!"
    echo "📱 App location: dist/ProjectCreatorLight.app"
    
    # Show size comparison
    echo ""
    echo "📊 Size comparison:"
    if [ -d "dist/ProjectCreator.app" ]; then
        ORIGINAL_SIZE=$(du -sh dist/ProjectCreator.app | cut -f1)
        LIGHT_SIZE=$(du -sh dist/ProjectCreatorLight.app | cut -f1)
        echo "Original app: $ORIGINAL_SIZE"
        echo "Light app: $LIGHT_SIZE"
    else
        LIGHT_SIZE=$(du -sh dist/ProjectCreatorLight.app | cut -f1)
        echo "Light app: $LIGHT_SIZE"
    fi
    
    echo ""
    echo "To install on Desktop:"
    echo "cp -r dist/ProjectCreatorLight.app ~/Desktop/"
    echo ""
    echo "To run the app:"
    echo "open dist/ProjectCreatorLight.app"
else
    echo "❌ Build failed!"
    exit 1
fi
