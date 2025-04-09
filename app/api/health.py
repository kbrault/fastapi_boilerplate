from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
import time

router = APIRouter()

@router.get("/health", tags=["Health"])
async def health_check():
    start = time.perf_counter()
    checks = {"app": "ok"}
    duration = time.perf_counter() - start

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "pass",
            "details": checks,
            "response_time_ms": round(duration * 1000, 2)
        },
    )
