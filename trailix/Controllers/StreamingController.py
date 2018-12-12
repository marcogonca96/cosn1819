from __future__ import print_function
import logging
import mimetypes
import os
import re

from flask import Response

logger = logging.getLogger(__name__)


class StreamingController():

    VIDEO_PATH = '/videos'

    MB = 1 << 20
    BUFF_SIZE = 10 * MB

    @staticmethod
    def partial_response(path, start, end=None):
        logger.info('Requested: %s, %s', start, end)
        file_size = os.path.getsize(path)

        # Determine (end, length)
        if end is None:
            end = start + BUFF_SIZE - 1
        end = min(end, file_size - 1)
        end = min(end, start + BUFF_SIZE - 1)
        length = end - start + 1

        # Read file
        with open(path, 'rb') as fd:
            fd.seek(start)
            bytes = fd.read(length)
        assert len(bytes) == length

        response = Response(
            bytes,
            206,
            mimetype=mimetypes.guess_type(path)[0],
            direct_passthrough=True,
        )
        response.headers.add(
            'Content-Range', 'bytes {0}-{1}/{2}'.format(
                start, end, file_size,
            ),
        )
        response.headers.add(
            'Accept-Ranges', 'bytes'
        )
        logger.info('Response: %s', response)
        logger.info('Response: %s', response.headers)
        return response

    @staticmethod
    def get_range(request):
        range = request.headers.get('Range')
        logger.info('Requested: %s', range)
        m = re.match('bytes=(?P<start>\d+)-(?P<end>\d+)?', range)
        if m:
            start = m.group('start')
            end = m.group('end')
            start = int(start)
            if end is not None:
                end = int(end)
            return start, end
        else:
            return 0, None

    @staticmethod
    @app.route(VIDEO_PATH)
    def video():
        path = 'videos/lionKingTrailer'
        start, end = get_range(request)
        return partial_response(path, start, end)
