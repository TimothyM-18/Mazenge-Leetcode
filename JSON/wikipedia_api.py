import requests

def get_image_sizes(page_title):
    url = "https://en.wikipedia.org/w/api.php"

    # Step 1: Get page info and images
    params = {
        "action": "query",
        "format": "json",
        "titles": page_title,
        "prop": "images",
        "imlimit": "max",
        "redirects": 1  # follow redirects automatically
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, ValueError):
        print("Failed to get page images. Check your internet or page title!")
        return

    pages = data.get("query", {}).get("pages", {})
    if not pages:
        print("No pages found. Check your page title!")
        return

    sizes = {}

    # Step 2: Loop through images
    for page in pages.values():
        images = page.get("images", [])
        if not images:
            print(f"No images found on page '{page.get('title', page_title)}'.")
            continue

        for img in images:
            img_title = img.get("title")
            if not img_title:
                continue

            img_params = {
                "action": "query",
                "format": "json",
                "titles": img_title,
                "prop": "imageinfo",
                "iiprop": "size"
            }

            try:
                img_response = requests.get(url, params=img_params, timeout=10)
                img_response.raise_for_status()
                if not img_response.text.strip():
                    continue
                img_data = img_response.json()
            except (requests.RequestException, ValueError):
                continue

            page_info = next(iter(img_data.get("query", {}).get("pages", {}).values()), {})
            imageinfo = page_info.get("imageinfo", [{}])[0]
            width = imageinfo.get("width")
            height = imageinfo.get("height")

            if width and height:
                sizes[img_title] = (width, height)

    # Step 3: Print results
    if not sizes:
        print("No image sizes found.")
        return

    print(f"\nImage sizes for page: {page_title}\n")
    for title, (w, h) in sizes.items():
        print(f"{title}: {w}x{h}")


# Run script
page_title = input("Enter Wikipedia page title: ").strip()
get_image_sizes(page_title)
