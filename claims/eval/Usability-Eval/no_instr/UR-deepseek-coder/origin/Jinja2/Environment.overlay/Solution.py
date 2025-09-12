from jinja2 import Environment, FileSystemLoader, ChoiceLoader, DictLoader

def create_overlay_environment(base_env, extra_extensions=None, cache_override=None, overridden_attributes=None):
    """
    Create a new overlay environment that shares all the data with the current environment
    except for cache and the overridden attributes. Extensions cannot be removed for an overlayed environment.
    An overlayed environment automatically gets all the extensions of the environment it is linked to
    plus optional extra extensions.

    :param base_env: The base Jinja2 environment to overlay.
    :param extra_extensions: Optional extra extensions to add to the overlay environment.
    :param cache_override: Optional cache settings to override in the overlay environment.
    :param overridden_attributes: Optional attributes to override in the overlay environment.
    :return: A new Jinja2 environment that is an overlay of the base environment.
    """
    # Copy the base environment's settings
    overlay_env = Environment(
        loader=base_env.loader,
        autoescape=base_env.autoescape,
        variable_start_string=base_env.variable_start_string,
        variable_end_string=base_env.variable_end_string,
        block_start_string=base_env.block_start_string,
        block_end_string=base_env.block_end_string,
        comment_start_string=base_env.comment_start_string,
        comment_end_string=base_env.comment_end_string,
        line_statement_prefix=base_env.line_statement_prefix,
        line_comment_prefix=base_env.line_comment_prefix,
        trim_blocks=base_env.trim_blocks,
        lstrip_blocks=base_env.lstrip_blocks,
        newline_sequence=base_env.newline_sequence,
        keep_trailing_newline=base_env.keep_trailing_newline,
        extensions=base_env.extensions + (extra_extensions or [])
    )

    # Override cache settings if provided
    if cache_override is not None:
        overlay_env.cache = cache_override

    # Override specific attributes if provided
    if overridden_attributes:
        for attr, value in overridden_attributes.items():
            setattr(overlay_env, attr, value)

    return overlay_env

# Example usage:
# base_env = Environment(loader=FileSystemLoader('templates'))
# overlay_env = create_overlay_environment(base_env, extra_extensions=['jinja2.ext.i18n'], cache_override={}, overridden_attributes={'variable_start_string': '[[', 'variable_end_string': ']]'})
