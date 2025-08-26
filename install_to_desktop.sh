#!/bin/bash

# Install Project Creator app to Desktop

echo "📱 Installing Project Creator to Desktop..."

# Check if app exists
if [ ! -d "dist/ProjectCreator.app" ]; then
    echo "❌ App not found! Please run build_app.sh first."
    exit 1
fi

# Copy to Desktop
cp -r dist/ProjectCreator.app ~/Desktop/

echo "✅ Project Creator installed to Desktop!"
echo "🚀 You can now double-click the app icon to launch it."
echo ""
echo "To remove from Desktop:"
echo "rm -rf ~/Desktop/ProjectCreator.app"
