from caption import enhance_caption

def test_enhance_caption():
    caption = "Excited to share my new project with everyone! Stay tuned for updates."
    sample_caption = caption
    print("Original:", sample_caption)
    print("\nEnhanced:")
    enhanced = enhance_caption(sample_caption)
    print(enhanced)

    print("\nEnhanced (Upscale):")
    enhanced_upscale = enhance_caption(sample_caption, upscale=True)
    print(enhanced_upscale)

if __name__ == "__main__":
    test_enhance_caption()
