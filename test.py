try:
    import langchain
    import langchain_community
    import langchain_google_genai
    import dotenv
    print("✓ All packages installed!")
except ImportError as e:
    print(f"✗ Missing: {e}")
