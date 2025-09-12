import rhodecode

# Assuming you have the API client set up and your API key is set
client = rhodecode.RhodeCodeAPI(api_key="YOUR_API_KEY")

# Define the repository and updates
repository_id = "your_repository_id_or_name"
update_details = {
    "description": "New repository description",
    "private": True
}

# Update the repository using the API
try:
    response = client.update_repository(repository_id, **update_details)
    print("Repository updated successfully:", response)
except Exception as e:
    print("Failed to update repository:", str(e))
