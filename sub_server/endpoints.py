from PIL import ImageGrab
from datetime import datetime
from starlette.responses import FileResponse

async def take_screenshot(request):
    file_name = f"{datetime.now()}.png"
    snapshot = ImageGrab.grab()
    snapshot.save(file_name)

    return FileResponse(file_name)
