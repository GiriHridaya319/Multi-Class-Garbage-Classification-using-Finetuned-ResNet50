from fastapi import HTTPException
import os

def validate_image(file_size, file_extension):
    # Limit file size to 5MB
    if file_size > 5 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File size too large. Maximum size is 5MB.")
    
    # Validate file extension
    valid_extensions = ['.jpg', '.jpeg', '.png']
    if file_extension.lower() not in valid_extensions:
        raise HTTPException(status_code=400, 
                           detail=f"Invalid file extension. Supported formats are: {', '.join(valid_extensions)}")

def save_upload_file(file_content, upload_dir="uploads"):
    """Save uploaded file temporarily for debugging if needed"""
    os.makedirs(upload_dir, exist_ok=True)
    
    # You could implement saving the file here if needed
    # This is optional and not used in the main application flow
    pass