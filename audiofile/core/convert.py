import logging
import subprocess

import audeer

from audiofile.core.utils import (
    broken_file_error,
    run_ffmpeg,
    run_sox,
)


def convert(
        infile: str,
        outfile: str,
        offset: float = 0,
        duration: float = None,
):
    """Convert any audio/video file to WAV.

    Args:
        infile: audio/video file name
        outfile: WAV file name
        duration: return only a specified duration in seconds
        offset: start reading at offset in seconds

    """
    try:
        # Convert to WAV file with sox
        from audiofile.core.sox import SOX_ERRORS
        run_sox(infile, outfile, offset, duration)
    except SOX_ERRORS:
        try:
            # Convert to WAV file with ffmpeg
            run_ffmpeg(infile, outfile, offset, duration)
        except subprocess.CalledProcessError:
            raise RuntimeError(broken_file_error(infile))
    except OSError:
        raise RuntimeError(broken_file_error(infile))
