import jinja2

def create_overlay_environment(original_env, extra_extensions=None, override_attributes=None):
    # Create a copy of the original environment's attributes
    overlay_attrs = {
        'block_start_string': original_env.block_start_string,
        'block_end_string': original_env.block_end_string,
        'variable_start_string': original_env.variable_start_string,
        'variable_end_string': original_env.variable_end_string,
        'comment_start_string': original_env.comment_start_string,
        'comment_end_string': original_env.comment_end_string,
        'line_statement_prefix': original_env.line_statement_prefix,
        'line_comment_prefix': original_env.line_comment_prefix,
        'trim_blocks': original_env.trim_blocks,
        'lstrip_blocks': original_env.lstrip_blocks,
        'newline_sequence': original_env.newline_sequence,
        'keep_trailing_newline': original_env.keep_trailing_newline,
        'extensions': list(original_env.extensions),
        'autoescape': original_env.autoescape,
        'auto_reload': original_env.auto_reload,
        'cache_size': None,  # Disabling cache
    }

    # Include any additional extensions if provided
    if extra_extensions:
        overlay_attrs['extensions'].extend(extra_extensions)

    # Apply any overridden attributes
    if override_attributes:
        overlay_attrs.update(override_attributes)

    # Create overlay environment with modified attributes
    overlay_env = jinja2.Environment(**overlay_attrs)

    return overlay_env

# Example usage:

# Initialize the base environment with some configurations
base_env = jinja2.Environment(
    autoescape=True,
    cache_size=50,
    block_start_string='[%',
    block_end_string='%]',
    variable_start_string='[[',
    variable_end_string=']]'
)

# Create an overlay environment modifying some attributes and adding extra extensions
overlay_env = create_overlay_environment(
    base_env,
    extra_extensions=[jinja2.ext.loopcontrols],
    override_attributes={'autoescape': False, 'line_statement_prefix': '#'}
)
