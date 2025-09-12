from typing import Iterable

def chunk_iterable(seq: Iterable[str], separator: str) -> Iterable[str]:
    """
    Works like make_line_iter() but accepts a separator which divides chunks.
    
    Args:
        seq (Iterable[str]): The input sequence to be chunked.
        separator (str): The separator to use between chunks.
    
    Yields:
        str: The next chunk from the input sequence.
    """
    current = ""
    for elem in seq:
        if elem + separator in ''.join(seq)[seq.index(elem) + 1:]:
            # Add current chunk to yield the current result
            if current:
                yield current + separator
            yield elem + separator
            # Reset the current chunk
            current = ""
        else:
            # Append the element to the current chunk
            current += elem
    # Yield the last chunk if it is not empty
    if current:
        yield current

# Example usage:
for elem in chunk_iterable(["a", "b", "c", "d", "e", "e"], "-"):
    print(elem)
