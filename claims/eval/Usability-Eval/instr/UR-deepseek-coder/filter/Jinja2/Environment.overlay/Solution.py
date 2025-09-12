from jinja2 import Environment, FileSystemLoader, ChoiceLoader, PrefixLoader

def create_overlay_environment(base_env, extra_extensions=None):
    # Copy the base environment's settings
    overlay_env = Environment(
        block_start_string=base_env.block_start_string,
        block_end_string=base_env.block_end_string,
        variable_start_string=base_env.variable_start_string,
        variable_end_string=base_env.variable_end_string,
        comment_start_string=base_env.comment_start_string,
        comment_end_string=base_env.comment_end_string,
        line_statement_prefix=base_env.line_statement_prefix,
        line_comment_prefix=base_env.line_comment_prefix,
        trim_blocks=base_env.trim_blocks,
        lstrip_blocks=base_env.lstrip_blocks,
        newline_sequence=base_env.newline_sequence,
        keep_trailing_newline=base_env.keep_trailing_newline,
        extensions=base_env.extensions + (extra_extensions or []),
        optimized=base_env.optimized,
        undefined=base_env.undefined,
        finalize=base_env.finalize,
        autoescape=base_env.autoescape,
        loader=ChoiceLoader([base_env.loader, FileSystemLoader('.')]),
        cache_size=0,  # Disable cache for the overlay environment
        auto_reload=base_env.auto_reload,
        bytecode_cache=None  # Disable bytecode cache for the overlay environment
    )

    # Copy over the globals, filters, tests, and policies
    overlay_env.globals.update(base_env.globals)
    overlay_env.filters.update(base_env.filters)
    overlay_env.tests.update(base_env.tests)
    overlay_env.policies.update(base_env.policies)

    return overlay_env

# Example usage:
# base_env = Environment(...)
# overlay_env = create_overlay_environment(base_env, extra_extensions=['jinja2.ext.do'])
