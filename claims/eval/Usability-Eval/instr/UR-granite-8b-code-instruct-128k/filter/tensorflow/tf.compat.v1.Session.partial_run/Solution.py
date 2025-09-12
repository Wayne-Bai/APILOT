import tensorflow as tf

# Assume you have already defined your graph and session
# ...

# Define new feeds and fetches
new_feeds = {new_input_op: new_input_data}
new_fetches = {new_output_op: new_output_data}

# Run the new feeds and fetches
new_results = session.run(new_fetches, new_feeds)

# Print the results
print(new_results)
