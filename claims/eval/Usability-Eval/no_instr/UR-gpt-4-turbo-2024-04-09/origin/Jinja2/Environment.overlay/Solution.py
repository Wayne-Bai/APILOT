import jinja2

def create_overlay_environment(original_env, override_attributes=None, extra_extensions=None):
    """
    Create a new overlay environment based on an existing Jinja2 environment.
    
    Parameters:
    - original_env: The original Jinja2 Environment instance
    - override_attributes: Dictionary of attributes to override in the new environment
    - extra_extensions: List of additional extensions to include in the new environment
    
    Returns:
    - Jinja2 Environment instance (overlay environment)
    """
    if override_attributes is None:
        override_attributes = {}
    if extra_extensions is None:
        extra_extensions = []
    
    # Create a duplicate of the original environment's configuration.
    overlay_env = jinja2.Environment(
        loader=original_env.loader,
        block_start_string=original_env.block_start_string,
        block_end_string=original_env.block_end_string,
        variable_start_string=original_env.variable_start_string,
        variable_end_string=original_env.variable_end_string,
        comment_start_string=original_env.comment_start_string,
        comment_end_string=original_env.comment_end_string,
        line_statement_prefix=original_env.line_statement_prefix,
        line_comment_prefix=original_env.line_comment_prefix,
        trim_blocks=original_env.trim_blocks,
        lstrip_blocks=original_env.lstrip_blocks,
        newline_sequence=original_env.newline_sequence,
        keep_trailing_newline=original_env.keep_trailing_newline,
        extensions=list(original_env.extensions) + extra_extensions,  # Include existing plus any extra extensions
        optimized=original_env.optimized,
        autoescape=original_env.autoescape
    )

    # Apply the attribute overrides
    for attr, value in override_attributes.items():
        setattr(overlay_env, attr, value)
    
    return overlay_env

# Usage example
original_environment = jinja2.Environment()
overlay_environment = create_overlay_environment(
    original_environment,
    override_attributes={'autoescape': True},
    extra_extensions=['jinja2.ext.do']
)
