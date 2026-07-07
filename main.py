import os
from datetime import datetime

import requests
from dotenv import load_dotenv

# ==========================================================
# Load Environment Variables
# ==========================================================
load_dotenv()

# ==========================================================
# Pixela Account Credentials
# ==========================================================
TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")
GRAPH_ID = os.getenv("GRAPH_ID")

# ==========================================================
# Pixela API Endpoint
# ==========================================================
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# ==========================================================
# Create a New Pixela User
# Run this section ONLY ONCE while creating your account.
# ==========================================================
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Uncomment the lines below to create a new user.
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.status_code)
# print(response.text)

# ==========================================================
# Create a New Graph
# Run this section ONLY ONCE after creating the user.
# ==========================================================
# graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai",
# }
#
# # Pixela Authentication Header
headers = {
    "X-USER-TOKEN": TOKEN
}

# # Uncomment the lines below to create a new graph.
# response = requests.post(
#     url=graph_endpoint,
#     json=graph_config,
#     headers=headers
# )
# print(response.text)

# ==========================================================
# Add Today's Cycling Record
# ==========================================================
pixel_creation_endpoint = (
    f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
)

# Automatically use today's date
today = datetime.now()

# ==========================================================
# Ask the user to enter today's cycling distance
# Only numeric values are accepted.
# Examples:
# 5
# 10.5
# 25
# ==========================================================
while True:
    distance = input("🚴 Enter today's cycling distance (in Km): ").strip()

    try:
        float(distance)
        break
    except ValueError:
        print("❌ Please enter a valid number (Example: 5 or 10.5)")

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": distance
}

# ==========================================================
# Send Data to Pixela
# ==========================================================
try:
    response = requests.post(
        url=pixel_creation_endpoint,
        json=pixel_data,
        headers=headers
    )

    response.raise_for_status()

    print("\n✅ Cycling record added successfully!")
    print(f"📅 Date      : {today.strftime('%d/%m/%Y')}")
    print(f"🚴 Distance  : {distance} Km")

except requests.exceptions.RequestException as error:
    print(f"\n❌ Error: {error}")

# ==========================================================
# Update Existing Pixel
# Uncomment this section if you want to update today's record.
# ==========================================================
update_endpoint = (
    f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/"
    f"{GRAPH_ID}/{today.strftime('%Y%m%d')}"
)

# Enter the new distance here
updated_pixel = {
    "quantity": "15.2"
}

# response = requests.put(
#     url=update_endpoint,
#     json=updated_pixel,
#     headers=headers
# )
#
# response.raise_for_status()
# print("✅ Pixel updated successfully!")
# print(response.json())

# ==========================================================
# Delete Existing Pixel
# Uncomment this section if you want to delete today's record.
# ==========================================================
delete_endpoint = (
    f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/"
    f"{GRAPH_ID}/{today.strftime('%Y%m%d')}"
)

# response = requests.delete(
#     url=delete_endpoint,
#     headers=headers
# )
#
# response.raise_for_status()
# print("🗑️ Pixel deleted successfully!")
# print(response.json())