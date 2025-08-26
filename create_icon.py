#!/usr/bin/env python3
"""
Create a simple icon for the Project Creator app
"""
from PIL import Image, ImageDraw, ImageFont
import os

def create_icon():
    """Create a simple icon"""
    # Create a 512x512 image with a blue background
    size = 512
    img = Image.new('RGBA', (size, size), (52, 152, 219, 255))
    draw = ImageDraw.Draw(img)
    
    # Draw a rocket emoji or simple shape
    # For now, let's draw a simple rocket shape
    rocket_color = (255, 255, 255, 255)
    
    # Rocket body (rectangle)
    body_width = size // 3
    body_height = size // 2
    body_x = (size - body_width) // 2
    body_y = size // 4
    draw.rectangle([body_x, body_y, body_x + body_width, body_y + body_height], 
                  fill=rocket_color)
    
    # Rocket tip (triangle)
    tip_points = [
        (body_x + body_width // 2, body_y - size // 8),
        (body_x - size // 16, body_y + size // 8),
        (body_x + body_width + size // 16, body_y + size // 8)
    ]
    draw.polygon(tip_points, fill=rocket_color)
    
    # Rocket fins
    fin_color = (231, 76, 60, 255)
    fin_width = size // 8
    fin_height = size // 6
    
    # Left fin
    draw.rectangle([body_x - fin_width, body_y + body_height - fin_height, 
                   body_x, body_y + body_height], fill=fin_color)
    
    # Right fin
    draw.rectangle([body_x + body_width, body_y + body_height - fin_height, 
                   body_x + body_width + fin_width, body_y + body_height], fill=fin_color)
    
    # Save as PNG
    img.save('icon.png')
    print("✅ Icon created: icon.png")
    
    # Convert to ICNS for macOS (requires iconutil)
    try:
        # Create iconset directory
        os.makedirs('icon.iconset', exist_ok=True)
        
        # Generate different sizes
        sizes = [16, 32, 64, 128, 256, 512]
        for s in sizes:
            resized = img.resize((s, s), Image.Resampling.LANCZOS)
            resized.save(f'icon.iconset/icon_{s}x{s}.png')
            if s != 512:  # Also create @2x versions
                resized.save(f'icon.iconset/icon_{s//2}x{s//2}@2x.png')
        
        # Convert to ICNS
        os.system('iconutil -c icns icon.iconset')
        print("✅ Icon converted to ICNS: icon.icns")
        
        # Clean up
        import shutil
        shutil.rmtree('icon.iconset')
        os.remove('icon.png')
        
    except Exception as e:
        print(f"⚠️  Could not create ICNS: {e}")
        print("Using PNG icon instead")

if __name__ == "__main__":
    create_icon()
