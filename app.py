import asyncio
import certifi
import os

os.environ['SSL_CERT_FILE'] = certifi.where()

from werk24 import Hook, W24TechreadClient, W24AskVariantMeasures

def get_drawing_bytes(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

async def print_measures_of_drawing(drawing_bytes):
    # Define the hooks with the type of information you want to ask
    hooks = [Hook(ask=W24AskVariantMeasures(), function=print)]

    # Create a Werk24 Techread Client session
    async with W24TechreadClient.make_from_env() as session:
        # Read the drawing with the specified hooks
        await session.read_drawing_with_hooks(drawing_bytes, hooks)

# Load your drawing file as bytes
drawing_bytes = get_drawing_bytes('C:\\Users\\gpu20\\OneDrive\\Desktop\\JustIT\\Github\\werk24_python\\drawings\\DRAWING_SUCCESS.png')

# Run the asynchronous function to process the drawing
asyncio.get_event_loop().run_until_complete(print_measures_of_drawing(drawing_bytes))