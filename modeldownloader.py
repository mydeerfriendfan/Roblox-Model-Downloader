import webbrowser

def open_url_with_prompt(base_url):
    prompt = input("Enter roblox model ID here: ")
    full_url = f"{base_url}{prompt}"
    webbrowser.open(full_url)

# Example usage
base_url = "https://assetdelivery.roblox.com/v1/asset/?id="
open_url_with_prompt(base_url)
print("Model download link opened!")