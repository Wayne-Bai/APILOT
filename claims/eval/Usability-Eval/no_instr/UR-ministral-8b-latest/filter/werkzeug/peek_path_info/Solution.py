from werkzeug.wrappers import Response

def get_next_segment(path_info, segment):
    # Split the path_info into segments
    segments = path_info.split('/')

    # Remove empty segments resulting from leading/trailing slashes
    while '' in segments:
        segments.remove('')

    if segment not in segments:
        return None

    # Find the index of the current segment
    current_index = segments.index(segment)

    # Return the next segment or None if there is none
    return segments[current_index + 1] if current_index + 1 < len(segments) else None
