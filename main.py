import requests
import json

# marketplace base item url to pass to Downloader Service
marketplaceBaseURL = "https://marketplace.visualstudio.com/items?itemName="

extensionQueryURL = "https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery"

# use VS Code Offline Extension Downloader Service
downloadURL = "https://vscode-offline.herokuapp.com/api/extract"

HEADERS = {
    "Accept": "application/json;api-version=5.0-preview.1;excludeUrls=true",
    "Content-Type": "application/json"
}

PARAMS = {
    "assetTypes": [
        "Microsoft.VisualStudio.Services.Icons.Default",
        "Microsoft.VisualStudio.Services.Icons.Branding",
        "Microsoft.VisualStudio.Services.Icons.Small"
    ],
    "filters": [
        {
            "criteria": [
                {
                    "filterType": 8,
                    "value": "Microsoft.VisualStudio.Code"
                },
                {
                    "filterType": 10,
                    "value": "target:\"Microsoft.VisualStudio.Code\" "
                },
                {
                    "filterType": 12,
                    "value": "37888"
                }
            ],
            "direction": 2,
            "pageSize": 54,
            "pageNumber": 2,
            "sortBy": 4,
            "sortOrder": 0
        }
    ],
    "flags": 870,
    "extensionQuery": "All"
}

r = requests.post(url=extensionQueryURL, headers=HEADERS, data=PARAMS)

print(r.text)

# with open('vsmarketplace-2018.json') as data_file:
#     data = json.load(data_file)
# print(len(data["results"][0]["extensions"]))
